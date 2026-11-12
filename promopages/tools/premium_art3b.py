import sys; sys.path.insert(0, sys.argv[1] + '/scripts')
from premium_lib import *
S, R, D = sys.argv[1], sys.argv[2], sys.argv[3]
k = Kit(S, R)
pages = {
"00_vstuplenie": k.top('') + k.photo('44113/b31cd6q1vz', 760, 'center 55%')
  + '<div style="height:28px"></div>' + foot('На фото сковороды TalleR «Урбан»'),
"01_kazhdyy-den": k.top('') + products(k, [
  ('44182/m269m827fc','«Антрацит»','Диаметры 20, 24, 26 и 28 см'),
  ('44904/atfyrtkww5','Professional','Матовая полировка корпуса, ручка на клёпках')], pic=420, name=56),
"02_duhovka": k.top('') + k.photo('44105/ek0cfguyby', 600, 'center 55%')
  + figures([('Молочный','и коричневый: цвета серии «Хюгге»'),('Чёрный','и красный: цвета серии «Минерал»')], size=80)
  + foot('На фото сковорода «Хюгге» в духовке'),
"03_indikator": k.top('') + k.photo('crop/mryk_crop', 600, 'center 40%')
  + figures([('20,4 см','диаметр дна у сковороды 26 см'),('3,5 мм','толщина её дна')], size=88)
  + foot('На фото сковорода TalleR с индикатором нагрева'),
"04_semya": k.top('') + k.photo('44091/ven810rdr3', 600, 'center 55%')
  + figures([('21 см','диаметр дна «Эмили» 26 см'),('2,8 мм','толщина стенок «Грейси»'),('3 мм','толщина дна «Комфорта»')], size=80)
  + foot('На фото сковорода «Грейси»'),
"05_bliny": k.top('') + k.photo('44169/td1nxu2iek', 540, 'center', 'contain')
  + figures([('18,8 см','диаметр дна блинной сковороды 22 см'),('2,5 мм','толщина стенок'),('Бакелит','ручка с бархатистой отделкой')], size=76),
"06_chugun": k.top('') + k.photo('44915/gjdzoqjgu3', 560, 'center', 'contain')
  + figures([('3,3 л','объём чугунного вока 28 см'),('2,8 мм','толщина дна вока'),('17 см','диаметр дна сковороды 26 см')], size=80)
  + foot('На фото чугунная серия «Профессионал»'),
"07_vok": k.top('') + k.photo('44199/jp4nai4lvi', 560, 'center', 'contain')
  + figures([('Казан','такую форму напоминает корпус'),('Клёпки','крепление ручек из нержавеющей стали'),('17,5 см','диаметр дна')], size=80)
  + foot('На фото вок «Итан» 30 см'),
}
for name, body in pages.items(): k.render(body, f'{D}/{name}.png')
print('ok')
