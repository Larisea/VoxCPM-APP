// ============================================================
// i18n 国际化
// ============================================================
const I18N = {
  en: {
    'tab.tts': 'Synthesis',
    'tab.voicebank': 'Voice Bank',
    'tab.capture': 'Capture',
    'tab.revoice': 'Revoice',
    'tts.title': 'Text-to-Speech Engine',
    'tts.voiceProfile': 'Voice Profile',
    'tts.defaultVoice': '— Default Voice —',
    'tts.refTranscript': 'Reference Transcript',
    'tts.refTranscriptPH': 'Enter the text spoken in the reference audio...',
    'tts.inputText': 'Input Text',
    'tts.inputTextPH': 'Enter text to synthesize...',
    'tts.cfgScale': 'CFG Scale',
    'tts.inferSteps': 'Inference Steps',
    'tts.generate': '▸ Generate',
    'tts.clear': 'Clear',
    'tts.recentOutput': 'Recent Output',
    'vb.uploadRef': 'Upload Reference',
    'vb.dropText': 'Drop audio files or click to upload',
    'vb.dropHint': 'WAV / MP3 / FLAC — 15-30s recommended',
    'vb.library': 'Voice Library',
    'rec.title': 'Audio Capture',
    'rec.script': 'Script (read aloud while recording)',
    'rec.hint': 'Press to record — aim for 10-30 seconds',
    'rec.hintDone': 'Recording complete — preview or save',
    'rec.recording': 'Recording... press to stop',
    'rec.save': '▸ Save to Voice Bank',
    'cover.title': 'Revoice Studio',
    'cover.desc': 'Train a voice model via RVC, then replace vocals in any song with your own voice.',
    'cover.phase1num': 'Phase 01 — Acquire',
    'cover.phase1desc': 'Record 3-10 minutes of clean dry vocals. Multiple short clips work well.',
    'cover.startRec': 'Start Recording →',
    'cover.phase2num': 'Phase 02 — Install',
    'cover.phase2desc': 'Deploy RVC WebUI for voice model training pipeline.',
    'cover.installRVC': 'Install RVC',
    'cover.phase3num': 'Phase 03 — Train',
    'cover.phase3desc': 'Upload audio in RVC → Train → Export model (.pth).',
    'cover.phase3note': '~10-30 MIN DEPENDING ON GPU',
    'cover.phase4num': 'Phase 04 — Revoice',
    'cover.phase4desc': 'Upload song → select your model → generate cover.',
    'cover.tryClone': 'Try VoxCPM Clone →',
    'cover.quickTitle': 'Quick Revoice (VoxCPM Sim)',
    'cover.quickDesc': 'No RVC needed — VoxCPM reads lyrics in your cloned voice directly.',
    'cover.voiceProfile': 'Voice Profile',
    'cover.refTranscript': 'Reference Transcript',
    'cover.refTranscriptPH': 'Enter the text spoken in the reference audio...',
    'cover.lyrics': 'Lyrics (one line per segment)',
    'cover.generate': '▸ Generate Cover',
    'cover.clear': 'Clear',
    'cover.installLog': 'Installation Log',
    'cover.awaitInit': 'Awaiting initialization...',
    // Dynamic toasts / statuses
    'status.online': 'ONLINE',
    'status.offline': 'OFFLINE',
    'status.loading': 'LOADING MODEL...',
    'status.noConn': 'NO CONNECTION',
    'status.initFail': 'INIT FAILED — REFRESH',
    'toast.modelLoaded': 'Model loaded',
    'toast.loadFail': 'Load failed',
    'toast.connFail': 'Connection failed',
    'toast.enterText': 'Enter text to synthesize',
    'toast.textLong': 'Text too long — max 500 chars',
    'toast.refNeeded': 'Reference transcript required when using voice profile',
    'toast.synthesizing': 'Synthesizing...',
    'toast.submitFail': 'Submit failed',
    'toast.requestFail': 'Request failed',
    'toast.genFail': 'Generation failed',
    'toast.timeout': 'Task timed out',
    'toast.uploaded': 'Uploaded',
    'toast.uploadFail': 'Upload failed',
    'toast.deleted': 'Deleted',
    'toast.delFail': 'Delete failed',
    'toast.recNoData': 'No recording to save',
    'toast.saved': 'Saved to voice bank',
    'toast.saveFail': 'Save failed',
    'toast.micFail': 'Microphone access denied',
    'toast.wavFail': 'Audio conversion failed, retry',
    'toast.enterLyrics': 'Enter lyrics',
    'toast.lyricsEmpty': 'Lyrics cannot be empty',
    'toast.lineLong': 'Single line exceeds 500 chars — split it',
    'toast.lineFailed': 'Line failed',
    'toast.lineReqFail': 'Line request failed',
    'toast.merging': 'Merging audio...',
    'toast.coverComplete': '▸ COVER COMPLETE',
    'toast.genFailCover': 'Generation failed',
    'toast.refNeededCover': 'Reference transcript required when using voice profile',
    'toast.defaultVoice': '— Default Voice —',
    'toast.emptyLib': 'Empty library',
    'toast.noOutput': 'No output yet',
    'toast.deletedBtn': 'DEL',
    'toast.dlBtn': 'DL',
    'toast.synthComplete': '▸ SYNTHESIS COMPLETE',
    'toast.download': 'Download',
    'toast.uploading': 'UPLOADING',
  },
  zh: {
    'tab.tts': '语音合成',
    'tab.voicebank': '声音库',
    'tab.capture': '录制',
    'tab.revoice': '翻唱',
    'tts.title': '文本转语音引擎',
    'tts.voiceProfile': '声音档案',
    'tts.defaultVoice': '— 默认声音 —',
    'tts.refTranscript': '参考音频文本',
    'tts.refTranscriptPH': '输入参考音频中朗读的文本内容...',
    'tts.inputText': '输入文本',
    'tts.inputTextPH': '输入要合成的文本...',
    'tts.cfgScale': '引导强度 (CFG)',
    'tts.inferSteps': '推理步数',
    'tts.generate': '▸ 生成语音',
    'tts.clear': '清空',
    'tts.recentOutput': '最近生成',
    'vb.uploadRef': '上传参考音频',
    'vb.dropText': '拖拽音频文件或点击上传',
    'vb.dropHint': 'WAV / MP3 / FLAC — 建议 15-30 秒',
    'vb.library': '声音库',
    'rec.title': '录制声音',
    'rec.script': '朗读文本（录制时对着麦克风朗读）',
    'rec.hint': '点击开始录制，建议录制 10-30 秒',
    'rec.hintDone': '录制完成，可以预览或保存',
    'rec.recording': '录制中... 点击停止',
    'rec.save': '▸ 保存到声音库',
    'cover.title': '翻唱工作室',
    'cover.desc': '先通过 RVC 训练声音模型，然后将歌曲中的人声替换为你的声音。',
    'cover.phase1num': '阶段 01 — 采集',
    'cover.phase1desc': '录制 3-10 分钟清晰干声（无背景噪音），多个短音频也可。',
    'cover.startRec': '开始录制 →',
    'cover.phase2num': '阶段 02 — 安装',
    'cover.phase2desc': '部署 RVC WebUI 声音模型训练环境。',
    'cover.installRVC': '安装 RVC',
    'cover.phase3num': '阶段 03 — 训练',
    'cover.phase3desc': '在 RVC 中上传音频 → 一键训练 → 导出模型 (.pth)。',
    'cover.phase3note': '约 10-30 分钟（取决于 GPU）',
    'cover.phase4num': '阶段 04 — 翻唱',
    'cover.phase4desc': '上传歌曲 → 选择你的模型 → 生成翻唱版本。',
    'cover.tryClone': '先用 VoxCPM 体验克隆 →',
    'cover.quickTitle': '简易翻唱（VoxCPM 模拟）',
    'cover.quickDesc': '无需安装 RVC，直接用 VoxCPM 将歌词转为你的声音朗读。',
    'cover.voiceProfile': '声音档案',
    'cover.refTranscript': '参考音频文本',
    'cover.refTranscriptPH': '输入参考音频中朗读的文本内容...',
    'cover.lyrics': '歌词文本（每行一句）',
    'cover.generate': '▸ 生成翻唱',
    'cover.clear': '清空',
    'cover.installLog': '安装日志',
    'cover.awaitInit': '等待初始化...',
    // Dynamic
    'status.online': '在线',
    'status.offline': '离线',
    'status.loading': '加载模型中...',
    'status.noConn': '无连接',
    'status.initFail': '初始化失败 — 请刷新',
    'toast.modelLoaded': '模型加载成功',
    'toast.loadFail': '加载失败',
    'toast.connFail': '连接失败',
    'toast.enterText': '请输入要合成的文本',
    'toast.textLong': '文本过长，最多 500 字',
    'toast.refNeeded': '使用声音档案时需要填写参考音频文本',
    'toast.synthesizing': '正在合成...',
    'toast.submitFail': '提交失败',
    'toast.requestFail': '请求失败',
    'toast.genFail': '生成失败',
    'toast.timeout': '任务超时',
    'toast.uploaded': '已上传',
    'toast.uploadFail': '上传失败',
    'toast.deleted': '已删除',
    'toast.delFail': '删除失败',
    'toast.recNoData': '没有可保存的录音',
    'toast.saved': '已保存到声音库',
    'toast.saveFail': '保存失败',
    'toast.micFail': '无法访问麦克风',
    'toast.wavFail': '音频转换失败，请重试',
    'toast.enterLyrics': '请输入歌词',
    'toast.lyricsEmpty': '歌词不能为空',
    'toast.lineLong': '单行超过 500 字，请拆分',
    'toast.lineFailed': '第 N 句失败',
    'toast.lineReqFail': '第 N 句请求失败',
    'toast.merging': '正在合并音频...',
    'toast.coverComplete': '▸ 翻唱完成',
    'toast.genFailCover': '生成失败',
    'toast.refNeededCover': '使用声音档案时需要填写参考音频文本',
    'toast.defaultVoice': '— 默认声音 —',
    'toast.emptyLib': '还没有上传声音',
    'toast.noOutput': '还没有生成过语音',
    'toast.deletedBtn': '删除',
    'toast.dlBtn': '下载',
    'toast.synthComplete': '▸ 合成完成',
    'toast.download': '下载',
    'toast.uploading': '上传中',
  }
};

let currentLang = localStorage.getItem('voxcpm-lang') || 'en';

function t(key) {
  return (I18N[currentLang] && I18N[currentLang][key]) || (I18N.en[key]) || key;
}

function setLang(lang) {
  currentLang = lang;
  localStorage.setItem('voxcpm-lang', lang);

  document.getElementById('langEn').classList.toggle('active', lang === 'en');
  document.getElementById('langZh').classList.toggle('active', lang === 'zh');
  document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';

  // Update static text elements
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    const text = t(key);
    if (text) el.textContent = text;
  });

  // Update placeholders
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const key = el.getAttribute('data-i18n-placeholder');
    const text = t(key);
    if (text) el.placeholder = text;
  });

  // Re-render dynamic lists with new language
  loadReferences();
  loadHistory();
  if (currentTab === 'cover') loadCoverReferences();
  updateCharCount();
}

// ============================================================
// 全局状态
// ============================================================
let currentTab = 'tts';
let mediaRecorder = null;
let audioChunks = [];
let recStartTime = 0;
let recTimerInterval = null;
let recordedBlob = null;
let modelReady = false;

// ── SVG Icons for audio list items ──
const ICON_MIC = '<svg class="audio-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/></svg>';
const ICON_WAVE = '<svg class="audio-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h2l3-9 4 18 4-18 3 9h2"/></svg>';
const ICON_MUSIC = '<svg class="audio-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>';

// ============================================================
// 入场动画
// ============================================================
function animateEntrance() {
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, i) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(16px)';
        card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 80 + i * 80);
    });
}

// ============================================================
// 初始化
// ============================================================
async function init() {
    try {
        setLang(currentLang);
        await checkStatus();
        await loadReferences();
        await loadHistory();
        updateCharCount();
        animateEntrance();

        const dropZone = document.getElementById('dropZone');
        if (dropZone) {
            dropZone.addEventListener('dragover', e => { e.preventDefault(); dropZone.classList.add('drag-over'); });
            dropZone.addEventListener('dragleave', () => dropZone.classList.remove('drag-over'));
            dropZone.addEventListener('drop', e => {
                e.preventDefault();
                dropZone.classList.remove('drag-over');
                handleFiles(e.dataTransfer.files);
            });
        }

        const ttsText = document.getElementById('ttsText');
        if (ttsText) {
            ttsText.addEventListener('input', updateCharCount);
        }
    } catch(e) {
        console.error('init error:', e);
        document.getElementById('statusText').textContent = t('status.initFail');
    }
}

async function checkStatus() {
    try {
        const res = await fetch('/api/status');
        const data = await res.json();
        modelReady = data.ready;
        const dot = document.getElementById('statusDot');
        const txt = document.getElementById('statusText');
        if (data.ready) {
            dot.className = 'status-dot online';
            txt.textContent = t('status.online');
        } else {
            dot.className = 'status-dot offline';
            txt.textContent = t('status.offline');
            loadModel();
        }
    } catch(e) {
        document.getElementById('statusText').textContent = t('status.noConn');
    }
}

async function loadModel() {
    try {
        document.getElementById('statusText').textContent = t('status.loading');
        const res = await fetch('/api/load_model', { method: 'POST' });
        const data = await res.json();
        if (data.success) {
            modelReady = true;
            document.getElementById('statusDot').className = 'status-dot online';
            document.getElementById('statusText').textContent = t('status.online');
            toast(t('toast.modelLoaded'), 'success');
        } else {
            toast(t('toast.loadFail') + ': ' + data.error, 'error');
        }
    } catch(e) {
        toast(t('toast.connFail'), 'error');
    }
}

// ============================================================
// 标签切换
// ============================================================
function switchTab(tab) {
    currentTab = tab;
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.style.display = 'none');

    const tabMap = { 'tts': 0, 'reference': 1, 'record': 2, 'cover': 3 };
    document.querySelectorAll('.tab')[tabMap[tab]].classList.add('active');
    document.getElementById('tab-' + tab).style.display = 'block';

    if (tab === 'reference') loadReferences();
    if (tab === 'tts') loadReferences(true);
    if (tab === 'cover') loadCoverReferences();
}

// ============================================================
// Toast
// ============================================================
function toast(msg, type = 'info') {
    const el = document.createElement('div');
    el.className = 'toast ' + type;
    el.textContent = msg;
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 3000);
}

// ============================================================
// 字数统计 (#6)
// ============================================================
function updateCharCount() {
    const text = document.getElementById('ttsText').value;
    const counter = document.getElementById('charCount');
    if (!counter) return;
    const len = text.length;
    const max = 500;
    counter.textContent = `${len} / ${max}`;
    counter.className = len > max ? 'char-count over' : (len > max * 0.8 ? 'char-count warn' : 'char-count');
}

// ============================================================
// 参考音频管理
// ============================================================
async function loadReferences(forSelect = false) {
    try {
        const res = await fetch('/api/reference_audios');
        const data = await res.json();

        if (forSelect || currentTab === 'tts') {
            const select = document.getElementById('promptWav');
            select.innerHTML = `<option value="">${t('toast.defaultVoice')}</option>`;
            data.files.forEach(f => {
                select.innerHTML += `<option value="${f.path}">${f.name} (${f.size_kb}KB)</option>`;
            });
        }

        const list = document.getElementById('refList');
        if (data.files.length === 0) {
            list.innerHTML = `<div class="empty"><div class="icon">◇</div><p>${t('toast.emptyLib')}</p></div>`;
        } else {
            list.innerHTML = data.files.map(f => `
                <div class="audio-item">
                    ${ICON_MIC}
                    <span class="name" title="${f.name}">${f.name}</span>
                    <span class="meta">${f.size_kb} KB</span>
                    <audio controls src="/${f.path}"></audio>
                    <button class="btn btn-danger btn-sm" onclick="deleteRef('${f.name}')" style="margin-left:8px;">${t('toast.deletedBtn')}</button>
                </div>
            `).join('');
        }
    } catch(e) {
        console.error('加载参考音频失败', e);
    }
}

async function deleteRef(filename) {
    if (!confirm(`Delete ${filename} ?`)) return;
    try {
        await fetch('/api/reference/' + filename, { method: 'DELETE' });
        loadReferences();
        toast(t('toast.deleted'), 'info');
    } catch(e) {
        toast(t('toast.delFail'), 'error');
    }
}

function onPromptChange() {
    const val = document.getElementById('promptWav').value;
    document.getElementById('promptTextGroup').style.display = val ? 'block' : 'none';
}

// ============================================================
// 文件上传 + 进度条 (#9)
// ============================================================
async function uploadFile(event) {
    handleFiles(event.target.files);
    event.target.value = '';
}

function handleFiles(files) {
    const statusEl = document.getElementById('uploadStatus');
    Array.from(files).forEach(file => {
        const formData = new FormData();
        formData.append('file', file);

        const progressHTML = `
            <div class="upload-progress" id="upload-${file.name}">
                <span style="color:var(--text-secondary); font-size:12px;">${t('toast.uploading')}: ${file.name}</span>
                <div class="progress-track" style="margin-top:4px;">
                    <div class="progress-fill upload-fill" style="width:0%"></div>
                </div>
            </div>`;
        statusEl.insertAdjacentHTML('beforeend', progressHTML);

        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/api/upload_reference');
        xhr.upload.onprogress = (e) => {
            if (e.lengthComputable) {
                const pct = Math.round((e.loaded / e.total) * 100);
                const fill = document.querySelector(`#upload-${CSS.escape(file.name)} .upload-fill`);
                if (fill) fill.style.width = pct + '%';
            }
        };
        xhr.onload = () => {
            const el = document.getElementById('upload-' + file.name);
            if (el) el.remove();
            try {
                const data = JSON.parse(xhr.responseText);
                if (data.success) {
                    toast(`${t('toast.uploaded')}: ${data.filename}`, 'success');
                } else {
                    toast(`${t('toast.uploadFail')}: ${data.error}`, 'error');
                }
            } catch(e) {
                toast(t('toast.uploadFail'), 'error');
            }
            loadReferences();
        };
        xhr.onerror = () => {
            const el = document.getElementById('upload-' + file.name);
            if (el) el.remove();
            toast(t('toast.uploadFail'), 'error');
        };
        xhr.send(formData);
    });
}

// ============================================================
// 录制
// ============================================================
async function toggleRecord() {
    if (mediaRecorder && mediaRecorder.state === 'recording') {
        stopRecord();
        return;
    }
    startRecord();
}

async function startRecord() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        const mimeType = MediaRecorder.isTypeSupported('audio/webm;codecs=opus')
            ? 'audio/webm;codecs=opus' : 'audio/webm';
        mediaRecorder = new MediaRecorder(stream, { mimeType: mimeType });
        audioChunks = [];

        mediaRecorder.ondataavailable = e => {
            if (e.data.size > 0) audioChunks.push(e.data);
        };

        mediaRecorder.onstop = async () => {
            stream.getTracks().forEach(t => t.stop());
            const webmBlob = new Blob(audioChunks, { type: 'audio/webm' });

            const previewUrl = URL.createObjectURL(webmBlob);
            const preview = document.getElementById('recPreview');
            preview.src = previewUrl;
            preview.style.display = 'block';

            try {
                recordedBlob = await webmToWav(webmBlob);
                document.getElementById('btnSaveRec').style.display = 'inline-flex';
            } catch(e) {
                console.error('WAV 转换失败:', e);
                toast(t('toast.wavFail'), 'error');
            }
        };

        mediaRecorder.start();
        recStartTime = Date.now();
        document.getElementById('recBtn').classList.add('recording');
        document.getElementById('recHint').textContent = t('rec.recording');
        document.getElementById('btnSaveRec').style.display = 'none';
        document.getElementById('recPreview').style.display = 'none';

        recTimerInterval = setInterval(updateRecTimer, 200);
    } catch(e) {
        toast(t('toast.micFail') + ': ' + e.message, 'error');
    }
}

async function webmToWav(webmBlob) {
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    const arrayBuffer = await webmBlob.arrayBuffer();
    const audioBuffer = await audioCtx.decodeAudioData(arrayBuffer);

    const sampleRate = audioBuffer.sampleRate;
    const length = audioBuffer.length;
    const pcmData = audioBuffer.getChannelData(0);

    const buffer = new ArrayBuffer(44 + length * 2);
    const view = new DataView(buffer);

    writeString(view, 0, 'RIFF');
    view.setUint32(4, 36 + length * 2, true);
    writeString(view, 8, 'WAVE');
    writeString(view, 12, 'fmt ');
    view.setUint32(16, 16, true);
    view.setUint16(20, 1, true);
    view.setUint16(22, 1, true);
    view.setUint32(24, sampleRate, true);
    view.setUint32(28, sampleRate * 2, true);
    view.setUint16(32, 2, true);
    view.setUint16(34, 16, true);
    writeString(view, 36, 'data');
    view.setUint32(40, length * 2, true);

    let offset = 44;
    for (let i = 0; i < length; i++) {
        const sample = Math.max(-1, Math.min(1, pcmData[i]));
        const intSample = sample < 0 ? sample * 0x8000 : sample * 0x7FFF;
        view.setInt16(offset, intSample, true);
        offset += 2;
    }

    audioCtx.close();
    return new Blob([buffer], { type: 'audio/wav' });
}

function stopRecord() {
    if (mediaRecorder) {
        mediaRecorder.stop();
        document.getElementById('recBtn').classList.remove('recording');
        document.getElementById('recHint').textContent = t('rec.hintDone');
        clearInterval(recTimerInterval);
    }
}

function updateRecTimer() {
    const elapsed = Math.floor((Date.now() - recStartTime) / 1000);
    const min = String(Math.floor(elapsed / 60)).padStart(2, '0');
    const sec = String(elapsed % 60).padStart(2, '0');
    document.getElementById('recTimer').textContent = `${min}:${sec}`;
}

async function saveRecording() {
    if (!recordedBlob) {
        toast(t('toast.recNoData'), 'error');
        return;
    }
    const formData = new FormData();
    formData.append('file', recordedBlob, `recording_${Date.now()}.wav`);

    try {
        const res = await fetch('/api/upload_reference', { method: 'POST', body: formData });
        const data = await res.json();
        if (data.success) {
            toast(t('toast.saved'), 'success');
            document.getElementById('btnSaveRec').style.display = 'none';
            document.getElementById('recPreview').style.display = 'none';
            recordedBlob = null;
            loadReferences();
        } else {
            toast(t('toast.saveFail') + ': ' + (data.error || 'unknown error'), 'error');
        }
    } catch(e) {
        toast(t('toast.saveFail'), 'error');
    }
}

// ============================================================
// TTS
// ============================================================
async function doTTS() {
    if (!modelReady) {
        toast(t('toast.connFail'), 'error');
        await loadModel();
        if (!modelReady) return;
    }

    const text = document.getElementById('ttsText').value.trim();
    if (!text) {
        toast(t('toast.enterText'), 'error');
        return;
    }

    if (text.length > 500) {
        toast(t('toast.textLong'), 'error');
        return;
    }

    const promptWav = document.getElementById('promptWav').value;
    const promptText = document.getElementById('promptText').value.trim();

    if (promptWav && !promptText) {
        toast(t('toast.refNeeded'), 'error');
        return;
    }

    document.getElementById('btnGenerate').disabled = true;
    document.getElementById('ttsProgress').style.display = 'block';
    document.getElementById('ttsResult').innerHTML = '';
    document.getElementById('ttsMsg').textContent = t('toast.synthesizing');
    document.getElementById('ttsPercent').textContent = '0%';
    document.getElementById('ttsFill').style.width = '0%';

    const formData = new FormData();
    formData.append('text', text);
    formData.append('prompt_wav', promptWav);
    formData.append('prompt_text', promptText);
    formData.append('cfg', document.getElementById('cfg').value);
    formData.append('steps', document.getElementById('steps').value);

    try {
        const res = await fetch('/api/tts', { method: 'POST', body: formData });
        const data = await res.json();
        if (data.success) {
            pollTask(data.task_id);
        } else {
            toast(t('toast.submitFail') + ': ' + data.error, 'error');
            resetTTSBtn();
        }
    } catch(e) {
                toast(t('toast.requestFail'), 'error');
        resetTTSBtn();
    }
}

async function pollTask(taskId) {
    const maxPolls = 120;
    let polls = 0;

    const interval = setInterval(async () => {
        try {
            const res = await fetch('/api/task/' + taskId);
            const data = await res.json();
            const task = data.task;

            document.getElementById('ttsMsg').textContent = task.message;
            document.getElementById('ttsPercent').textContent = task.progress + '%';
            document.getElementById('ttsFill').style.width = task.progress + '%';

            if (task.status === 'done') {
                clearInterval(interval);
                document.getElementById('ttsProgress').style.display = 'none';
                document.getElementById('btnGenerate').disabled = false;

                const result = task.result;
                document.getElementById('ttsResult').innerHTML = `
                    <div class="result-card">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span style="color:var(--green); font-weight:600; font-size:13px;">${t('toast.synthComplete')}</span>
                            <div style="display:flex; align-items:center; gap:12px;">
                                <span class="range-label">${result.duration}s / ${result.sample_rate}Hz</span>
                                <a class="btn btn-outline btn-sm" href="/api/download/${result.filename}" download="${result.filename}">${t('toast.download')}</a>
                            </div>
                        </div>
                        <audio controls src="data:audio/wav;base64,${result.audio_base64}"></audio>
                    </div>
                `;
                loadHistory();

            } else if (task.status === 'error') {
                clearInterval(interval);
                toast(t('toast.genFail') + ': ' + task.message, 'error');
                resetTTSBtn();
            }

            polls++;
            if (polls >= maxPolls) {
                clearInterval(interval);
                toast(t('toast.timeout'), 'error');
                resetTTSBtn();
            }
        } catch(e) {
            clearInterval(interval);
            resetTTSBtn();
        }
    }, 1000);
}

function resetTTSBtn() {
    document.getElementById('btnGenerate').disabled = false;
    document.getElementById('ttsProgress').style.display = 'none';
}

// ============================================================
// 历史记录 (#4 下载按钮, #10 删除按钮)
// ============================================================
async function loadHistory() {
    try {
        const res = await fetch('/api/history');
        const data = await res.json();
        const list = document.getElementById('historyList');
        if (data.files.length === 0) {
            list.innerHTML = `<div class="empty"><div class="icon">◇</div><p>${t('toast.noOutput')}</p></div>`;
        } else {
            list.innerHTML = data.files.map(f => `
                <div class="audio-item">
                    ${ICON_WAVE}
                    <span class="name" title="${f.name}">${f.name}</span>
                    <span class="meta">${f.time} / ${f.size_kb}KB</span>
                    <audio controls src="/${f.path}"></audio>
                    <a class="btn btn-outline btn-sm" href="/api/download/${f.name}" download="${f.name}" style="margin-left:4px;">${t('toast.dlBtn')}</a>
                    <button class="btn btn-danger btn-sm" onclick="deleteHistory('${f.name}')" style="margin-left:4px;">${t('toast.deletedBtn')}</button>
                </div>
            `).join('');
        }
    } catch(e) {
        console.error('加载历史失败', e);
    }
}

async function deleteHistory(filename) {
    if (!confirm(`Delete ${filename} ?`)) return;
    try {
        await fetch('/api/history/' + filename, { method: 'DELETE' });
        loadHistory();
        toast(t('toast.deleted'), 'info');
    } catch(e) {
        toast(t('toast.delFail'), 'error');
    }
}

// ============================================================
// 翻唱功能
// ============================================================
function onCoverPromptChange() {
    const val = document.getElementById('coverPromptWav').value;
    document.getElementById('coverPromptTextGroup').style.display = val ? 'block' : 'none';
}

async function loadCoverReferences() {
    try {
        const res = await fetch('/api/reference_audios');
        const data = await res.json();
        const select = document.getElementById('coverPromptWav');
        select.innerHTML = `<option value="">${t('toast.defaultVoice')}</option>`;
        data.files.forEach(f => {
            select.innerHTML += `<option value="${f.path}">${f.name} (${f.size_kb}KB)</option>`;
        });
        select.onchange = onCoverPromptChange;
    } catch(e) {
        console.error('加载翻唱参考音频失败', e);
    }
}

async function doCover() {
    if (!modelReady) {
        toast(t('toast.connFail'), 'error');
        await loadModel();
        if (!modelReady) return;
    }

    const lyrics = document.getElementById('coverLyrics').value.trim();
    if (!lyrics) {
        toast(t('toast.enterLyrics'), 'error');
        return;
    }

    const promptWav = document.getElementById('coverPromptWav').value;
    const promptText = document.getElementById('coverPromptText').value.trim();

    if (promptWav && !promptText) {
        toast(t('toast.refNeededCover'), 'error');
        return;
    }

    const lines = lyrics.split('\n').filter(l => l.trim());
    if (lines.length === 0) {
        toast(t('toast.lyricsEmpty'), 'error');
        return;
    }

    const longLine = lines.find(l => l.length > 500);
    if (longLine) {
        toast(t('toast.lineLong'), 'error');
        return;
    }

    document.getElementById('btnCoverGenerate').disabled = true;
    document.getElementById('coverProgress').style.display = 'block';
    document.getElementById('coverResult').innerHTML = '';
    document.getElementById('coverMsg').textContent = `${t('toast.synthesizing')} 1/${lines.length}...`;
    document.getElementById('coverPercent').textContent = '0%';
    document.getElementById('coverFill').style.width = '0%';

    const audioChunks = [];
    for (let i = 0; i < lines.length; i++) {
        document.getElementById('coverMsg').textContent = `${t('toast.synthesizing')} ${i+1}/${lines.length}: "${lines[i].substring(0,20)}..."`;
        document.getElementById('coverPercent').textContent = Math.round((i/lines.length)*100) + '%';
        document.getElementById('coverFill').style.width = Math.round((i/lines.length)*100) + '%';

        const formData = new FormData();
        formData.append('text', lines[i]);
        formData.append('prompt_wav', promptWav);
        formData.append('prompt_text', promptText);
        formData.append('cfg', '2.0');
        formData.append('steps', '10');

        try {
            const submitRes = await fetch('/api/tts', { method: 'POST', body: formData });
            const submitData = await submitRes.json();
            if (!submitData.success) {
                toast(`${t('toast.lineFailed')}: ${submitData.error}`, 'error');
                continue;
            }

            const result = await waitForTask(submitData.task_id);
            if (result) {
                const binaryStr = atob(result.audio_base64);
                const bytes = new Uint8Array(binaryStr.length);
                for (let j = 0; j < binaryStr.length; j++) {
                    bytes[j] = binaryStr.charCodeAt(j);
                }
                audioChunks.push({ buffer: bytes.buffer, sr: result.sample_rate });
            }
        } catch(e) {
            toast(`${t('toast.lineReqFail')}`, 'error');
        }
    }

    if (audioChunks.length > 0) {
        document.getElementById('coverMsg').textContent = t('toast.merging');
        const merged = mergeWavBuffers(audioChunks);
        const blob = new Blob([merged], { type: 'audio/wav' });
        const url = URL.createObjectURL(blob);

        document.getElementById('coverProgress').style.display = 'none';
        document.getElementById('btnCoverGenerate').disabled = false;
        document.getElementById('coverResult').innerHTML = `
            <div class="result-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="color:var(--green); font-weight:600; font-size:13px;">${t('toast.coverComplete')} (${lines.length})</span>
                    <button class="btn btn-outline btn-sm" onclick="downloadCover('${url}')">${t('toast.download')}</button>
                </div>
                <audio controls src="${url}" style="width:100%; margin-top:8px;"></audio>
            </div>
        `;
    } else {
        document.getElementById('coverProgress').style.display = 'none';
        document.getElementById('btnCoverGenerate').disabled = false;
        toast(t('toast.genFailCover'), 'error');
    }
}

async function waitForTask(taskId) {
    for (let i = 0; i < 120; i++) {
        await new Promise(r => setTimeout(r, 1000));
        try {
            const res = await fetch('/api/task/' + taskId);
            const data = await res.json();
            if (data.task.status === 'done') return data.task.result;
            if (data.task.status === 'error') return null;
        } catch(e) {
            return null;
        }
    }
    return null;
}

function mergeWavBuffers(chunks) {
    const sampleRate = chunks[0].sr;
    const totalSamples = chunks.reduce((sum, c) => sum + new Int16Array(c.buffer).length, 0);
    const totalBytes = 44 + totalSamples * 2;

    const merged = new ArrayBuffer(totalBytes);
    const view = new DataView(merged);

    writeString(view, 0, 'RIFF');
    view.setUint32(4, totalBytes - 8, true);
    writeString(view, 8, 'WAVE');
    writeString(view, 12, 'fmt ');
    view.setUint32(16, 16, true);
    view.setUint16(20, 1, true);
    view.setUint16(22, 1, true);
    view.setUint32(24, sampleRate, true);
    view.setUint32(28, sampleRate * 2, true);
    view.setUint16(32, 2, true);
    view.setUint16(34, 16, true);
    writeString(view, 36, 'data');
    view.setUint32(40, totalSamples * 2, true);

    let offset = 44;
    for (const chunk of chunks) {
        const bytes = new Uint8Array(chunk.buffer);
        const dst = new Uint8Array(merged, offset, bytes.length);
        dst.set(bytes);
        offset += bytes.length;
    }

    return merged;
}

function writeString(view, offset, str) {
    for (let i = 0; i < str.length; i++) {
        view.setUint8(offset + i, str.charCodeAt(i));
    }
}

function downloadCover(url) {
    const a = document.createElement('a');
    a.href = url;
    a.download = 'cover_output.wav';
    a.click();
}

function installRVC() {
    const card = document.getElementById('rvcInstallCard');
    const log = document.getElementById('rvcInstallLog');
    card.style.display = 'block';
    log.innerHTML = '> Initializing RVC installer...\n> Check the spawned console for progress.\n\n';

    fetch('/api/install_rvc', { method: 'POST' })
        .then(r => r.json())
        .then(data => {
            if (data.success) {
                log.innerHTML += data.message + '\n';
                document.getElementById('rvcProgressFill').style.width = '100%';
            } else {
                log.innerHTML += '> [ERROR] ' + data.error + '\n';
            }
        })
        .catch(e => {
            log.innerHTML += '> [ERROR] Request failed: ' + e.message + '\n';
        });
}

// ============================================================
// 启动
// ============================================================
init();
