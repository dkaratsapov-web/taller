import subprocess, sys, pathlib, base64, glob, re
S, R, D = sys.argv[1], sys.argv[2], sys.argv[3]
b64 = lambda f: base64.b64encode(open(f,'rb').read()).decode()
img = lambda p: 'data:image/jpeg;base64,' + b64(glob.glob(f'{R}/{p}*')[0])
logo = 'data:image/png;base64,' + b64(f'{S}/site/logo.png')
nb = lambda t: re.sub(r"(?<=\s)(в|до|к|по|с|и|о|на|от|за|не|что|у)\s", lambda m: m.group(1)+" ", t)
items = [
 ("01_cheklist", [("44182/1ypuayqaoy","cover","center 68%")], "Чек-лист", "Что проверить в посуде до покупки", "7 пунктов, которые стоит сверить в карточке товара"),
 ("02_tolshchina-dna", [("44182/m269m827fc","contain","center"),("44903/cq3njxdb3z","contain","center")], "Чек-лист", "Начните с толщины дна", "У Professional капсулированное дно 5 мм, у «Антрацита» 3,3 мм"),
 ("03_harakteristiki", [("44903/4ug718lrom","cover","center 45%")], "Сезон распродаж", "Выбирайте посуду по характеристикам", "Материал, дно, покрытие и гарантия: что сверить"),
 ("04_plita", [("44024/6zedo8pakj","cover","center 55%")], "Чек-лист", "Подойдёт ли сковорода к вашей\u00a0плите?", "«Минерал» подходит для всех типов плит, включая индукцию"),
]
for name, photos, tag, title, sub in items:
    cells = ''.join(f'<div class="cell" style="background:#fff url({img(p)}) {pos}/{fit} no-repeat"></div>' for p, fit, pos in photos)
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1080px;font-family:Inter,sans-serif;overflow:hidden;background:#fff;position:relative}}
.photo{{position:absolute;top:0;left:0;right:0;height:700px;display:flex;gap:0}}
.cell{{flex:1;height:100%}}
.logo{{position:absolute;top:40px;left:40px;background:rgba(255,255,255,.95);padding:16px 24px;border-radius:14px;box-shadow:0 6px 24px rgba(0,0,0,.08)}}
.logo img{{height:54px;display:block}}
.panel{{position:absolute;left:0;right:0;bottom:0;height:380px;background:#fff;padding:44px 56px 0}}
.panel:before{{content:"";position:absolute;top:0;left:56px;width:72px;height:6px;background:#DA3B64;border-radius:3px}}
.tag{{display:inline-block;background:#DA3B64;color:#fff;font-weight:600;font-size:24px;padding:8px 18px;border-radius:8px;margin:18px 0 22px}}
h1{{font-weight:700;font-size:60px;line-height:1.08;color:#1f1f1f;letter-spacing:-1px}}
p{{margin-top:16px;font-size:28px;line-height:1.3;color:#707070}}
</style></head><body><div class="photo">{cells}</div><div class="logo"><img src="{logo}"></div>
<div class="panel"><span class="tag">{tag}</span><h1>{nb(title)}</h1><p>{nb(sub)}</p></div></body></html>"""
    p = pathlib.Path(f'{S}/{name}_real.html'); p.write_text(html)
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:1080}}}});await pg.goto('file://{p}');await pg.waitForTimeout(300);await pg.screenshot({{path:'{D}/{name}_1080.png'}});await b.close();}})();"
    subprocess.run(['node','-e',js],check=True)
print('ok')
