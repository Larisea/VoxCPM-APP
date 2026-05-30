// ============================================================
// VoxCPM Landing — Clean Waveform
// ============================================================
(function () {
  const canvas = document.getElementById('waveform');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let W, H, midY, animId;

  function resize() {
    const dpr = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();
    W = rect.width; H = rect.height;
    canvas.width = W * dpr; canvas.height = H * dpr;
    ctx.scale(dpr, dpr);
    midY = H / 2;
  }
  window.addEventListener('resize', resize);
  resize();

  const style = getComputedStyle(document.documentElement);
  const accent = style.getPropertyValue('--accent').trim() || '#8b7dff';
  const textMuted = style.getPropertyValue('--text-muted').trim() || '#525252';
  const border = style.getPropertyValue('--border').trim() || '#262626';

  let t = 0;

  function hexToRgb(hex) {
    hex = hex.replace('#', '');
    return {
      r: parseInt(hex.substring(0, 2), 16),
      g: parseInt(hex.substring(2, 4), 16),
      b: parseInt(hex.substring(4, 6), 16),
    };
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);

    const accentRgb = hexToRgb(accent);
    const mutedRgb = hexToRgb(textMuted);
    const borderRgb = hexToRgb(border);

    // Background reference lines
    ctx.strokeStyle = `rgba(${borderRgb.r}, ${borderRgb.g}, ${borderRgb.b}, 0.4)`;
    ctx.lineWidth = 1;
    for (let y of [midY - 30, midY, midY + 30]) {
      ctx.beginPath();
      ctx.setLineDash([4, 4]);
      ctx.moveTo(0, y);
      ctx.lineTo(W, y);
      ctx.stroke();
    }
    ctx.setLineDash([]);

    // Main waveform — 3 clean layers
    const waves = [
      { freq: 0.008, amp: 32, speed: 0.02, lw: 1.5, color: accentRgb, alpha: 0.7 },
      { freq: 0.013, amp: 22, speed: 0.028, lw: 1.2, color: accentRgb, alpha: 0.3 },
      { freq: 0.02, amp: 12, speed: 0.038, lw: 1, color: mutedRgb, alpha: 0.25 },
    ];

    for (const w of waves) {
      ctx.beginPath();
      ctx.strokeStyle = `rgba(${w.color.r}, ${w.color.g}, ${w.color.b}, ${w.alpha})`;
      ctx.lineWidth = w.lw;

      for (let x = 0; x <= W; x += 1.5) {
        const norm = x / W;
        const env = Math.sin(norm * Math.PI);
        const y = midY
          + Math.sin(x * w.freq + t * w.speed) * w.amp * env
          + Math.sin(x * w.freq * 1.6 + t * w.speed * 0.7) * w.amp * 0.3 * env;
        if (x === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();
    }

    // Thin accent line at center
    ctx.beginPath();
    ctx.strokeStyle = `rgba(${accentRgb.r}, ${accentRgb.g}, ${accentRgb.b}, 0.15)`;
    ctx.lineWidth = 1;
    ctx.moveTo(0, midY);
    ctx.lineTo(W, midY);
    ctx.stroke();

    t += 1;
    animId = requestAnimationFrame(draw);
  }

  draw();
  window.addEventListener('beforeunload', () => cancelAnimationFrame(animId));
})();

// ============================================================
// Scroll reveal
// ============================================================
(function () {
  const obs = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach((el) => obs.observe(el));
})();

// ============================================================
// Nav scroll
// ============================================================
window.addEventListener('scroll', () => {
  document.getElementById('nav').classList.toggle('scrolled', window.scrollY > 30);
});

// ============================================================
// i18n
// ============================================================
const LANDING_I18N = {
  en: {
    nav: 'Launch App',
    badge: 'Neural Voice Synthesis',
    title1: 'One Voice.',
    title2: 'Infinite Possibilities.',
    desc: 'Open-source voice cloning and text-to-speech. Clone any voice from a short audio sample, synthesize natural speech, and create AI covers — all running locally.',
    cta: 'Launch Application',
    ctaSecondary: 'View on GitHub',
    featTitle: 'Everything you need',
    feat1t: 'Text-to-Speech',
    feat1d: 'Natural speech synthesis from text. Fine-tune with CFG scale and inference steps for perfect prosody.',
    feat2t: 'Voice Clone',
    feat2d: 'Upload a short reference audio and transcript. VoxCPM clones the voice for any new text.',
    feat3t: 'Audio Capture',
    feat3d: 'Record reference audio in the browser. Built-in WebM-to-WAV conversion included.',
    feat4t: 'Revoice',
    feat4d: 'Paste lyrics, pick your cloned voice, generate song covers line by line.',
    howTitle: 'How it works',
    step1: 'Record or upload a reference voice',
    step2: 'Input your text or lyrics',
    step3: 'Generate with your cloned voice',
    ctaTitle: 'Start creating with your voice',
    ctaDesc: 'Free and open source. Runs on a 6GB GPU.',
    footerDesc: 'Powered by VoxCPM1.5',
    footerLink: 'Open Application →',
  },
  zh: {
    nav: '启动应用',
    badge: '神经语音合成',
    title1: '一个声音，',
    title2: '无限可能。',
    desc: '开源语音克隆与文本转语音。从一段短音频克隆任何声音，合成自然语音，创建 AI 翻唱 — 全部本地运行。',
    cta: '启动应用',
    ctaSecondary: '查看 GitHub',
    featTitle: '核心能力',
    feat1t: '文本转语音',
    feat1d: '支持多声音的自然语音合成，可调节引导强度和推理步数。',
    feat2t: '语音克隆',
    feat2d: '上传参考音频和对应文本，一键克隆任何声音。',
    feat3t: '录制声音',
    feat3d: '浏览器内直接录制参考音频，内置格式转换。',
    feat4t: 'AI 翻唱',
    feat4d: '粘贴歌词，选择你的克隆声音，逐句生成翻唱。',
    howTitle: '使用流程',
    step1: '录制或上传参考声音',
    step2: '输入文本或歌词',
    step3: '生成你的声音',
    ctaTitle: '开始用你的声音创作',
    ctaDesc: '免费开源，6GB 显存即可运行。',
    footerDesc: '基于 VoxCPM1.5',
    footerLink: '打开应用 →',
  }
};

let landingLang = localStorage.getItem('voxcpm-lang') || 'en';

function setLandingLang(lang) {
  landingLang = lang;
  localStorage.setItem('voxcpm-lang', lang);
  const d = LANDING_I18N[lang] || LANDING_I18N.en;
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (d[key]) el.textContent = d[key];
  });
  document.getElementById('langEn').classList.toggle('active', lang === 'en');
  document.getElementById('langZh').classList.toggle('active', lang === 'zh');
}

document.addEventListener('DOMContentLoaded', () => setLandingLang(landingLang));
