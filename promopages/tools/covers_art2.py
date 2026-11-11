import subprocess, sys, pathlib, base64, glob
S, R, D = sys.argv[1], sys.argv[2], sys.argv[3]
b64 = lambda f: base64.b64encode(open(f,'rb').read()).decode()
img = lambda p: 'data:image/jpeg;base64,' + b64(glob.glob(f'{R}/{p}*')[0])
logo = 'data:image/png;base64,' + b64(f'{S}/site/logo.png')
covers = [
 ("01_kuhnya-celikom", "51979/x8yxv1byrt", "center 55%", "center 55%"),
 ("02_lyuis-kastryuli", "11071/gavfsqg9x9", "center 50%", "center 50%", None, "contain"),
 ("03_chaynik-reynard", "11372/70hddjhpop", "center 50%", "center 50%", "11372/2rctbjdyc5", "contain"),
 ("04_pribory-somerset", "21665/1oin0roazr", "center 50%", "center 50%"),
]
SALE = set()
TAG = """<div style="position:absolute;top:{top}px;right:{right}px;transform:scale({sc});transform-origin:top right">
<svg width="400" height="300" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg" style="display:block;overflow:visible">
<path d="M350 -40 C 335 10, 290 40, 262 84" stroke="#9a9a9a" stroke-width="3" fill="none"/>
<g transform="rotate(-10 200 160)" filter="url(#sh)">
<path d="M84 72 H366 a18 18 0 0 1 18 18 V230 a18 18 0 0 1 -18 18 H84 L20 160 Z" fill="#DA3B64"/>
<circle cx="66" cy="160" r="12" fill="#fff"/>
<text x="232" y="150" text-anchor="middle" font-family="Inter" font-weight="700" font-size="46" fill="#fff">Сезон</text>
<text x="232" y="204" text-anchor="middle" font-family="Inter" font-weight="700" font-size="46" fill="#fff">распродаж</text>
</g>
<defs><filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="8" stdDeviation="10" flood-opacity=".22"/></filter></defs>
</svg></div>"""
sizes = [("mob_1080x1080", 1080, 1080, 2), ("desk_1600x800", 1600, 800, 3)]
for c in covers:
    name, photo, fm, fd = c[:4]; dphoto = (c[4] if len(c) > 4 and c[4] else photo); dfit = c[5] if len(c) > 5 else 'cover'
    for tag, w, h, idx in sizes:
        pos = fm if idx == 2 else fd
        lh = 52 if w == 1080 else 56
        ty, tx = (150, 90) if w == 1080 else (130, 150)
        tagh = TAG.format(top=(ty-20) if w == 1080 else 40, right=(tx-30) if w == 1080 else 120, sc=1.0 if w == 1080 else 0.9) if name in SALE else ''
        html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0}} body{{width:{w}px;height:{h}px;overflow:hidden;background:#fff url({img(photo if idx == 2 else dphoto)}) {pos}/{('cover' if idx == 2 else dfit)} no-repeat;position:relative}}
.logo{{position:absolute;top:{ty}px;left:{tx}px;background:rgba(255,255,255,.95);padding:14px 22px;border-radius:14px;box-shadow:0 6px 24px rgba(0,0,0,.10)}}
.logo img{{height:{lh}px;display:block}}</style></head><body><div class="logo"><img src="{logo}"></div>{tagh}</body></html>"""
        p = pathlib.Path(f'{S}/cov_{name}_{tag}.html'); p.write_text(html)
        js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:{w},height:{h}}}}});await pg.goto('file://{p}');await pg.waitForTimeout(300);await pg.screenshot({{path:'{D}/{name}_{tag}.jpg',type:'jpeg',quality:92}});await b.close();}})();"
        subprocess.run(['node','-e',js],check=True)
print('ok')
