"""Делает из md-статьи текст для вставки в редактор Промостраниц."""
import re, sys
src, out, title, folder = sys.argv[1:5]
s = open(src).read()
heads = re.search(r'## Заголовки.*?\n\n(.*?)\n\n## ', s, re.S).group(1)
desc = re.search(r'## Описание.*?\n\n(.*?)\n', s, re.S).group(1)
m = re.search(r'## Текст статьи\n\n(.*?)\n\*\*Scroll2Site, текст кнопки:\*\* (.*?)\n', s, re.S)
text, cta = m.group(1), m.group(2)
text = re.sub(r'\[ИЛЛЮСТРАЦИЯ: [^\]]*/([^/\]]+)\]', r'[Картинка: \1]', text)
text = re.sub(r'\[ССЫЛК[АИ] → ([^\]]+)\]', lambda m: '[Ссылки: ' + m.group(1).replace(' · ', '; ') + ']', text)
text = re.sub(r'\n\|.*?\n\n', '\n', text, flags=re.S)
text = text.replace('### ', '').replace('**', '')
text = re.sub(r'^> ', '', text, flags=re.M)
open(out, 'w').write(f"""TalleR × Яндекс Промостраницы
{title}

ЗАГОЛОВКИ (до 56 знаков)
{heads}

ОПИСАНИЕ (до 81 знака)
{desc}

ТЕКСТ СТАТЬИ
Подзаголовки оформите в редакторе как H2. Метки [Картинка: …] показывают, куда вставить иллюстрацию из папки {folder}/v-tekst/. Метки [Ссылки: …] показывают, на какие слова поставить ссылку.

{text.strip()}

КНОПКА SCROLL2SITE
{cta}

ОБЛОЖКИ
Папка {folder}/oblozhki/: для каждого сюжета мобильная 1080×1080 и десктопная 1600×800.
""")
