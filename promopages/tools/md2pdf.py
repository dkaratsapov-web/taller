import sys, re, pathlib, markdown, subprocess, html
src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2])
md = src.read_text()
# стилизуем служебные пометки
md = re.sub(r'^\[(ССЫЛК[АИ][^\]]*)\]\s*$', lambda m: '<p class="note link">🔗 ' + html.escape(m.group(1)) + '</p>', md, flags=re.M)
md = re.sub(r'^\[(ФОТО[^\]]*)\]\s*$', lambda m: '<p class="note photo">🖼 ' + html.escape(m.group(1)) + '</p>', md, flags=re.M)
md = re.sub(r'^\[ИЛЛЮСТРАЦИЯ: ([^\]]+)\]\s*$', lambda m: '<p class="ill"><img src="file://' + str((src.parent/m.group(1)).resolve()) + '"><br><span>Иллюстрация: ' + m.group(1).split('/')[-1] + '</span></p>', md, flags=re.M)
body = markdown.markdown(md, extensions=['tables', 'sane_lists'])
body = re.sub(r'(https://[^\s<"·]+)', r'<a href="\1">\1</a>', body)
css = """
@page { size: A4; margin: 18mm 18mm 20mm; }
body { font-family: Inter, 'DejaVu Sans', sans-serif; font-size: 10.5pt; line-height: 1.55; color: #222; }
h1 { font-size: 17pt; line-height: 1.25; color: #DA3B64; margin: 0 0 10pt; }
h2 { font-size: 13pt; margin: 18pt 0 6pt; padding-bottom: 3pt; border-bottom: 1.5pt solid #DA3B64; }
h3 { font-size: 11.5pt; margin: 14pt 0 4pt; }
p { margin: 0 0 7pt; } li { margin-bottom: 3pt; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 10pt; font-size: 9.5pt; }
th, td { border: 0.6pt solid #ccc; padding: 4pt 6pt; text-align: left; vertical-align: top; }
th { background: #f6e3e8; }
blockquote { margin: 6pt 0; padding: 6pt 10pt; background: #f7f7f7; border-left: 3pt solid #DA3B64; font-style: italic; }
blockquote p { margin: 0; }
.note { font-size: 9pt; padding: 4pt 8pt; border-radius: 4pt; margin: 4pt 0 8pt; word-break: break-all; }
.link { background: #eef4fb; color: #1d4f86; } .photo { background: #fdf3e2; color: #8a5a00; }
a { color: #1d4f86; text-decoration: none; word-break: break-all; }
.ill { text-align:center; margin: 8pt 0 12pt; page-break-inside: avoid; } .ill img { width: 62%; border: 0.6pt solid #ddd; border-radius: 6pt; } .ill span { font-size: 8.5pt; color: #999; }
hr { border: none; border-top: 1pt dashed #bbb; margin: 18pt 0; page-break-after: always; }
"""
doc = f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'
tmp = out.with_suffix('.html'); tmp.write_text(doc)
js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://{tmp.resolve()}');await p.pdf({{path:'{out.resolve()}',format:'A4',printBackground:true,
displayHeaderFooter:true,headerTemplate:'<div></div>',footerTemplate:'<div style="font-size:8px;width:100%;text-align:center;color:#999;font-family:Inter">TalleR × Яндекс Промостраницы · черновик · стр. <span class=pageNumber></span>/<span class=totalPages></span></div>',
margin:{{top:'18mm',bottom:'20mm',left:'18mm',right:'18mm'}}}});await b.close();}})();"""
subprocess.run(['node', '-e', js], check=True)
tmp.unlink()
