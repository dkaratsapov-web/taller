import subprocess, sys, pathlib, base64, glob, re
S, R, D = sys.argv[1], sys.argv[2], sys.argv[3]
b64 = lambda f: base64.b64encode(open(f,'rb').read()).decode()
img = lambda p: 'data:image/jpeg;base64,' + b64(glob.glob(f'{R}/{p}*')[0])
logo = 'data:image/png;base64,' + b64(f'{S}/site/logo.png')
nb = lambda t: re.sub(r"(?<=[\s>])(в|до|к|по|с|и|о|на|от|за|не|у|для|без)\s", lambda m: m.group(1)+" ", t)
CSS = """*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;font-family:Inter,sans-serif;background:#fff;color:#1f1f1f}
.wrap{padding:56px}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:24px;margin-bottom:36px}
.num{display:inline-block;background:#DA3B64;color:#fff;font-weight:600;font-size:26px;padding:8px 18px;border-radius:8px;margin-bottom:18px}
h1{font-size:62px;line-height:1.08;font-weight:700;letter-spacing:-1px}
.logo{height:46px;margin-top:6px}
.sub{font-size:32px;color:#707070;margin-top:14px;line-height:1.3}
.photo{border-radius:20px;background:#f5f5f5 center/cover no-repeat}
.grid{display:grid;gap:24px}
.card{background:#F7F5F6;border-radius:20px;padding:28px}
.card .pic{height:250px;background:#fff center/contain no-repeat;border-radius:14px;margin-bottom:22px}
.card h3{font-size:36px;font-weight:700;line-height:1.15}
.card p{font-size:28px;color:#5f5f5f;margin-top:8px;line-height:1.3}
.stat{background:#F7F5F6;border-radius:20px;padding:30px 32px}
.stat b{display:block;font-size:64px;font-weight:700;color:#DA3B64;letter-spacing:-1px;line-height:1.05}
.stat span{display:block;font-size:30px;color:#4a4a4a;margin-top:10px;line-height:1.25}
ol{list-style:none;counter-reset:i}
ol li{counter-increment:i;display:flex;align-items:center;gap:26px;font-size:40px;font-weight:600;padding:16px 0;border-bottom:2px solid #f0e6e9}
ol li:last-child{border-bottom:none}
ol li:before{content:counter(i);flex:0 0 64px;height:64px;border-radius:50%;background:#DA3B64;color:#fff;font-size:32px;font-weight:700;display:flex;align-items:center;justify-content:center}
.foot{font-size:24px;color:#999;margin-top:22px}
"""
def head(num, title, sub=''):
    s = f'<p class="sub">{nb(sub)}</p>' if sub else ''
    return f'<div class="head"><div><span class="num">{num}</span><h1>{nb(title)}</h1>{s}</div><img class="logo" src="{logo}"></div>'
pages = {
"01_7-punktov": head("Чек-лист", "7 пунктов перед покупкой посуды") + f"""
<div class="photo" style="height:470px;background-image:url({img('44182/1ypuayqaoy')});background-position:center 70%"></div>
<ol style="margin-top:30px">{''.join(f'<li>{x}</li>' for x in ['Материал корпуса','Толщина дна','Покрытие: название, слои, температура','Совместимость с плитой','Ручка и хранение','Гарантия','Доставка и упаковка'])}</ol>""",
"02_material": head("Пункт 1", "Материал корпуса") + '<div class="grid" style="grid-template-columns:1fr 1fr">' + ''.join(
 f'<div class="card"><div class="pic" style="background-image:url({img(p)})"></div><h3>{nb(t)}</h3><p>{nb(d)}</p></div>' for p,t,d in [
 ('44182/m269m827fc','Кованый алюминий','Лёгкий, быстро нагревается. «Антрацит» 26 см весит 846 г'),
 ('44024/419hrzgt4l','Литой алюминий','Массивнее, дольше держит тепло и форму. «Минерал»'),
 ('44903/ek0ys5tye1','Сталь 18/10','Для тех, кто готовит много и часто. Professional'),
 ('44914/rwgble1qar','Чугун','Со временем образуется естественный антипригарный слой. «Профессионал»')]) + '</div>',
"03_tolshchina-dna": head("Пункт 2", "Толщина дна", "Ищите эту строку в карточке товара: толстое дно прогревается равномерно") + '<div class="grid" style="grid-template-columns:1fr 1fr">' + ''.join(
 f'<div class="card"><div class="pic" style="height:380px;background-image:url({img(p)})"></div><div class="stat" style="padding:0;background:none"><b>{v}</b><span>{nb(d)}</span></div></div>' for p,v,d in [
 ('44036g/2t045590n1','3,3 мм','«Грейстоун», кованый алюминий'),
 ('44903/cq3njxdb3z','5 мм','Professional, капсулированное дно')]) + '</div>',
"04_pokrytie": head("Пункт 3", "Покрытие: что смотреть", "Название, число слоёв и термостойкость. Пример: сковорода Professional") + f"""
<div class="grid" style="grid-template-columns:1fr 1fr;align-items:stretch">
<div class="photo" style="background:#fff url({img('44903/ek0ys5tye1')}) center/contain no-repeat;border:2px solid #f0e6e9"></div>
<div class="grid">
<div class="stat"><b>3 слоя</b><span>покрытие ILAG®</span></div>
<div class="stat"><b>до 260 °C</b><span>термостойкость покрытия</span></div>
<div class="stat"><b>до 5 000</b><span>циклов истирания</span></div>
<div class="stat"><b>Без ПФОК</b><span>(PFOA) в покрытии</span></div>
</div></div>""",
"05_plita-ruchka": head("Пункты 4 и 5", "Плита и ручка", "Пример: сковорода «Минерал» 28 см") + f"""
<div class="photo" style="height:430px;background-image:url({img('44024/6zedo8pakj')});background-position:center 45%"></div>
<div class="grid" style="grid-template-columns:1fr 1fr 1fr;margin-top:24px">
<div class="stat"><b style="font-size:46px">Все плиты</b><span>включая индукционные</span></div>
<div class="stat"><b style="font-size:46px">20,3 см</b><span>диаметр дна: конфорка не шире</span></div>
<div class="stat"><b style="font-size:46px">Съёмная</b><span>ручка: можно в духовку</span></div>
</div>""",
"06_garantiya-dostavka": head("Пункты 6 и 7", "Гарантия и доставка") + f"""
<div class="photo" style="height:430px;background-image:url({img('44903/4ug718lrom')});background-position:center 40%"></div>
<div class="grid" style="grid-template-columns:1fr 1fr 1fr;margin-top:24px">
<div class="stat"><b style="font-size:46px">2 года</b><span>гарантии на посуду TalleR</span></div>
<div class="stat"><b style="font-size:46px">Осмотр</b><span>заказа до оплаты</span></div>
<div class="stat"><b style="font-size:46px">от 2 500 ₽</b><span>бесплатная доставка*</span></div>
</div><p class="foot">* В дальние регионы доставка может быть платной. Условия на taller.ru</p>""",
}
for name, body in pages.items():
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="wrap">{body}</div></body></html>'
    p = pathlib.Path(f'{S}/{name}.html'); p.write_text(html)
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:800}}}});await pg.goto('file://{p}');await pg.waitForTimeout(300);await pg.screenshot({{path:'{D}/{name}.png',fullPage:true}});await b.close();}})();"
    subprocess.run(['node','-e',js],check=True)
print('ok')
