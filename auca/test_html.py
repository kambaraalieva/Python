from bs4 import BeautifulSoup

# Your HTML
wiki = '''<div id="main-tfa" class="main-block main-box main-box-responsive-image"><style data-mw-deduplicate="TemplateStyles:r142962676">.mw-parser-output .fake-heading{color:var(--color-emphasized,#000000);background:none;margin:0;overflow:hidden;padding-bottom:0.17em;page-break-after:avoid;padding-top:0.5em}.mw-parser-output .fake-heading.h1,.mw-parser-output .fake-heading.h2{border-bottom:1px solid var(--border-color-base,#a2a9b1);margin-bottom:0.25em;margin-top:1em;padding:0;font-family:"Linux Libertine","Georgia","Times","Source Serif Pro",serif;line-height:1.375}body.skin-monobook .mw-parser-output .fake-heading.h1,body.skin-monobook .mw-parser-output .fake-heading.h2{font-family:inherit;line-height:inherit}body.skin-timeless .mw-parser-output .fake-heading.h1,body.skin-timeless .mw-parser-output .fake-heading.h2{border-bottom:3px solid var(--border-color-subtle,#c8ccd1)}.mw-parser-output .fake-heading.h1{font-size:1.8em}body.skin-timeless .mw-parser-output .fake-heading.h1{font-size:2em}.mw-parser-output .fake-heading.h2{font-size:1.5em}body.skin-timeless .mw-parser-output .fake-heading.h2{font-size:1.8em}.mw-parser-output .fake-heading.h3,.mw-parser-output .fake-heading.h4,.mw-parser-output .fake-heading.h5,.mw-parser-output .fake-heading.h6{font-weight:bold;margin-top:0.3em;margin-bottom:0;padding-bottom:0;line-height:1.6}.mw-parser-output .fake-heading.h3{font-size:1.2em}.mw-parser-output .fake-heading.h4{font-size:100%}.mw-parser-output .fake-heading.in-frame{margin-top:0;padding-top:0}</style>
<h2 id="Избранная_статья_Файф-о-клок" class="main-box-header mw-html-heading"><span id=".D0.98.D0.B7.D0.B1.D1.80.D0.B0.D0.BD.D0.BD.D0.B0.D1.8F_.D1.81.D1.82.D0.B0.D1.82.D1.8C.D1.8F_.D0.A4.D0.B0.D0.B9.D1.84-.D0.BE-.D0.BA.D0.BB.D0.BE.D0.BA"></span><div class="main-box-subtitle">Избранная статья </div><div class="fake-heading h2 main-header"><a href="/wiki/%D0%A4%D0%B0%D0%B9%D1%84-%D0%BE-%D0%BA%D0%BB%D0%BE%D0%BA" title="Файф-о-клок">Файф-о-клок</a></div>
</h2>
<div class="main-box-content">
<figure class="mw-halign-right" typeof="mw:File"><a href="https://commons.wikimedia.org/wiki/File:David_Comba_Adamson_(1859-1926)_-_Five_o%27Clock_Tea_-_10-1926_-_Dundee_Art_Galleries_and_Museums.jpg?uselang=ru" class="mw-file-description" title="«Five o’clock tea», картина шотландского художника Дэвида Комба Адамсона, холст, масло, 1884—1898"><img alt="«Five o’clock tea», картина шотландского художника Дэвида Комба Адамсона, холст, масло, 1884—1898" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/17/David_Comba_Adamson_%281859-1926%29_-_Five_o%27Clock_Tea_-_10-1926_-_Dundee_Art_Galleries_and_Museums.jpg/250px-David_Comba_Adamson_%281859-1926%29_-_Five_o%27Clock_Tea_-_10-1926_-_Dundee_Art_Galleries_and_Museums.jpg" decoding="async" width="200" height="156" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/17/David_Comba_Adamson_%281859-1926%29_-_Five_o%27Clock_Tea_-_10-1926_-_Dundee_Art_Galleries_and_Museums.jpg/330px-David_Comba_Adamson_%281859-1926%29_-_Five_o%27Clock_Tea_-_10-1926_-_Dundee_Art_Galleries_and_Museums.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/17/David_Comba_Adamson_%281859-1926%29_-_Five_o%27Clock_Tea_-_10-1926_-_Dundee_Art_Galleries_and_Museums.jpg/500px-David_Comba_Adamson_%281859-1926%29_-_Five_o%27Clock_Tea_-_10-1926_-_Dundee_Art_Galleries_and_Museums.jpg 2x" data-file-width="1200" data-file-height="938"></a><figcaption>«Five o’clock tea», картина шотландского художника Дэвида Комба Адамсона, холст, масло, 1884—1898</figcaption></figure>
<p><b><a href="/wiki/%D0%A4%D0%B0%D0%B9%D1%84-%D0%BE-%D0%BA%D0%BB%D0%BE%D0%BA" title="Файф-о-клок">Файф-о-клок</a></b> (<a href="/wiki/%D0%90%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9_%D1%8F%D0%B7%D1%8B%D0%BA" title="Английский язык">англ.</a>&nbsp;<span lang="en" style="font-style:italic;">five o’clock tea</span>, то есть <i>пятичасовой чай</i>; также <i>afternoon tea</i>)&nbsp;— традиционный британский ритуал приёма пищи, возникший в <a href="/wiki/%D0%92%D0%B5%D0%BB%D0%B8%D0%BA%D0%BE%D0%B1%D1%80%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D1%8F" title="Великобритания">Великобритании</a> в <a href="/wiki/XIX_%D0%B2%D0%B5%D0%BA" title="XIX век">XIX&nbsp;веке</a>, обычно состоящий из чая, <a href="/wiki/%D0%A1%D1%8D%D0%BD%D0%B4%D0%B2%D0%B8%D1%87" title="Сэндвич">сэндвичей</a>, <a href="/wiki/%D0%A1%D0%BA%D0%BE%D0%BD" title="Скон">сконов</a> с <a href="/wiki/%D0%A2%D0%BE%D0%BF%D0%BB%D1%91%D0%BD%D1%8B%D0%B5_%D1%81%D0%BB%D0%B8%D0%B2%D0%BA%D0%B8" title="Топлёные сливки">топлёными сливками</a> и <a href="/wiki/%D0%94%D0%B6%D0%B5%D0%BC" class="mw-redirect" title="Джем">джемом</a>, а также различной выпечки. Является культурным феноменом, ассоциируемым с <a href="/wiki/%D0%9A%D1%83%D0%BB%D1%8C%D1%82%D1%83%D1%80%D0%B0_%D0%90%D0%BD%D0%B3%D0%BB%D0%B8%D0%B8" title="Культура Англии">английской культурой</a>, спокойным и размеренным образом жизни, определённым <a href="/wiki/%D0%AD%D1%82%D0%B8%D0%BA%D0%B5%D1%82" title="Этикет">этикетом</a>. Несмотря на название, время его проведения может варьироваться, но исторически сложилось, что оно приходится на середину дня, между обедом и ужином, чаще всего около 16:00 или 17:00. 
</p><p>Возникший изначально в гостиных английской аристократии как камерная непринуждённая беседа нескольких женщин за чашкой чая, со временем файф-о-клок распространился на другие социальные слои и приобрёл другие формы. Обычай был популяризован <a href="/wiki/%D0%A0%D0%B0%D1%81%D1%81%D0%B5%D0%BB,_%D0%90%D0%BD%D0%BD%D0%B0,_%D0%B3%D0%B5%D1%80%D1%86%D0%BE%D0%B3%D0%B8%D0%BD%D1%8F_%D0%91%D0%B5%D0%B4%D1%84%D0%BE%D1%80%D0%B4" title="Рассел, Анна, герцогиня Бедфорд">Анной Рассел</a>, седьмой герцогиней <a href="/wiki/%D0%93%D0%B5%D1%80%D1%86%D0%BE%D0%B3_%D0%91%D0%B5%D0%B4%D1%84%D0%BE%D1%80%D0%B4" title="Герцог Бедфорд">Бедфордской</a>, примерно в 1840 году, когда она начала приглашать друзей присоединиться к ней за лёгкой трапезой, чтобы облегчить «тягостное ощущение» голода в конце дня — время, на которое повлияли изменившиеся графики приёмов пищи в эпоху индустриализации и урбанизации Англии. Важной особенностью файф-о-клока является неформальная, расслабленная, дружеская и приятная атмосфера, сопровождаемая лёгкой и непринуждённой беседой всех участников. На такое чаепитие приходят в «повседневном» настроении, чтобы повидаться с друзьями.
</p>
</div>
<div class="main-footer"><div class="main-footer-actions main-plainlist">
<ul><li><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r137875209"><span class="main-cdx-button-link"><a href="/wiki/%D0%A4%D0%B0%D0%B9%D1%84-%D0%BE-%D0%BA%D0%BB%D0%BE%D0%BA" title="Файф-о-клок">Читать</a></span></li>
<li><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r137875209"><span class="main-cdx-button-link is-quiet"><a href="/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F:%D0%98%D0%B7%D0%B1%D1%80%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5_%D1%81%D1%82%D0%B0%D1%82%D1%8C%D0%B8" title="Википедия:Избранные статьи">Все 2093 избранные статьи</a></span></li></ul>
</div><div class="main-footer-menu group-user-show mw-collapsible mw-collapsed mw-made-collapsible">
<div class="main-footer-menuToggle skin-invert" title="Дополнительные действия"><span typeof="mw:File"><span><img alt="Доп. действия" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b3/OOjs_UI_icon_ellipsis.svg/20px-OOjs_UI_icon_ellipsis.svg.png" decoding="async" width="20" height="20" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b3/OOjs_UI_icon_ellipsis.svg/40px-OOjs_UI_icon_ellipsis.svg.png 1.5x" data-file-width="20" data-file-height="20"></span></span><button type="button" class="mw-collapsible-toggle mw-collapsible-toggle-default mw-collapsible-toggle-collapsed" aria-expanded="false" tabindex="0"><span class="mw-collapsible-text">показать</span></button></div>
<div class="main-footer-menuDropdown mw-collapsible-content main-plainlist" hidden="until-found">
<ul><li><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r137875209"><span class="main-cdx-button-link is-quiet"><a href="/wiki/%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%82:%D0%98%D0%B7%D0%B1%D1%80%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5_%D1%81%D1%82%D0%B0%D1%82%D1%8C%D0%B8/%D0%9A%D0%B0%D0%BD%D0%B4%D0%B8%D0%B4%D0%B0%D1%82%D1%8B" title="Проект:Избранные статьи/Кандидаты">Кандидаты</a></span></li>
<li><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r137875209"><span class="main-cdx-button-link is-quiet"><a href="/wiki/%D0%A8%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD:%D0%A2%D0%B5%D0%BA%D1%83%D1%89%D0%B0%D1%8F_%D0%B8%D0%B7%D0%B1%D1%80%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D0%B0%D1%82%D1%8C%D1%8F" title="Шаблон:Текущая избранная статья">Просмотр шаблона</a></span></li></ul>
</div></div></div>
</div>'''

# Create BeautifulSoup object
soup = BeautifulSoup(wiki, 'html.parser')

# Extract all paragraph texts
paragraphs = soup.find('div', class_='main-box-content').find_all('p')
all_text = [p.get_text(strip=True) for p in paragraphs]

# Extract all links inside paragraphs safely
url_dict = {}
for p in paragraphs:
    for a in p.find_all('a'):
        href = a.get('href')
        if href:  # Only store links that have href
            text = a.get_text(strip=True)
            # Handle duplicate link texts by storing a list
            if text in url_dict:
                if isinstance(url_dict[text], list):
                    url_dict[text].append(href)
                else:
                    url_dict[text] = [url_dict[text], href]
            else:
                url_dict[text] = href

# Output
print("Paragraphs:")
for i, para in enumerate(all_text, start=1):
    print(f"Paragraph {i}:\n{para}\n")

print("Links:")
for text, href in url_dict.items():
    print(f"{text}: {href}")
