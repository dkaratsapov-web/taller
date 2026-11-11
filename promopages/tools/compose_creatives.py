import json, subprocess, sys, pathlib, base64
S, D = sys.argv[1], sys.argv[2]
logo = base64.b64encode(open(f'{S}/site/logo.png','rb').read()).decode()
items = [
 ("01_cheklist", "Чек-лист", "Что проверить в посуде до покупки", "7 пунктов, которые стоит сверить в карточке товара", "center 35%"),
 ("02_sravnenie-dna", "Чек-лист", "Начните с толщины дна", "От 3,3 до 5 мм: почему это важно для готовки", "center 30%"),
 ("03_ruki-vybor", "Сезон распродаж", "Выбирайте посуду по характеристикам", "Материал, дно, покрытие и гарантия: что сверить", "center 25%"),
 ("04_indukciya", "Чек-лист", "Подойдёт ли сковорода к вашей плите?", "Совместимость с индукцией и диаметр дна", "center 30%"),
]
import re
nb=lambda t: re.sub(r"(?<=\s)(в|до|к|по|с|и|о|на|от|за|не|что)\s", lambda m: m.group(1)+"\u00a0", t)
for name, tag, title, sub, pos in items:
    title, sub = nb(title), nb(sub)
    img = base64.b64encode(open(f'{D}/{name}.png','rb').read()).decode()
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1080px;font-family:Inter,sans-serif;overflow:hidden;position:relative;background:#fff}}
.bg{{position:absolute;inset:0;background:url(data:image/png;base64,{img}) {pos}/cover no-repeat}}
.logo{{position:absolute;top:44px;left:44px;background:rgba(255,255,255,.94);padding:18px 26px;border-radius:16px;box-shadow:0 6px 24px rgba(0,0,0,.08)}}
.logo img{{height:56px;display:block}}
.card{{position:absolute;left:44px;right:44px;bottom:44px;background:rgba(255,255,255,.96);border-radius:24px;padding:40px 48px 44px;box-shadow:0 10px 40px rgba(0,0,0,.12)}}
.tag{{display:inline-block;background:#DA3B64;color:#fff;font-weight:600;font-size:24px;letter-spacing:.2px;padding:8px 18px;border-radius:8px;margin-bottom:22px}}
h1{{font-weight:700;font-size:58px;line-height:1.08;color:#1f1f1f;letter-spacing:-1px}}
p{{margin-top:16px;font-size:28px;line-height:1.3;color:#707070}}
</style></head><body><div class="bg"></div><div class="logo"><img src="data:image/png;base64,{logo}"></div>
<div class="card"><span class="tag">{tag}</span><h1>{title}</h1><p>{sub}</p></div></body></html>"""
    p = pathlib.Path(f'{S}/{name}.html'); p.write_text(html)
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:1080}},deviceScaleFactor:1}});await pg.goto('file://{p}');await pg.waitForTimeout(300);await pg.screenshot({{path:'{D}/final/{name}_1080.png'}});await b.close();}})();"
    subprocess.run(['node','-e',js],check=True)
print('ok')
