import subprocess, sys, pathlib, base64, glob
S, R, D = sys.argv[1], sys.argv[2], sys.argv[3]
b64 = lambda f: base64.b64encode(open(f,'rb').read()).decode()
img = lambda p: 'data:image/jpeg;base64,' + b64(glob.glob(f'{R}/{p}*')[0])
logo = 'data:image/png;base64,' + b64(f'{S}/site/logo.png')
covers = [  # имя, фото, фокус для 1:1, фокус для 2:1
 ("01_antracit-kuhnya", "44182/1ypuayqaoy", "center 55%", "center 62%"),
 ("02_professional-nabor", "44903/4ug718lrom", "center 50%", "center 45%", "44903/rcrg7xar5e"),
 ("03_greystoun", "44036g/59l4vrgf6b", "center 50%", "center 45%"),
 ("04_mineral-krevetki", "44024/uic0b647gh", "center 50%", "center 52%"),
]
sizes = [("mob_1080x1080", 1080, 1080, 2), ("desk_1600x800", 1600, 800, 3)]
for c in covers:
    name, photo, fm, fd = c[:4]; dphoto = c[4] if len(c) > 4 else photo
    for tag, w, h, idx in sizes:
        pos = fm if idx == 2 else fd
        lh = 52 if w == 1080 else 56
        html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0}} body{{width:{w}px;height:{h}px;overflow:hidden;background:#fff url({img(photo if idx == 2 else dphoto)}) {pos}/cover no-repeat;position:relative}}
.logo{{position:absolute;top:40px;left:40px;background:rgba(255,255,255,.95);padding:14px 22px;border-radius:14px;box-shadow:0 6px 24px rgba(0,0,0,.10)}}
.logo img{{height:{lh}px;display:block}}</style></head><body><div class="logo"><img src="{logo}"></div></body></html>"""
        p = pathlib.Path(f'{S}/cov_{name}_{tag}.html'); p.write_text(html)
        js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:{w},height:{h}}}}});await pg.goto('file://{p}');await pg.waitForTimeout(300);await pg.screenshot({{path:'{D}/{name}_{tag}.jpg',type:'jpeg',quality:92}});await b.close();}})();"
        subprocess.run(['node','-e',js],check=True)
print('ok')
