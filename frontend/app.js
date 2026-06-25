let currentStudent = null;
let selectedTag = '';
let currentProjectId = null;
let currentProgressNote = '';
let currentWizardStep = 0;
let lastDashboard = [];
let teacherPassword = '';

const TAGS = ['게임','스포츠','음악','K-POP','유튜브','웹툰','영화','음식','동물','환경','패션','친구관계','스마트폰','진로','과학','로봇','AI','건강','여행','학교생활'];
const WIZARD_PAGES = ['wizardPlan', 'wizardGuide', 'wizardSurvey', 'wizardInterview', 'wizardLog', 'wizardReport'];
const WIZARD_PROGRESS = [30, 45, 60, 70, 80, 90];

window.onload = () => {
  const tagBox = document.getElementById('tags');
  if (tagBox) {
    tagBox.innerHTML = TAGS.map(t => `<span class="tag" onclick="selectTag(this,'${t}')">${t}</span>`).join('');
  }
  initWizardPage();
  initInternetStatus();
};

function selectTag(el, tag) {
  document.querySelectorAll('.tag').forEach(x => x.classList.remove('active'));
  el.classList.add('active');
  selectedTag = tag;
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
  if (!navigator.onLine) {
    setInternetStatus(false);
    return;
  }
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

async function login() {
  const name = document.getElementById('name').value.trim();
  const student_no = document.getElementById('studentNo').value.trim();
  if (!name || !student_no) return alert('이름과 학번을 입력하세요.');
  currentStudent = await post('/api/student/login', { name, student_no });
  document.getElementById('loginBox').classList.add('hidden');
  document.getElementById('interestBox').classList.remove('hidden');
  await loadMyProjects();
}

async function loadMyProjects() {
  const res = await (await fetch(`/api/student/${currentStudent.id}/projects`)).json();
  if (!res.items.length) return;
  document.getElementById('myProjectsBox').classList.remove('hidden');
  document.getElementById('myProjects').innerHTML = res.items.map(p => `
    <div class="topic">
      <h3>${esc(p.topic)}</h3>
      <p class="muted">진행률 ${p.progress}% · 적합도 ${p.fit_score}점</p>
      <div class="bar"><span style="width:${clamp(p.progress)}%"></span></div>
      <label class="field-label" for="note${p.id}">진행 상황</label>
      <textarea class="progress-note" id="note${p.id}" placeholder="오늘 진행한 내용, 어려운 점, 다음 계획을 적어보세요.">${esc(p.progress_note || '')}</textarea>
      <div class="row">
        <button class="btn secondary" onclick="openProject(${p.id})">이어하기</button>
        <button class="btn" onclick="saveProgressNote(${p.id})">진행 상황 저장</button>
      </div>
    </div>`).join('');
}

async function saveProgressNote(projectId) {
  const note = document.getElementById(`note${projectId}`).value;
  const res = await fetch(`/api/projects/${projectId}/progress-note`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ progress_note: note }),
  });
  if (!res.ok) return alert('진행 상황 저장에 실패했습니다.');
  alert('진행 상황이 저장되었습니다.');
}

function openProject(id) {
  window.location.href = `wizard.html?project_id=${id}`;
}

async function recommend() {
  if (!selectedTag) return alert('태그를 선택하세요.');
  const detail = document.getElementById('detail').value;
  const res = await post('/api/recommend', { tag: selectedTag, detail });
  const items = (res.items || []).sort((a, b) => (b.fit?.total || 0) - (a.fit?.total || 0));
  document.getElementById('recommendBox').classList.remove('hidden');
  document.getElementById('modeText').innerText = res.mode === 'online' ? '온라인 AI 추천 결과입니다.' : '오프라인 추천 엔진 결과입니다.';
  document.getElementById('topics').innerHTML = items.map(it => {
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
}

async function startProject(item) {
  const fit = item.fit || {};
  const res = await post('/api/projects', {
    student_id: currentStudent.id,
    tag: selectedTag,
    interest: document.getElementById('detail').value,
    topic: item.topic,
    subject: item.subject || '',
    fit_score: fit.total || 70,
  });
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
  document.getElementById('reportOutput').innerHTML = p.report ? `<pre>${esc(p.report)}</pre>` : '';
  const progress = Number(p.progress || 30);
  const step = progress >= 90 ? 5 : progress >= 80 ? 4 : progress >= 70 ? 3 : progress >= 60 ? 2 : progress >= 45 ? 1 : 0;
  setWizardStep(step, progress);
}

function setWizardStep(step, progressOverride = null) {
  currentWizardStep = Math.max(0, Math.min(WIZARD_PAGES.length - 1, step));
  WIZARD_PAGES.forEach((id, index) => {
    const page = document.getElementById(id);
    if (page) page.classList.toggle('hidden', index !== currentWizardStep);
  });
  document.querySelectorAll('#wizardStepper span').forEach((item, index) => {
    item.classList.toggle('active', index === currentWizardStep);
    item.classList.toggle('done', index < currentWizardStep);
  });
  const prev = document.getElementById('prevWizardBtn');
  const next = document.getElementById('nextWizardBtn');
  if (prev) prev.disabled = currentWizardStep === 0;
  if (next) next.innerText = currentWizardStep === WIZARD_PAGES.length - 1 ? '완료' : '다음';
  updateProgress(progressOverride ?? WIZARD_PROGRESS[currentWizardStep]);
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

async function nextWizardStep() {
  await saveProject(WIZARD_PROGRESS[currentWizardStep], false);
  if (currentWizardStep < WIZARD_PAGES.length - 1) {
    setWizardStep(currentWizardStep + 1);
  } else {
    alert('탐구 마법사를 완료했습니다. 보고서 초안을 확인하고 필요한 내용을 수정해 주세요.');
  }
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
  if ((document.getElementById('reportOutput')?.innerText || '').trim().length > 20) progress = Math.max(progress, 90);
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
  if (!currentProjectId) return;
  await fetch(`/api/projects/${currentProjectId}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      plan: valueOf('plan'),
      plan_note: valueOf('planNote'),
      guide_note: valueOf('guideNote'),
      survey_note: valueOf('surveyNote'),
      interview_note: valueOf('interviewNote'),
      research_log: valueOf('log'),
      progress_note: currentProgressNote,
      report: document.getElementById('reportOutput').innerText,
      progress,
    }),
  });
  updateProgress(progress);
  if (showAlert) alert('저장되었습니다.');
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

async function teacherLogin() {
  const password = document.getElementById('teacherPw').value;
  const res = await post('/api/teacher/login', { password });
  if (!res.ok) return alert('비밀번호가 올바르지 않습니다.');
  teacherPassword = password;
  document.getElementById('teacherLogin').classList.add('hidden');
  document.getElementById('dash').classList.remove('hidden');
  await loadDashboard();
}

async function loadDashboard() {
  const res = await (await fetch('/api/teacher/dashboard')).json();
  lastDashboard = res.items || [];
  document.getElementById('dashboard').innerHTML = `<table class="table"><tr><th>학생</th><th>주제</th><th>진행 상황</th><th>적합도</th><th>진행률</th><th class="no-print">피드백</th></tr>${lastDashboard.map(x => `<tr><td><b>${esc(x.name)}</b><br><span class="muted">${esc(x.student_no)}</span></td><td>${esc(x.topic)}<br><span class="pill">${esc(x.subject || '')}</span></td><td>${esc(x.progress_note || '아직 입력된 진행 상황이 없습니다.')}</td><td>${x.fit_score}점</td><td>${x.progress}%<div class="bar"><span style="width:${clamp(x.progress)}%"></span></div></td><td class="no-print"><input class="input" id="c${x.id}" placeholder="교사 피드백"><br><br><button class="btn secondary" onclick="saveFeedback(${x.id})">저장</button><p class="muted">${esc(x.teacher_comment || '')}</p></td></tr>`).join('')}</table>`;
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
  await post(`/api/projects/${id}/feedback`, { teacher_comment: document.getElementById(`c${id}`).value });
  alert('피드백이 저장되었습니다.');
  await loadDashboard();
}
