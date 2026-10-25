# Shared CSS/JS (palette from acl-semg-robustness.vercel.app, values inlined so no CSS custom properties are needed)
P=dict(bg="#0b111c",bg2="#0f1726",card="#161e2e",card2="#1b2537",line="#26324a",line2="#33415e",
 ink="#e8edf6",muted="#a3afc4",soft="#8592aa",coral="#e8603c",cyan="#26a3cc",coralg="#ff8a65",cyang="#5fd4f5",focus="#ffd166")
CSS="""
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:BG;color:INK;font:17px/1.65 BODYF;overflow-x:hidden;
background-image:linear-gradient(BG2 1px,transparent 1px),linear-gradient(90deg,BG2 1px,transparent 1px);background-size:48px 48px}
a{color:CYANG}
:focus-visible{outline:2px solid FOCUS;outline-offset:3px;border-radius:4px}
.skip{position:absolute;inset-inline-start:-9999px}.skip:focus{inset-inline-start:12px;top:12px;z-index:60;background:INK;color:BG;padding:8px 12px;border-radius:8px}
.wrap{max-width:1160px;margin:0 auto;padding:0 24px}
.progress{position:fixed;top:0;left:0;height:2px;width:100%;transform-origin:0 50%;transform:scaleX(0);background:linear-gradient(90deg,CYAN,CORAL);z-index:40}
[dir=rtl] .progress{transform-origin:100% 50%;background:linear-gradient(270deg,CYAN,CORAL)}
.topbar{position:sticky;top:0;z-index:30;background:rgba(11,17,28,.84);backdrop-filter:blur(12px);border-bottom:1px solid LINE}
.topbar .wrap{display:flex;align-items:center;gap:18px;height:64px}
.brand{display:flex;align-items:center;gap:10px;color:INK;text-decoration:none;font:600 16px HEADF;white-space:nowrap}
.brand svg{width:30px;height:30px;flex:none}
.nav{display:flex;gap:2px;margin-inline-start:auto;overflow-x:auto}
.nav a{color:MUTED;text-decoration:none;font-size:14px;padding:7px 11px;border-radius:8px;white-space:nowrap}
.nav a:hover,.nav a.on{color:INK;background:CARD}
.lang{display:inline-flex;border:1px solid LINE2;border-radius:9px;overflow:hidden;flex:none}
.lang a{color:MUTED;font:600 12px MONOF;padding:7px 10px;text-decoration:none}
.lang a[aria-current]{background:INK;color:BG}
.kicker{font:600 12px MONOF;letter-spacing:2px;text-transform:uppercase;color:CYANG}
.kicker .dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:CORAL;margin-inline-end:8px;box-shadow:0 0 12px CORALG;animation:pulse 2s infinite}
@keyframes pulse{50%{opacity:.35}}
h1,h2,h3{font-family:HEADF;font-weight:600;letter-spacing:-.02em;line-height:1.12;margin:0}
h1{font-size:clamp(38px,6vw,72px);margin:18px 0 22px}
h1 .c{color:CORAL} h1 .y{color:CYAN}
h2{font-size:clamp(28px,3.8vw,46px);margin:12px 0 16px}
h3{font-size:21px;margin:0 0 8px}
.lead{font-size:clamp(18px,2vw,21px);color:MUTED;max-width:720px}
.muted{color:MUTED}.small{font-size:14px}.soft{color:SOFT}
.num{font:600 12px MONOF;color:SOFT;letter-spacing:2px}
.cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 18px;border-radius:10px;font:600 15px BODYF;text-decoration:none;border:1px solid LINE2;color:INK;background:CARD;transition:transform .2s,border-color .2s}
.btn:hover{transform:translateY(-1px);border-color:SOFT}
.btn.primary{background:CORAL;border-color:CORAL;color:#140804}
section{padding:84px 0;border-top:1px solid LINE;scroll-margin-top:60px}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:start}
.grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.grid-2>*,.grid-3>*,.hero-grid>*,.optima>*,.toc>*,.kpis>*{min-width:0}
.card{background:CARD;border:1px solid LINE;border-radius:18px;padding:26px}
.card.glow{box-shadow:0 30px 80px -40px rgba(38,163,204,.5)}
.card p{color:#d3dbe8}
.tag{display:inline-block;font:600 11px MONOF;letter-spacing:1px;text-transform:uppercase;padding:4px 9px;border-radius:6px;background:CARD2;color:CYANG;border:1px solid LINE2}
.tag.coral{color:CORALG}
.abs{display:inline-block;font:500 10.5px MONOF;padding:1px 6px;border-radius:5px;border:1px dashed LINE2;color:SOFT;vertical-align:middle;white-space:nowrap}
.callout{border-inline-start:3px solid CORAL;background:CARD;padding:18px 22px;border-radius:14px;margin:26px 0;color:MUTED}
.callout strong{color:INK}
.callout.cy{border-inline-start-color:CYAN}
.hero{padding-top:70px;padding-bottom:40px}
.hero-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:44px;align-items:center}
.scope{background:linear-gradient(180deg,CARD,BG2);border:1px solid LINE2;border-radius:22px;padding:22px;box-shadow:0 40px 90px -45px rgba(232,96,60,.45)}
.scope-top{display:flex;justify-content:space-between;font:12px MONOF;color:SOFT;margin-bottom:6px;gap:8px}
.scope-top .live{color:CORALG}
.rings{display:grid;grid-template-columns:1fr 1fr;gap:12px;text-align:center}
.rings svg{width:100%;max-width:190px;height:auto;display:block;margin:0 auto}
.rings .trk{fill:none;stroke:LINE;stroke-width:12}
.rings .arc{fill:none;stroke-width:12;stroke-linecap:round;transform:rotate(-90deg);transform-origin:50% 50%;transition:stroke-dashoffset 1.6s cubic-bezier(.2,.7,.2,1)}
.rings .v{font:600 30px MONOF;fill:INK}
.rings p{margin:6px 0 0;font-size:14px;color:MUTED}
.scope-cap{font-size:12.5px;color:SOFT;margin-top:16px}
.kpis{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-top:54px}
.kpi{background:CARD;border:1px solid LINE;border-radius:14px;padding:18px}
.kpi b{display:block;font:600 32px/1.1 MONOF;font-variant-numeric:tabular-nums}
.kpi b.c{color:CORAL}.kpi b.y{color:CYAN}
.kpi span{font-size:13px;color:MUTED}
.toc{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-top:26px}
.toc a{display:block;background:CARD;border:1px solid LINE;border-radius:16px;padding:18px;text-decoration:none;color:INK;transition:transform .3s,border-color .3s}
.toc a:hover{transform:translateY(-4px);border-color:CORAL}
.toc .k{font:600 12px MONOF;color:CORALG}
.toc b{display:block;font:600 17px HEADF;margin:6px 0}
.toc span{font-size:13.5px;color:MUTED}
.table-wrap{overflow-x:auto;border:1px solid LINE;border-radius:14px;background:CARD;margin:22px 0}
table{border-collapse:collapse;width:100%;font-size:14.5px}
th,td{text-align:start;padding:12px 14px;border-bottom:1px solid LINE;vertical-align:top}
th{font:600 11px MONOF;letter-spacing:1px;text-transform:uppercase;color:SOFT;background:CARD2}
td b{color:INK}
tr:last-child td{border-bottom:0}
td.no{color:CORALG;font-weight:600}td.yes{color:CYANG;font-weight:600}
.ev-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px;margin:22px 0}
.ev{background:CARD2;border:1px solid LINE;border-radius:14px;padding:18px}
.ev .yr{font:600 12px MONOF;color:SOFT}
.ev b{display:block;font:600 16px HEADF;margin:6px 0}
.ev p{margin:6px 0 0;font-size:14.5px;color:#d3dbe8}
.ev .big{font:600 30px MONOF;color:CORAL;display:block;margin-top:6px}
.ev a{font-size:13px}
.bars{display:grid;gap:12px;margin:18px 0 6px}
.bar{display:grid;grid-template-columns:200px 1fr 56px;gap:12px;align-items:center;font-size:14px}
.bar .track{height:14px;background:CARD2;border-radius:7px;overflow:hidden}
.bar .fill{height:100%;border-radius:7px;background:CYAN;transform-origin:0 50%;transition:transform 1.1s cubic-bezier(.2,.7,.2,1)}
[dir=rtl] .bar .fill{transform-origin:100% 50%}
.bar .fill.c{background:CORAL}.bar .fill.s{background:LINE2}
.bar b{font-family:MONOF;text-align:end}
.js .bars:not(.in) .fill{transform:scaleX(0)}
.optima{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px}
.opt{background:CARD2;border:1px solid LINE;border-radius:14px;padding:16px}
.opt .chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.opt .chips span{font:600 13px MONOF;padding:5px 9px;border-radius:7px;border:1px solid CORAL;color:INK}
.road{display:grid;grid-template-columns:repeat(3,1fr);margin-top:30px;position:relative}
.road::before{content:"";position:absolute;left:0;right:0;top:11px;height:2px;background:linear-gradient(90deg,CORAL,CYAN,LINE2)}
[dir=rtl] .road::before{background:linear-gradient(270deg,CORAL,CYAN,LINE2)}
.road div{padding:34px 22px 0 0;position:relative}
[dir=rtl] .road div{padding:34px 0 0 22px}
.road div::before{content:"";position:absolute;top:4px;inset-inline-start:0;width:16px;height:16px;border-radius:50%;background:BG;border:3px solid CORAL}
.road div:nth-child(2)::before{border-color:CYAN}.road div:nth-child(3)::before{border-color:LINE2}
.road b{display:block;font:600 18px HEADF;margin-bottom:6px}
.road p{color:MUTED;font-size:15px;margin:0}
.rules{list-style:none;padding:0;margin:18px 0;display:grid;gap:10px;counter-reset:r}
.rules li{background:CARD2;border:1px solid LINE;border-radius:12px;padding:14px 16px 14px 56px;position:relative;counter-increment:r}
[dir=rtl] .rules li{padding:14px 56px 14px 16px}
.rules li::before{content:counter(r,decimal-leading-zero);position:absolute;inset-inline-start:16px;top:14px;font:600 13px MONOF;color:CORALG}
.rules li small{display:block;color:SOFT;font-size:12.5px;margin-top:4px}
.concept{border:1px dashed CORAL;border-radius:18px;padding:26px;background:rgba(232,96,60,.05)}
ol.refs{padding-inline-start:24px;font-size:14.5px;color:#d3dbe8}
ol.refs li{margin-bottom:9px;overflow-wrap:anywhere}
ol.refs .st{color:SOFT;font-size:12.5px}
footer{border-top:1px solid LINE;padding:44px 0 60px;color:MUTED;font-size:14px}
.disc{border:1px solid LINE2;border-radius:14px;padding:16px 18px;background:CARD;color:INK;margin:24px 0}
.js .reveal{opacity:0;transform:translateY(24px);transition:opacity .8s ease,transform .8s cubic-bezier(.2,.7,.2,1)}
.js .reveal.in{opacity:1;transform:none}
.js .reveal.d1{transition-delay:.1s}.js .reveal.d2{transition-delay:.2s}.js .reveal.d3{transition-delay:.3s}.js .reveal.d4{transition-delay:.4s}
[lang=ar] .kicker,[lang=ar] .num,[lang=ar] th,[lang=ar] .tag{letter-spacing:0;text-transform:none}
[lang=ar] h1,[lang=ar] h2,[lang=ar] h3{letter-spacing:0;line-height:1.35}
[lang=ar] body{line-height:1.85}
[lang=ar] .kicker,[lang=ar] .num,[lang=ar] .scope-top,[lang=ar] .tag,[lang=ar] th,[lang=ar] .ev .yr,[lang=ar] .opt .chips span{font-family:ARABF}
@media (max-width:980px){.hero-grid,.grid-2{grid-template-columns:1fr}.kpis{grid-template-columns:repeat(3,1fr)}.toc{grid-template-columns:repeat(2,1fr)}.grid-3{grid-template-columns:1fr 1fr}}
@media (max-width:720px){body{font-size:16px}.wrap{padding:0 16px}
.topbar .wrap{height:auto;min-height:58px;flex-wrap:wrap;padding-top:8px;padding-bottom:8px;gap:8px}
.nav{order:3;width:100%;margin-inline-start:0}.lang{margin-inline-start:auto}
section{padding:56px 0}.kpis,.toc{grid-template-columns:1fr 1fr}.grid-3,.road,.optima{grid-template-columns:1fr}.road::before{display:none}
.bar{grid-template-columns:1fr 48px}.bar .lab{grid-column:1/-1}.card{padding:20px}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}
.js .reveal,.bar .fill,.rings .arc,.toc a,.btn{transition:none!important;transform:none!important;opacity:1!important}
.js .bars:not(.in) .fill{transform:none!important}.kicker .dot{animation:none}}
@media print{.topbar,.progress,.cta{display:none}body{background:#fff;color:#000}.js .reveal{opacity:1!important;transform:none!important}}
"""
JS="""
document.documentElement.classList.add('js');
(function(){
var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
var loc=document.documentElement.dataset.loc||'en-US';
var bar=document.querySelector('.progress');
function onScroll(){var h=document.documentElement;var k=h.scrollTop/Math.max(1,h.scrollHeight-h.clientHeight);if(bar)bar.style.transform='scaleX('+k+')';}
addEventListener('scroll',onScroll,{passive:true});onScroll();
function fmt(n,v){var d=+(n.dataset.dec||0);return v.toLocaleString(loc,{minimumFractionDigits:d,maximumFractionDigits:d})+(n.dataset.suf||'');}
function countUp(n){var to=parseFloat(n.dataset.count);if(reduce){n.textContent=fmt(n,to);return;}var t0=performance.now();
function st(t){var k=Math.min(1,(t-t0)/1400);n.textContent=fmt(n,to*(1-Math.pow(1-k,3)));if(k<1)requestAnimationFrame(st);}requestAnimationFrame(st);}
function ring(svg){svg.querySelectorAll('.arc').forEach(function(a){var r=+a.getAttribute('r'),c=2*Math.PI*r,p=+a.dataset.p;a.style.strokeDasharray=c;a.style.strokeDashoffset=c*(1-p/100);});}
document.querySelectorAll('.rings .arc').forEach(function(a){var c=2*Math.PI*(+a.getAttribute('r'));a.style.strokeDasharray=c;a.style.strokeDashoffset=reduce?c*(1-a.dataset.p/100):c;});
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;var t=e.target;t.classList.add('in');if(t.dataset.count)countUp(t);if(t.classList.contains('rings'))ring(t);io.unobserve(t);});},{threshold:0.2,rootMargin:'0px 0px -40px 0px'});
document.querySelectorAll('.reveal,[data-count],.bars,.rings').forEach(function(n){io.observe(n);});
var links=[].slice.call(document.querySelectorAll('.nav a'));
var so=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;links.forEach(function(l){l.classList.toggle('on',l.getAttribute('href')==='#'+e.target.id);});});},{rootMargin:'-45% 0px -50% 0px'});
document.querySelectorAll('main section[id]').forEach(function(s){so.observe(s);});
})();
"""
def css(lang,extra=''):
    head = "'IBM Plex Sans Arabic','Noto Naskh Arabic',system-ui,sans-serif" if lang=="ar" else "'Space Grotesk',system-ui,sans-serif"
    body = "'IBM Plex Sans Arabic','Noto Naskh Arabic',system-ui,sans-serif" if lang=="ar" else "'IBM Plex Sans',system-ui,-apple-system,'Segoe UI',sans-serif"
    s=(CSS+extra).replace("ARABF","'IBM Plex Sans Arabic','Noto Naskh Arabic',system-ui,sans-serif").replace("HEADF",head).replace("BODYF",body).replace("MONOF","'JetBrains Mono',ui-monospace,Consolas,monospace")
    for k,v in sorted(P.items(),key=lambda x:-len(x[0])):
        s=s.replace(k.upper(),v)
    return s
