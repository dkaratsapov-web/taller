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
.sub{font-size:32px;color:#707070;margin-top:4px;line-height:1.3}
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
    return f'<div class="head"><div><span class="num">{num}</span>{s}</div><img class="logo" src="{logo}"></div>'
pages = {
"01_o-brende": head("О бренде", "") + f"""
<div class="photo" style="height:520px;background-image:url({img('44903/33intkhci6')});background-position:center 55%"></div>
<div class="grid" style="grid-template-columns:1fr 1fr 1fr;margin-top:24px">
<div class="stat"><b style="font-size:50px">с 2006</b><span>года на российском рынке</span></div>
<div class="stat"><b style="font-size:50px">6 стран</b><span>Россия, Беларусь, Казахстан, Армения, Кыргызстан, Абхазия</span></div>
<div class="stat"><b style="font-size:50px">Петербург</b><span>компания и основной склад</span></div>
</div>""",
"02_materialy": head("Материалы", "", "Три сковороды TalleR: корпус, дно и покрытие") + '<div class="grid" style="grid-template-columns:1fr 1fr 1fr;gap:20px">' + ''.join(
 f'<div class="card" style="padding:22px"><div class="pic" style="height:230px;background-image:url({img(p)})"></div><h3 style="font-size:32px">{nb(t)}</h3>' + ''.join(f'<p style="font-size:25px;margin-top:10px"><b style="color:#1f1f1f">{k}:</b> {nb(v)}</p>' for k,v in rows) + '</div>' for p,t,rows in [
 ('44036g/0n21hm83cz','«Грейстоун»',[('Корпус','кованый алюминий'),('Дно','3,3 мм'),('Покрытие','трёхслойное MULTISTONE®')]),
 ('44024/419hrzgt4l','«Минерал»',[('Корпус','литой алюминий'),('Дно','4,8 мм'),('Покрытие','двухслойное XYLAN®, до 260 °C')]),
 ('44903/ek0ys5tye1','Professional',[('Корпус','сталь 18/10'),('Дно','5 мм, капсулированное'),('Покрытие','трёхслойное ILAG®, до 5 000 циклов истирания')])]) + '</div>',
"03_kollekcii": head("Коллекции сковород", "") + '<div class="grid" style="grid-template-columns:1fr 1fr 1fr;gap:20px">' + ''.join(
 f'<div class="card" style="padding:20px"><div class="pic" style="height:210px;background-image:url({img(p)})"></div><h3 style="font-size:31px">{nb(t)}</h3><p style="font-size:24px">{nb(d)}</p></div>' for p,t,d in [
 ('44182/m269m827fc','«Антрацит»','Усиленное трёхслойное покрытие для ежедневной готовки'),
 ('44024/419hrzgt4l','«Минерал»','Съёмная ручка: можно ставить в духовку'),
 ('44105/6lz33bhv1z','«Хюгге»','Съёмная ручка и компактное хранение'),
 ('44122/r9xyn29tk4','«Сканди»','Глубокие сковороды с крышкой'),
 ('44903/ek0ys5tye1','Professional','Нержавеющая сталь и антипригарное покрытие'),
 ('44914/rwgble1qar','«Профессионал»','Чугунная серия, есть вок с крышкой')]) + '</div>',
"04_detali": head("Детали", "") + '<div class="grid" style="grid-template-columns:1fr 1fr">' + ''.join(
 f'<div class="card"><div class="pic" style="height:270px;background:#fff url({img(p)}) {pos}/{fit} no-repeat"></div><h3>{nb(t)}</h3><p>{nb(d)}</p></div>' for p,fit,pos,t,d in [
 ('44142/5cf9cn9x8u','contain','center','Индикатор нагрева','Подсказывает, что сковорода прогрелась'),
 ('44105/jzgupac3qh','cover','center 40%','Съёмная ручка','Сковорода уходит с плиты в духовку, потом в ящик'),
 ('44036g/0n21hm83cz','contain','center','Бакелитовая ручка','С бархатистой отделкой, не нагревается, если конфорка не шире дна'),
 ('44182/m269m827fc','contain','center','Индукция','«Антрацит», «Грейстоун» и «Минерал» подходят для всех плит')]) + '</div>',
"05_servis": head("После заказа", "") + f"""
<div class="photo" style="height:420px;background:#fff url({img('44122/srl0fq5g4r')}) center 45%/cover no-repeat"></div>
<div class="grid" style="grid-template-columns:1fr 1fr 1fr;margin-top:24px;gap:20px">
<div class="stat"><b style="font-size:44px">Новые</b><span>товары с основного склада в Петербурге</span></div>
<div class="stat"><b style="font-size:44px">Единые</b><span>цены во всех каналах продаж</span></div>
<div class="stat"><b style="font-size:44px">от 2 500 ₽</b><span>бесплатная доставка*</span></div>
<div class="stat"><b style="font-size:44px">Осмотр</b><span>заказа до оплаты</span></div>
<div class="stat"><b style="font-size:44px">2 года</b><span>гарантии на посуду TalleR</span></div>
<div class="stat"><b style="font-size:44px">менее 0,2%</b><span>возвратов из-за производственных дефектов**</span></div>
</div><p class="foot">* В дальние регионы доставка может быть платной. ** По данным интернет-магазина TalleR. Условия на taller.ru</p>""",
"06_otzyvy": head("Отзывы покупателей", "", "С сайта taller.ru") + f"""
<div class="photo" style="height:420px;background-image:url({img('11071/gavfsqg9x9')});background-position:center 55%"></div>
<div class="grid" style="margin-top:24px;gap:20px">
<div class="card" style="border-left:8px solid #DA3B64"><p style="font-size:32px;color:#1f1f1f;line-height:1.35;margin:0">«Сегодня получили набор кастрюль Льюис. Всё отлично, начиная от скорости доставки и упаковки до качества самого товара»</p></div>
<div class="card" style="border-left:8px solid #DA3B64"><p style="font-size:32px;color:#1f1f1f;line-height:1.35;margin:0">«Доставили заказ в срок, упаковано отлично. Посуда пришла без повреждений. Красивый дизайн»</p></div>
</div><p class="foot">На фото набор посуды «Льюис», 9 предметов</p>""",
}
for name, body in pages.items():
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="wrap">{body}</div></body></html>'
    p = pathlib.Path(f'{S}/{name}.html'); p.write_text(html)
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1080,height:800}}}});await pg.goto('file://{p}');await pg.waitForTimeout(300);await pg.screenshot({{path:'{D}/{name}.png',fullPage:true}});await b.close();}})();"
    subprocess.run(['node','-e',js],check=True)
print('ok')
