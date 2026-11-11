"""Премиальные иллюстрации для статей TalleR: общая дизайн-система и рендер."""
import subprocess, pathlib, base64, glob, re
FONTS = '/tmp/claude-0/-home-user-taller/b76a1919-6550-5252-ab1c-cd03450ea53b/scratchpad/fonts/node_modules/@fontsource/cormorant-garamond/files'
def b64(f): return base64.b64encode(open(f,'rb').read()).decode()
class Kit:
    def __init__(self, S, R):
        self.S, self.R = S, R
        self.logo = 'data:image/png;base64,' + b64(f'{S}/site/logo.png')
        self.css = ''.join(f"@font-face{{font-family:'Cormorant';font-weight:{w};src:url(data:font/woff2;base64,{b64(f'{FONTS}/cormorant-garamond-{sub}-{w}-normal.woff2')}) format('woff2');unicode-range:{rng}}}"
            for w in (500,600) for sub,rng in (('cyrillic','U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116'),('latin','U+0000-00FF,U+2000-206F,U+20AC,U+20BD,U+2122,U+2212'))) + CSS
    def img(self, p): return 'data:image/jpeg;base64,' + b64(glob.glob(f'{self.R}/{p}*')[0])
    def render(self, body, out):
        html = f'<!doctype html><html><head><meta charset="utf-8"><style>{self.css}</style></head><body>{body}</body></html>'
        p = pathlib.Path(out).with_suffix('.html'); p.write_text(html)
        js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:800}}}});await pg.goto('file://{p}');await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(200);await pg.screenshot({{path:'{out}',fullPage:true}});await b.close();}})();"
        subprocess.run(['node','-e',js],check=True); p.unlink()
    # --- блоки ---
    def top(self, label):
        return f'<header class="top"><span class="label">{nb(label)}</span><img class="logo" src="{self.logo}"></header>'
    def photo(self, p, h, pos='center', fit='cover', bg='#fff'):
        return f'<div class="photo" style="height:{h}px;background:{bg} url({self.img(p)}) {pos}/{fit} no-repeat"></div>'
def nb(t): return re.sub(r"(?<=[\s>(«])(в|до|к|по|с|и|о|на|от|за|не|у|для|без|из)\s", lambda m: m.group(1)+" ", t)
def figures(items, cols=None, size=104, band=True):
    cols = cols or len(items)
    cells = ''.join(f'<div class="fig"><b style="font-size:{size}px">{v}</b>{dim if dim else ""}<span>{nb(l)}</span></div>' for v,l,dim in [(i+(None,))[:3] for i in items])
    return f'<section class="{"band" if band else "plain"}"><div class="figs" style="grid-template-columns:repeat({cols},1fr)">{cells}</div></section>'
def dimline(w=200):
    return f'<svg class="dim" width="{w}" height="18" viewBox="0 0 {w} 18"><path d="M1 1V17M{w-1} 1V17M1 9H{w-1}" stroke="#DA3B64" stroke-width="2" fill="none"/></svg>'
def products(kit, items, cols=None, pic=300, name=46):
    cols = cols or len(items)
    cells = ''.join(f'<div class="prod"><div class="pic" style="height:{pic}px;background-image:url({kit.img(p)})"></div><h3 style="font-size:{name}px">{nb(t)}</h3>{"".join(f"<p>{nb(x)}</p>" for x in (d if isinstance(d,list) else [d]))}</div>' for p,t,d in items)
    return f'<section class="prods" style="grid-template-columns:repeat({cols},1fr)">{cells}</section>'
def foot(t): return f'<p class="foot">{nb(t)}</p>'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;background:#fff;color:#1E1C1D;font-family:Inter,sans-serif;-webkit-font-smoothing:antialiased}
.top{display:flex;justify-content:space-between;align-items:center;padding:44px 64px 36px}
.label{font-size:31px;font-weight:500;color:#5E595B;letter-spacing:.2px}
.logo{height:40px;display:block}
.photo{width:1080px}
.band{background:#F1EFEE;padding:56px 64px 60px}
.plain{padding:48px 64px 56px}
.figs{display:grid}
.fig{padding:0 36px;border-left:1px solid rgba(30,28,29,.12);display:flex;flex-direction:column}
.fig:first-child{padding-left:0;border-left:none}
.fig b{font-family:Cormorant,serif;font-weight:600;line-height:.95;letter-spacing:-.5px;font-variant-numeric:lining-nums tabular-nums;color:#1E1C1D}
.fig span{font-size:34px;line-height:1.28;color:#5E595B;margin-top:16px}
.dim{display:block;margin-top:14px}
.prods{display:grid;padding:8px 40px 56px}
.prod{padding:0 24px;border-left:1px solid rgba(30,28,29,.12)}
.prod:first-child{border-left:none}
.prod .pic{background:#fff center/contain no-repeat;margin-bottom:20px}
.prod h3{font-family:Cormorant,serif;font-weight:600;line-height:1.02;letter-spacing:-.3px}
.prod p{font-size:31px;line-height:1.3;color:#5E595B;margin-top:10px}
.prod p b{color:#1E1C1D;font-weight:500}
.list{padding:40px 64px 56px}
.row{display:grid;grid-template-columns:76px 1fr;align-items:baseline;padding:20px 0;border-top:1px solid rgba(30,28,29,.12)}
.row:first-child{border-top:none}
.row i{font-style:normal;font-family:Cormorant,serif;font-variant-numeric:lining-nums;font-weight:600;font-size:60px;line-height:1;color:#DA3B64}
.row span{font-size:40px;font-weight:500;line-height:1.2}
.quotes{padding:48px 64px 24px}
.q{position:relative;padding:8px 0 36px 76px}
.q:before{content:"«";position:absolute;left:0;top:-14px;font-family:Cormorant,serif;font-weight:600;font-size:120px;line-height:1;color:#DA3B64}
.q p{font-family:Cormorant,serif;font-weight:500;font-size:46px;line-height:1.18;color:#1E1C1D}
.q .who{display:block;font-size:26px;color:#9A9497;margin-top:10px}
.q{padding-bottom:30px}
.foot{font-size:25px;line-height:1.4;color:#9A9497;padding:0 64px 44px}
.band + .foot{padding-top:24px;background:#F1EFEE}
"""

_nb_words = nb
def nb(t):
    """Неразрывные пробелы после коротких слов и между числом и единицей измерения."""
    return re.sub(r"(\d)\s(г|мм|см|л|°C|₽|%)", lambda m: m.group(1) + " " + m.group(2), _nb_words(t))
