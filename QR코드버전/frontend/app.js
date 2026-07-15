let currentStudent = null;
let selectedTags = [];
let currentProjectId = null;
let currentProgressNote = '';
let currentWizardStep = 0;
let recommendedItems = [];
let recommendationPage = 0;
let lastDashboard = [];
let teacherPassword = '';
let studentAiModeActive = false;

const TAGS = ['AI','스마트폰','유튜브','SNS','게임','웹툰','K-POP','영화','음악','스포츠','건강','수면','스트레스','음식','환경','기후변화','플라스틱','동물','생명윤리','과학','로봇','데이터','수학','학습법','독서','진로','친구관계','학교생활','소비습관','지역사회'];
const WIZARD_PAGES = ['wizardPlan', 'wizardGuide', 'wizardSurvey', 'wizardInterview', 'wizardLog', 'wizardReport', 'wizardPrint'];
const WIZARD_PROGRESS = [30, 45, 60, 70, 80, 90, 100];
const RECOMMEND_PAGE_SIZE = 5;
const RECOMMEND_MAX_ITEMS = 15;
window.onload = () => {
  const tagBox = document.getElementById('tags');
  if (tagBox) tagBox.innerHTML = TAGS.map(t => `<span class="tag" onclick="selectTag(this,'${t}')">${t}</span>`).join('');
  initTeacherPage();
  initWizardPage();
  initAiSettingsPage();
  initAiSettingsInputs();
  initInternetStatus();
};

function selectTag(el, tag) {
  const exists = selectedTags.includes(tag);
  if (exists) {
    selectedTags = selectedTags.filter(x => x !== tag);
    el.classList.remove('active');
    return;
  }
  if (selectedTags.length >= 2) return alert('버튼 관심사는 최대 2개까지 선택할 수 있습니다.');
  selectedTags.push(tag);
  el.classList.add('active');
}

function parseDetailInterests() {
  return valueOf('detail').split(/[,，、]/).map(item => item.trim()).filter(Boolean);
}

function getInterestQuery() {
  const detailItems = parseDetailInterests();
  const detail = detailItems.join(' + ');
  const tagText = selectedTags.join(' + ');
  const parts = [];
  if (detail) parts.push(`직접 입력: ${detail}`);
  if (tagText) parts.push(`버튼 선택: ${tagText}`);
  return { detail, detailItems, tagText, queryText: parts.join(' + ') };
}

function validateInterestSelection(detailItems) {
  const total = selectedTags.length + detailItems.length;
  if (total === 0) return '버튼 관심사를 선택하거나 직접 관심사를 입력하세요.';
  if (detailItems.length > 2) return '직접 입력 관심사는 쉼표(,)로 구분해 최대 2개까지 입력하세요.';
  if (total > 2) return '버튼 관심사와 직접 입력 관심사를 합쳐 최대 2개까지 융합할 수 있습니다.';
  return '';
}

async function post(url, data) {
  const res = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
  return res.json();
}

function esc(value) {
  return String(value ?? '').replace(/[&<>\"]/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[ch]));
}

function valueOf(id) {
  return document.getElementById(id)?.value || '';
}

function numberOf(id) {
  return Number(valueOf(id) || 0);
}

function setValue(id, value) {
  const el = document.getElementById(id);
  if (el) el.value = value || '';
}

function clamp(value) {
  return Math.max(0, Math.min(100, Math.round(Number(value || 0))));
}

function setInternetStatus(online) {
  const box = document.getElementById('internetStatus');
  if (!box) return;
  box.classList.toggle('online', online);
  box.classList.toggle('offline', !online);
  box.classList.remove('checking');
  box.innerHTML = `<span class="status-dot"></span><span>${online ? '인터넷이 연결되어 있음' : '인터넷이 연결되어 있지 않음'}</span>`;
}

async function initInternetStatus() {
  const box = document.getElementById('internetStatus');
  if (!box) return;
  if (!navigator.onLine) return setInternetStatus(false);
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 3000);
  try {
    await fetch('https://www.gstatic.com/generate_204', { mode: 'no-cors', cache: 'no-store', signal: controller.signal });
    setInternetStatus(true);
  } catch (error) {
    setInternetStatus(false);
  } finally {
    clearTimeout(timeout);
  }
  window.addEventListener('online', () => setInternetStatus(true));
  window.addEventListener('offline', () => setInternetStatus(false));
}

async function refreshStudentAiMode() {
  const box = document.getElementById('customTopicBox');
  if (!box) return false;
  try {
    const res = await (await fetch('/api/class-info', { cache: 'no-store' })).json();
    studentAiModeActive = !!res.ai_mode_active;
  } catch (error) {
    studentAiModeActive = false;
  }
  box.classList.toggle('hidden', !studentAiModeActive);
  const input = document.getElementById('customTopic');
  const button = box.querySelector('button');
  if (input) input.disabled = !studentAiModeActive;
  if (button) button.disabled = !studentAiModeActive;
  return studentAiModeActive;
}

async function login() {
  const name = document.getElementById('name').value.trim();
  const student_no = document.getElementById('studentNo').value.trim();
  if (!name || !student_no) return alert('학번과 이름을 입력하세요.');
  currentStudent = await post('/api/student/login', { name, student_no });
  document.getElementById('loginBox').classList.add('hidden');
  document.getElementById('interestBox').classList.remove('hidden');
  await refreshStudentAiMode();
  await loadMyProjects();
}

function renderFeedbackHistory(feedbacks = []) {
  if (!feedbacks.length) return '';
  return `<div class="feedback-box">
    <h4>교사 피드백</h4>
    <div class="feedback-list">${feedbacks.map(f => `
      <div class="feedback-item">
        <b>${esc(f.created_at || '')}</b>
        <p>${esc(f.teacher_comment || '교사 피드백이 아직 입력되지 않았습니다.')}</p>
      </div>`).join('')}</div>
  </div>`;
}

async function loadMyProjects() {
  const res = await (await fetch(`/api/student/${currentStudent.id}/projects`)).json();
  const box = document.getElementById('myProjectsBox');
  const list = document.getElementById('myProjects');
  if (!res.items.length) {
    box.classList.add('hidden');
    list.innerHTML = '';
    return;
  }
  box.classList.remove('hidden');
  list.innerHTML = res.items.map(p => `
    <div class="topic">
      <h3>${esc(p.topic)}</h3>
      <p class="muted">진행률 ${p.progress}% · 적합도 ${p.fit_score}점</p>
      <div class="bar"><span style="width:${clamp(p.progress)}%"></span></div>
      ${renderFeedbackHistory(p.feedbacks || [])}
      <label class="field-label" for="note${p.id}">진행 상황</label>
      <textarea class="progress-note" id="note${p.id}" placeholder="오늘 진행한 내용, 어려운 점, 다음 계획을 적어보세요.">${esc(p.progress_note || '')}</textarea>
      <div class="row">
        <button class="btn secondary" onclick="openProject(${p.id})">이어하기</button>
        <button class="btn" onclick="saveProgressNote(${p.id})">진행 상황 저장</button>
        <button class="btn danger" onclick="deleteProject(${p.id})">삭제</button>
      </div>
    </div>`).join('');
}

async function saveProgressNote(projectId) {
  const note = document.getElementById(`note${projectId}`).value;
  const res = await fetch(`/api/projects/${projectId}/progress-note`, {
    method: 'PUT', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ progress_note: note }),
  });
  if (!res.ok) return alert('진행 상황 저장에 실패했습니다.');
  alert('진행 상황이 저장되었습니다.');
}

function openProject(id) {
  window.location.href = `wizard.html?project_id=${id}`;
}

async function deleteProject(projectId) {
  const ok = confirm('이 탐구와 저장된 진행 상황, 교사 피드백을 삭제할까요?');
  if (!ok) return;
  const res = await fetch(`/api/projects/${projectId}`, { method: 'DELETE' });
  if (!res.ok) return alert('탐구 삭제에 실패했습니다.');
  alert('탐구가 삭제되었습니다.');
  await loadMyProjects();
}

async function recommend() {
  const { detail, detailItems, tagText, queryText } = getInterestQuery();
  const error = validateInterestSelection(detailItems);
  if (error) return alert(error);

  const loading = document.getElementById('recommendLoading');
  const elapsed = document.getElementById('recommendElapsed');
  const button = document.getElementById('recommendBtn');
  const startedAt = Date.now();
  if (loading) loading.classList.remove('hidden');
  if (elapsed) elapsed.innerText = '0';
  if (button) {
    button.disabled = true;
    button.innerText = 'AI 추천 생성 중...';
  }
  const timer = setInterval(() => {
    if (elapsed) elapsed.innerText = String(Math.floor((Date.now() - startedAt) / 1000));
  }, 1000);

  try {
    const res = await post('/api/recommend', { tag: tagText, detail });
    recommendedItems = (res.items || []).sort((a, b) => (b.fit?.total || 0) - (a.fit?.total || 0)).slice(0, RECOMMEND_MAX_ITEMS);
    recommendationPage = 0;
    document.getElementById('recommendBox').classList.remove('hidden');
    const mode = res.mode === 'online'
      ? '온라인 AI 추천 결과입니다.'
      : (res.ai_error ? `AI 호출에 실패해 오프라인 결과를 표시합니다. ${res.ai_error}` : '오프라인 추천 엔진 결과입니다.');
    document.getElementById('modeText').innerText = `${mode} ${queryText} 기준으로 관련 주제를 점수가 높은 순서대로 5개씩 보여줍니다.`;
    if (res.ai_error) alert('OpenAI 호출이 실패했습니다. AI 설정에서 API 키와 계정 사용 한도를 확인해 주세요.');
    renderRecommendations();
    document.getElementById('recommendBox')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  } catch (error) {
    alert('추천 결과를 불러오지 못했습니다. 인터넷 연결을 확인한 뒤 다시 시도해 주세요.');
  } finally {
    clearInterval(timer);
    if (loading) loading.classList.add('hidden');
    if (button) {
      button.disabled = false;
      button.innerText = '탐구주제 추천받기';
    }
  }
}

function renderRecommendations() {
  const start = recommendationPage * RECOMMEND_PAGE_SIZE;
  const pageItems = recommendedItems.slice(start, start + RECOMMEND_PAGE_SIZE);
  const totalPages = Math.max(1, Math.ceil(recommendedItems.length / RECOMMEND_PAGE_SIZE));
  document.getElementById('topics').innerHTML = pageItems.map(it => {
    const fit = it.fit || {};
    return `<div class="topic">
      <h3>${esc(it.topic)}</h3>
      <p><b>교과</b> ${esc(it.subject)} · <b>난이도</b> ${esc(it.difficulty)} · <b>유형</b> ${esc(it.inquiry_type)} · <b>기간</b> ${esc(it.duration)}</p>
      <p class="muted">${esc(it.reason)}</p>
      <div class="score">${fit.total || 70}점</div>
      <div class="bar"><span style="width:${clamp(fit.total || 70)}%"></span></div>
      <div class="fit-grid"><span>자료 ${fit.data_collection || '-'}</span><span>설문 ${fit.survey || '-'}</span><span>실험 ${fit.experiment || '-'}</span><span>학교 ${fit.school_application || '-'}</span></div>
      <button class="btn" onclick='startProject(${JSON.stringify(it).replace(/'/g, "&#39;")})'>이 주제로 시작</button>
    </div>`;
  }).join('');
  const nav = document.getElementById('recommendNav');
  if (!nav) return;
  nav.innerHTML = `<button class="btn secondary" onclick="showRecommendationPage(-1)" ${recommendationPage === 0 ? 'disabled' : ''}>이전</button><span class="page-info">${recommendationPage + 1} / ${totalPages}쪽 · ${recommendedItems.length}개 중 ${start + 1}-${start + pageItems.length}번</span><button class="btn" onclick="showRecommendationPage(1)" ${recommendationPage >= totalPages - 1 ? 'disabled' : ''}>다음</button>`;
}

function showRecommendationPage(direction) {
  const totalPages = Math.max(1, Math.ceil(recommendedItems.length / RECOMMEND_PAGE_SIZE));
  recommendationPage = Math.max(0, Math.min(totalPages - 1, recommendationPage + direction));
  renderRecommendations();
  document.getElementById('recommendBox')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

async function startProject(item) {
  const fit = item.fit || {};
  const { detail, tagText } = getInterestQuery();
  const res = await post('/api/projects', { student_id: currentStudent.id, tag: tagText, interest: detail, topic: item.topic, subject: item.subject || '', fit_score: fit.total || 70 });
  window.location.href = `wizard.html?project_id=${res.project_id}`;
}

async function startCustomTopic() {
  if (!currentStudent) return alert('먼저 학번과 이름을 입력해 주세요.');
  if (!(await refreshStudentAiMode())) return alert('직접 주제 입력은 AI 모드에서만 사용할 수 있습니다. 교사에게 AI 모드 활성화를 요청해 주세요.');
  const topic = valueOf('customTopic').trim();
  if (topic.length < 8) return alert('대상, 핵심 개념 또는 비교 기준이 드러나도록 탐구주제를 조금 더 구체적으로 입력해 주세요.');
  const { detail, tagText } = getInterestQuery();
  const interest = detail || topic;
  const response = await fetch('/api/projects', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      student_id: currentStudent.id,
      tag: tagText || '직접 주제',
      interest,
      topic,
      subject: '자율탐구',
      fit_score: 80,
      custom_topic: true,
    }),
  });
  const res = await response.json();
  if (!response.ok) {
    await refreshStudentAiMode();
    return alert(res.detail || 'AI 모드에서만 직접 주제로 시작할 수 있습니다.');
  }
  window.location.href = `wizard.html?project_id=${res.project_id}`;
}

async function initWizardPage() {
  const box = document.getElementById('projectBox');
  if (!box) return;
  const id = new URLSearchParams(location.search).get('project_id');
  if (!id) {
    box.innerHTML = '<h2>프로젝트를 찾을 수 없습니다.</h2><p class="muted">학생 탐구실에서 주제를 선택하세요.</p><a class="btn" href="student.html">학생 탐구실로 이동</a>';
    return;
  }
  await loadWizardProject(id);
}

async function loadWizardProject(id) {
  const p = await (await fetch(`/api/projects/${id}`)).json();
  currentProjectId = p.id;
  currentProgressNote = p.progress_note || '';
  document.getElementById('projectTopic').innerText = p.topic;
  setValue('plan', p.plan);
  setValue('planNote', p.plan_note);
  setValue('guideNote', p.guide_note);
  setValue('surveyNote', p.survey_note);
  setValue('interviewNote', p.interview_note);
  setValue('log', p.research_log);
  setValue('reportNote', p.report_note);
  document.getElementById('reportOutput').innerHTML = p.report ? `<pre>${esc(p.report)}</pre>` : '';
  const progress = Number(p.progress || 30);
  const step = progress >= 100 ? 6 : progress >= 90 ? 5 : progress >= 80 ? 4 : progress >= 70 ? 3 : progress >= 60 ? 2 : progress >= 45 ? 1 : 0;
  setWizardStep(step, progress);
}

function setWizardStep(step, progressOverride = null) {
  currentWizardStep = Math.max(0, Math.min(WIZARD_PAGES.length - 1, step));
  WIZARD_PAGES.forEach((id, index) => document.getElementById(id)?.classList.toggle('hidden', index !== currentWizardStep));
  document.querySelectorAll('#wizardStepper span').forEach((item, index) => {
    item.classList.toggle('active', index === currentWizardStep);
    item.classList.toggle('done', index < currentWizardStep);
  });
  const prev = document.getElementById('prevWizardBtn');
  const next = document.getElementById('nextWizardBtn');
  if (prev) prev.disabled = currentWizardStep === 0;
  if (next) next.innerText = currentWizardStep === WIZARD_PAGES.length - 1 ? '완료' : '다음';
  updateProgress(progressOverride ?? WIZARD_PROGRESS[currentWizardStep]);
  if (WIZARD_PAGES[currentWizardStep] === 'wizardPrint') renderPrintSummary();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

async function nextWizardStep() {
  if (currentWizardStep < WIZARD_PAGES.length - 1) {
    await saveProject(WIZARD_PROGRESS[currentWizardStep], false);
    setWizardStep(currentWizardStep + 1);
    return;
  }
  await saveProject(100, false);
  renderPrintSummary();
  alert('완료 내용이 저장되었습니다. PDF로 저장하려면 인쇄 창에서 프린터를 PDF 저장으로 선택하세요.');
}

async function prevWizardStep() {
  await saveProject(WIZARD_PROGRESS[currentWizardStep], false);
  setWizardStep(currentWizardStep - 1);
}

function autoProgress() {
  let progress = WIZARD_PROGRESS[currentWizardStep] || 30;
  if ((valueOf('plan') || '').trim().length > 50 || (valueOf('planNote') || '').trim().length > 10) progress = Math.max(progress, 45);
  if ((document.getElementById('guideOutput')?.innerText || '').trim().length > 20 || (valueOf('guideNote') || '').trim().length > 10) progress = Math.max(progress, 55);
  if ((document.getElementById('surveyOutput')?.innerText || '').trim().length > 20 || (valueOf('surveyNote') || '').trim().length > 10) progress = Math.max(progress, 65);
  if ((document.getElementById('interviewOutput')?.innerText || '').trim().length > 20 || (valueOf('interviewNote') || '').trim().length > 10) progress = Math.max(progress, 75);
  if ((valueOf('log') || '').trim().length > 20) progress = Math.max(progress, 80);
  if ((document.getElementById('reportOutput')?.innerText || '').trim().length > 20 || (valueOf('reportNote') || '').trim().length > 10) progress = Math.max(progress, 90);
  if (currentWizardStep === WIZARD_PAGES.length - 1) progress = Math.max(progress, 100);
  updateProgress(progress);
  return progress;
}

function updateProgress(progress) {
  progress = clamp(progress);
  const text = document.getElementById('progressText');
  const barEl = document.getElementById('progressBar');
  if (text) text.innerText = `진행률 ${progress}%`;
  if (barEl) barEl.style.width = `${progress}%`;
}

async function saveProject(progress = autoProgress(), showAlert = false) {
  if (!currentProjectId) return null;
  const res = await fetch(`/api/projects/${currentProjectId}`, {
    method: 'PUT', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ plan: valueOf('plan'), plan_note: valueOf('planNote'), guide_note: valueOf('guideNote'), survey_note: valueOf('surveyNote'), interview_note: valueOf('interviewNote'), research_log: valueOf('log'), progress_note: currentProgressNote, report: document.getElementById('reportOutput').innerText, report_note: valueOf('reportNote'), progress }),
  });
  if (!res.ok) {
    alert('저장에 실패했습니다. 잠시 후 다시 시도하세요.');
    throw new Error('project save failed');
  }
  updateProgress(progress);
  if (showAlert) alert('저장되었습니다.');
  return res.json();
}

async function loadGuide() {
  const res = await (await fetch(`/api/projects/${currentProjectId}/guide`)).json();
  document.getElementById('guideOutput').innerHTML = `<div class="result"><h3>자료조사 가이드</h3><ol>${res.items.map(x => `<li>${esc(x)}</li>`).join('')}</ol></div>`;
  await saveProject(autoProgress());
}

async function loadSurvey() {
  const res = await (await fetch(`/api/projects/${currentProjectId}/survey`)).json();
  document.getElementById('surveyOutput').innerHTML = `<div class="result"><h3>설문 문항</h3><ol>${res.items.map(x => `<li>${esc(x)}</li>`).join('')}</ol></div>`;
  await saveProject(autoProgress());
}

async function loadInterview() {
  const res = await (await fetch(`/api/projects/${currentProjectId}/interview`)).json();
  document.getElementById('interviewOutput').innerHTML = `<div class="result"><h3>인터뷰 질문</h3><ol>${res.items.map(x => `<li>${esc(x)}</li>`).join('')}</ol></div>`;
  await saveProject(autoProgress());
}

async function makeReport() {
  await saveProject(80);
  const res = await post(`/api/projects/${currentProjectId}/report`, {});
  document.getElementById('reportOutput').innerHTML = `<pre>${esc(res.report)}</pre>`;
  setWizardStep(5, 90);
  await saveProject(90);
}

function summarySection(title, text) {
  return `<section><h3>${esc(title)}</h3><div class="summary-text">${esc(text || '아직 작성된 내용이 없습니다.')}</div></section>`;
}

function renderPrintSummary() {
  const box = document.getElementById('printSummary');
  if (!box) return;
  const reportText = document.getElementById('reportOutput')?.innerText || '';
  box.innerHTML = `<h2>AI 탐구메이트 정리내용</h2><p><b>탐구 주제</b> ${esc(document.getElementById('projectTopic')?.innerText || '')}</p>${summarySection('탐구계획서', valueOf('plan'))}${summarySection('계획서 메모', valueOf('planNote'))}${summarySection('자료조사 메모', valueOf('guideNote'))}${summarySection('설문 메모', valueOf('surveyNote'))}${summarySection('인터뷰 메모', valueOf('interviewNote'))}${summarySection('탐구일지', valueOf('log'))}${summarySection('보고서 초안', reportText)}${summarySection('보고서 정리 메모', valueOf('reportNote'))}`;
}

async function printSummary() {
  await saveProject(100, false);
  renderPrintSummary();
  window.print();
}

async function getTeacherPasswordStatus() {
  try {
    return await (await fetch('/api/teacher/password-status')).json();
  } catch (error) {
    return { has_password: true, has_hint: false };
  }
}

function updateTeacherPasswordStatus(status) {
  const hasPassword = !!status.has_password;
  const text = document.getElementById('teacherPasswordStatus');
  const title = document.getElementById('teacherAuthTitle');
  if (title) title.innerText = hasPassword ? '교사 로그인' : '교사 비밀번호 설정';
  if (text) {
    text.innerText = hasPassword
      ? '설정한 교사 비밀번호를 입력하세요.'
      : '처음 사용할 비밀번호와 필요한 경우 힌트를 설정하세요.';
  }
  document.getElementById('teacherLoginFields')?.classList.toggle('hidden', !hasPassword);
  document.getElementById('teacherPasswordPanel')?.classList.toggle('hidden', hasPassword);
  document.getElementById('cancelPasswordSetupBtn')?.classList.toggle('hidden', !hasPassword);
  document.getElementById('teacherHintBtn')?.classList.toggle('hidden', !hasPassword || !status.has_hint);
  document.getElementById('teacherRecoverPanel')?.classList.add('hidden');
}

async function initTeacherPage() {
  if (!document.getElementById('teacherLogin')) return;
  const status = await getTeacherPasswordStatus();
  updateTeacherPasswordStatus(status);
  teacherPassword = '';
  sessionStorage.removeItem('teacherPassword');
  document.getElementById('dash')?.classList.add('hidden');
  if (status.has_password) {
    document.getElementById('teacherModeSelect')?.classList.add('hidden');
    document.getElementById('teacherLogin')?.classList.remove('hidden');
    document.getElementById('teacherPw')?.focus();
    return;
  }
  document.getElementById('teacherModeSelect')?.classList.remove('hidden');
  document.getElementById('teacherLogin')?.classList.add('hidden');
}

function chooseTeacherMode(mode) {
  if (mode === 'ai') {
    window.location.href = 'ai-settings.html';
    return;
  }
  startOfflineTeacherMode();
}

async function startOfflineTeacherMode() {
  document.getElementById('teacherModeSelect')?.classList.add('hidden');
  const status = await getTeacherPasswordStatus();
  updateTeacherPasswordStatus(status);
  document.getElementById('teacherLogin')?.classList.remove('hidden');
  document.getElementById('dash')?.classList.add('hidden');
  if (status.has_password) document.getElementById('teacherPw')?.focus();
  else document.getElementById('newTeacherPw')?.focus();
}

async function showTeacherPasswordPanel() {
  const status = await getTeacherPasswordStatus();
  if (status.has_password && !teacherPassword) {
    alert('비밀번호 변경은 교사 로그인 후 사용할 수 있습니다.');
    return;
  }
  document.getElementById('teacherLogin')?.classList.remove('hidden');
  document.getElementById('teacherLoginFields')?.classList.add('hidden');
  document.getElementById('teacherPasswordPanel')?.classList.remove('hidden');
  document.getElementById('cancelPasswordSetupBtn')?.classList.toggle('hidden', !status.has_password);
  setValue('newTeacherPw', '');
  setValue('confirmTeacherPw', '');
  setValue('teacherPwHint', '');
  document.getElementById('newTeacherPw')?.focus();
}

function hideTeacherPasswordPanel() {
  document.getElementById('teacherPasswordPanel')?.classList.add('hidden');
  if (!document.getElementById('dash')?.classList.contains('hidden')) {
    document.getElementById('teacherLogin')?.classList.add('hidden');
    return;
  }
  document.getElementById('teacherLoginFields')?.classList.remove('hidden');
  document.getElementById('teacherPw')?.focus();
}

async function setTeacherPassword() {
  const password = valueOf('newTeacherPw').trim();
  const confirmation = valueOf('confirmTeacherPw').trim();
  if (!password) return alert('새 비밀번호를 입력하세요.');
  if (password !== confirmation) return alert('비밀번호 확인이 일치하지 않습니다.');
  const payload = {
    password,
    hint: valueOf('teacherPwHint').trim(),
    current_password: teacherPassword,
  };
  const res = await post('/api/teacher/password', payload);
  if (!res.ok) return alert(res.detail === 'invalid teacher password' ? '로그인 정보가 만료되었습니다. 다시 로그인하세요.' : '비밀번호 저장에 실패했습니다.');

  teacherPassword = password;
  sessionStorage.setItem('teacherPassword', password);
  document.getElementById('teacherLogin')?.classList.add('hidden');
  document.getElementById('teacherPasswordPanel')?.classList.add('hidden');
  document.getElementById('dash')?.classList.remove('hidden');
  setValue('teacherPw', '');
  setValue('newTeacherPw', '');
  setValue('confirmTeacherPw', '');
  alert('교사 비밀번호가 저장되었습니다.');
  await loadDashboard();
}

async function recoverTeacherPassword() {
  const hint = valueOf('teacherRecoverHint').trim();
  if (!hint) return alert('힌트를 입력하세요.');
  const res = await post('/api/teacher/password/recover', { hint });
  const result = document.getElementById('teacherRecoverResult');
  if (!res.ok) {
    if (result) result.innerText = '힌트가 일치하지 않습니다.';
    return;
  }
  if (result) result.innerText = `비밀번호: ${res.password}`;
}

async function showTeacherHintPanel() {
  const status = await getTeacherPasswordStatus();
  updateTeacherPasswordStatus(status);
  if (!status.has_hint) return alert('저장된 비밀번호 힌트가 없습니다.');
  document.getElementById('teacherRecoverPanel')?.classList.remove('hidden');
  document.getElementById('teacherRecoverHint')?.focus();
}

async function teacherLogin() {
  const password = document.getElementById('teacherPw').value;
  const res = await post('/api/teacher/login', { password });
  if (!res.ok) return alert('비밀번호가 올바르지 않습니다.');
  teacherPassword = password;
  sessionStorage.setItem('teacherPassword', password);
  document.getElementById('teacherLogin').classList.add('hidden');
  document.getElementById('dash').classList.remove('hidden');
  await loadDashboard();
}

async function aiSettingsLogin() {
  const password = valueOf('aiSettingsPw');
  const res = await post('/api/teacher/login', { password });
  if (!res.ok) return alert('비밀번호가 올바르지 않습니다.');
  teacherPassword = password;
  sessionStorage.setItem('teacherPassword', password);
  document.getElementById('aiSettingsLogin')?.classList.add('hidden');
  document.getElementById('aiSettingsBox')?.classList.remove('hidden');
  await loadAiSettings();
}

async function initAiSettingsPage() {
  if (!document.getElementById('aiSettingsLogin')) return;
  const status = await getTeacherPasswordStatus();
  teacherPassword = sessionStorage.getItem('teacherPassword') || '';
  if (!status.has_password) {
    teacherPassword = '';
  } else if (!teacherPassword) {
    return;
  } else {
    const auth = await post('/api/teacher/login', { password: teacherPassword });
    if (!auth.ok) return;
  }
  document.getElementById('aiSettingsLogin')?.classList.add('hidden');
  document.getElementById('aiSettingsBox')?.classList.remove('hidden');
  await loadAiSettings();
}

async function loadAiSettings() {
  if (!teacherPassword) return;
  const status = document.getElementById('aiSettingsStatus');
  if (status) status.innerText = 'AI 설정을 불러오는 중입니다.';
  const res = await post('/api/teacher/ai-settings', { password: teacherPassword });
  if (res.detail) {
    if (status) status.innerText = 'AI 설정을 불러오지 못했습니다.';
    return;
  }
  const enabled = document.getElementById('onlineAiEnabled');
  const clear = document.getElementById('clearAiKey');
  const keyInput = document.getElementById('aiApiKey');
  if (enabled) enabled.checked = !!res.online_ai_enabled;
  if (clear) clear.checked = false;
  if (keyInput) keyInput.value = '';
  const keyHint = document.getElementById('aiKeyHint');
  if (keyHint) keyHint.innerText = res.has_api_key ? `저장된 키: ${res.masked_api_key} · 자동 선택 모델: ${res.model}` : '저장된 API 키가 없습니다.';
  if (status) status.innerText = res.online_ai_enabled && res.has_api_key ? '온라인 AI 사용 중입니다.' : '오프라인 추천 엔진을 사용 중입니다.';
}

function initAiSettingsInputs() {
  const keyInput = document.getElementById('aiApiKey');
  const enabled = document.getElementById('onlineAiEnabled');
  if (!keyInput || !enabled || keyInput.dataset.boundAutoEnable) return;
  keyInput.dataset.boundAutoEnable = '1';
  keyInput.addEventListener('input', () => {
    if (keyInput.value.trim()) enabled.checked = true;
  });
}

async function saveAiSettings() {
  if (!teacherPassword) return alert('교사 로그인 후 사용할 수 있습니다.');
  const button = document.getElementById('saveAiSettingsBtn');
  const status = document.getElementById('aiSettingsStatus');
  const payload = { password: teacherPassword, online_ai_enabled: !!document.getElementById('onlineAiEnabled')?.checked, openai_api_key: valueOf('aiApiKey'), clear_api_key: !!document.getElementById('clearAiKey')?.checked };
  if (button) {
    button.disabled = true;
    button.innerText = 'API 키 확인 중...';
  }
  if (status) status.innerText = 'OpenAI 서버에서 API 키의 유효성을 확인하고 있습니다.';
  try {
    const res = await post('/api/teacher/ai-settings/save', payload);
    if (!res.ok) {
      if (status) status.innerText = res.detail || 'API 키 확인에 실패했습니다.';
      return alert(res.detail || 'AI 설정 저장에 실패했습니다.');
    }
    alert(`API 연결을 확인했습니다. 사용 모델: ${res.settings?.model || '자동 선택'}`);
    await loadAiSettings();
  } catch (error) {
    if (status) status.innerText = 'API 키 확인 중 연결 오류가 발생했습니다.';
    alert('OpenAI 서버에 연결하지 못했습니다. 인터넷 연결을 확인하고 다시 시도하세요.');
  } finally {
    if (button) {
      button.disabled = false;
      button.innerText = 'API 키 확인 후 저장';
    }
  }
}

function renderUpdateHistory(updates = []) {
  if (!updates.length) return '<p class="muted">아직 저장 이력이 없습니다.</p>';
  const latest = updates[0];
  const updateItem = u => `<div class="update-item"><b>${esc(u.created_at || '')}</b><p>${esc(u.summary || '저장된 진행 내용이 있습니다.')}</p><small>${esc(u.changed_text || '')}</small></div>`;
  if (updates.length === 1) return `<div class="update-list">${updateItem(latest)}</div>`;
  const olderItems = updates.slice(1).map(updateItem).join('');
  return `<details class="update-history">
    <summary>
      <span>저장 이력 ${updates.length}개 전체 보기</span>
      <span class="history-arrow">▾</span>
      <div class="update-list latest-update">${updateItem(latest)}</div>
    </summary>
    <div class="update-list all-updates">${olderItems}</div>
  </details>`;
}

function renderDashboardFeedbackHistory(feedbacks = []) {
  if (!feedbacks.length) return '<p class="muted">아직 저장된 피드백이 없습니다.</p>';
  return `<div class="teacher-feedback-history">${feedbacks.slice(0, 3).map(f => `<div class="teacher-feedback-item"><b>${esc(f.created_at || '')}</b><p>${esc(f.teacher_comment || '')}</p></div>`).join('')}</div>`;
}

async function loadDashboard() {
  const res = await (await fetch('/api/teacher/dashboard')).json();
  lastDashboard = res.items || [];
  document.getElementById('dashboard').innerHTML = `<table class="table"><tr><th>학생</th><th>주제</th><th>진행 상황</th><th>적합도</th><th>진행률</th><th class="no-print">교사 피드백</th></tr>${lastDashboard.map(x => `<tr><td><b>${esc(x.name)}</b><br><span class="muted">${esc(x.student_no)}</span></td><td>${esc(x.topic)}</td><td><strong>${esc(x.progress_note || '아직 입력된 진행 상황이 없습니다.')}</strong><p class="muted">최근 저장: ${esc(x.updated_at || '-')}</p>${renderUpdateHistory(x.updates || [])}</td><td>${x.fit_score}점</td><td>${x.progress}%<div class="bar"><span style="width:${clamp(x.progress)}%"></span></div></td><td class="no-print"><label class="field-label" for="c${x.id}">교사 피드백</label><textarea class="teacher-comment" id="c${x.id}" placeholder="학생에게 보여줄 피드백을 적어주세요."></textarea><button class="btn secondary" onclick="saveFeedback(${x.id})">피드백 저장</button>${renderDashboardFeedbackHistory(x.feedbacks || [])}</td></tr>`).join('')}</table>`;
}

function saveDashboardPdf() {
  window.print();
}

async function resetStudentData() {
  if (!teacherPassword) return alert('교사 로그인 후 사용할 수 있습니다.');
  const ok = confirm('모든 학생, 탐구, 피드백 자료를 삭제합니다. 계속할까요?');
  if (!ok) return;
  const res = await post('/api/teacher/reset', { password: teacherPassword });
  if (!res.ok) return alert('초기화에 실패했습니다.');
  alert('학생 자료가 초기화되었습니다.');
  await loadDashboard();
}

async function saveFeedback(id) {
  const payload = { teacher_comment: valueOf(`c${id}`).trim() };
  if (!payload.teacher_comment) return alert('교사 피드백을 입력하세요.');
  await post(`/api/projects/${id}/feedback`, payload);
  alert('교사 피드백이 저장되었습니다.');
  await loadDashboard();
}
