# -*- coding: utf-8 -*-
"""Генератор демо-лендингов из шаблона (стиль Шинсервис40, свой акцент на компанию)."""
import os, json

BASE = os.path.join(os.path.expanduser("~"), "Desktop", "SiteRedesign", "demos")

TEMPLATE = """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{meta_desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Russo+One&family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
:root{{--asphalt:#17191C;--asphalt2:#22252A;--line:{accent};--line-dark:{accent_dark};
--bg:#F2F3F5;--card:#FFFFFF;--steel:#5A6270;--ink:#1B1D21;--radius:14px}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{font-family:'Manrope',system-ui,sans-serif;background:var(--bg);color:var(--ink);line-height:1.55}}
.wrap{{max-width:1060px;margin:0 auto;padding:0 20px}}
h1,h2,.display{{font-family:'Russo One',sans-serif;font-weight:400;line-height:1.15}}
header{{position:sticky;top:0;z-index:50;background:var(--asphalt);border-bottom:3px solid var(--line)}}
.hrow{{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px 0}}
.logo{{color:#fff;font-family:'Russo One',sans-serif;font-size:19px;letter-spacing:.5px;text-decoration:none}}
.logo span{{color:var(--line)}}
.hphone{{display:inline-flex;align-items:center;gap:8px;background:var(--line);color:var(--asphalt);text-decoration:none;
font-weight:800;padding:10px 16px;border-radius:10px;font-size:15px;white-space:nowrap;transition:transform .15s}}
.hphone:hover{{transform:translateY(-1px);background:var(--line-dark)}}
.hero{{background:var(--asphalt);color:#fff;position:relative;overflow:hidden;padding:64px 0 330px}}
@media (min-width:1040px){{.hero{{padding-bottom:150px}}}}
.hero::after{{content:"";position:absolute;left:0;right:0;bottom:0;height:96px;
background:repeating-linear-gradient(90deg, var(--line) 0 64px, transparent 64px 128px) center 46px/128px 10px no-repeat border-box,
linear-gradient(180deg,#101215,#0B0C0E);background-repeat:repeat-x}}
.hero .wrap{{position:relative;z-index:2}}
.wheel{{position:absolute;z-index:2;bottom:36px;left:50%;transform:translateX(-50%);line-height:0}}
.wheel svg{{width:min(210px,54vw);height:auto}}
.wheel::after{{content:"";position:absolute;left:50%;bottom:-7px;transform:translateX(-50%);
width:78%;height:20px;border-radius:50%;background:radial-gradient(ellipse at center, rgba(0,0,0,.6), transparent 68%)}}
.roll{{transform-box:fill-box;transform-origin:center;animation:spin 14s linear infinite}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
@media (prefers-reduced-motion: reduce){{.roll{{animation:none}}}}
@media (min-width:1040px){{.wheel{{left:auto;right:6%;transform:none}}.wheel svg{{width:min(330px,28vw)}}}}
.eyebrow{{display:inline-flex;align-items:center;gap:10px;color:var(--line);font-weight:700;font-size:13px;
letter-spacing:.14em;text-transform:uppercase;margin-bottom:18px}}
.eyebrow::before{{content:"";width:34px;height:4px;background:var(--line)}}
.hero h1{{font-size:clamp(30px,5.4vw,52px);max-width:17ch}}
.hero p.sub{{margin:18px 0 28px;font-size:clamp(16px,2.2vw,19px);color:#C6CBD4;max-width:52ch}}
.ratebox{{display:inline-flex;align-items:center;gap:14px;background:var(--asphalt2);border:1px solid #33373E;
border-radius:var(--radius);padding:14px 18px;margin-bottom:30px}}
.ratebox .score{{font-family:'Russo One',sans-serif;font-size:34px;color:var(--line)}}
.stars{{color:var(--line);letter-spacing:2px;font-size:15px}}
.ratebox small{{display:block;color:#9AA1AC;font-size:13px;margin-top:2px}}
.ratebox a{{color:#C6CBD4}}
.cta-row{{display:flex;flex-wrap:wrap;gap:14px}}
.btn{{display:inline-flex;align-items:center;gap:10px;text-decoration:none;font-weight:800;font-size:17px;
padding:16px 28px;border-radius:12px;transition:transform .15s}}
.btn:active{{transform:scale(.98)}}
.btn-main{{background:var(--line);color:var(--asphalt)}}
.btn-main:hover{{background:var(--line-dark)}}
.btn-ghost{{border:2px solid #3A3E45;color:#fff}}
.btn-ghost:hover{{border-color:var(--line);color:var(--line)}}
.hours-hero{{margin-top:26px;color:#9AA1AC;font-size:14px}}
.hours-hero b{{color:#fff}}
section{{padding:64px 0}}
.sec-head{{margin-bottom:34px}}
.sec-head h2{{font-size:clamp(24px,3.4vw,34px)}}
.sec-head .eyebrow{{color:var(--steel)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px}}
.svc{{background:var(--card);border-radius:var(--radius);padding:24px;border-top:4px solid var(--line);
box-shadow:0 1px 3px rgba(23,25,28,.07)}}
.svc h3{{font-size:17px;margin-bottom:8px}}
.svc p{{color:var(--steel);font-size:14.5px;margin-bottom:14px}}
.svc .price{{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:16px}}
.svc .price small{{color:var(--steel);font-weight:500;font-family:'Manrope',sans-serif}}
.why .grid{{grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}}
.why-item{{padding:22px;background:var(--card);border-radius:var(--radius);box-shadow:0 1px 3px rgba(23,25,28,.07)}}
.why-item .display{{font-size:24px;color:var(--asphalt);margin-bottom:6px}}
.why-item .display em{{font-style:normal;color:var(--line-dark)}}
.why-item p{{color:var(--steel);font-size:14.5px}}
.reviews{{background:var(--asphalt);color:#fff}}
.reviews .sec-head h2{{color:#fff}}
.reviews .eyebrow{{color:#9AA1AC}}
.rev{{background:var(--asphalt2);border:1px solid #33373E;border-radius:var(--radius);padding:22px;display:flex;flex-direction:column;gap:12px}}
.rev p{{color:#D7DBE1;font-size:14.5px;flex:1}}
.rev .who{{display:flex;align-items:center;justify-content:space-between;font-weight:700;font-size:14px}}
.rev .who .stars{{font-size:13px}}
.rev-src{{margin-top:22px;font-size:14px;color:#9AA1AC}}
.rev-src a{{color:var(--line)}}
.contact .card{{background:var(--card);border-radius:var(--radius);padding:30px;box-shadow:0 1px 3px rgba(23,25,28,.07);
display:grid;grid-template-columns:1fr 1fr;gap:28px}}
.contact dt{{font-size:12.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--steel);margin-bottom:5px}}
.contact dd{{font-size:17px;font-weight:600;margin-bottom:20px}}
.contact dd a{{color:var(--ink);text-decoration:none}}
.contact dd a:hover{{color:var(--line-dark)}}
footer{{background:var(--asphalt);color:#9AA1AC;padding:26px 0;font-size:13px;border-top:3px solid var(--line)}}
footer .wrap{{display:flex;flex-wrap:wrap;gap:10px;justify-content:space-between;align-items:center}}
.demo-badge{{border:1px dashed #4A4F57;border-radius:8px;padding:6px 12px}}
.fab{{display:none;position:fixed;right:16px;bottom:16px;z-index:60;background:var(--line);color:var(--asphalt);
border-radius:50%;width:60px;height:60px;align-items:center;justify-content:center;font-size:26px;text-decoration:none;
box-shadow:0 6px 20px rgba(0,0,0,.3)}}
.reveal{{opacity:0;transform:translateY(18px);transition:opacity .5s,transform .5s}}
.reveal.on{{opacity:1;transform:none}}
@media (prefers-reduced-motion: reduce){{.reveal{{opacity:1;transform:none;transition:none}}html{{scroll-behavior:auto}}}}
a:focus-visible,.btn:focus-visible{{outline:3px solid var(--line);outline-offset:2px}}
@media (max-width:640px){{.hero{{padding:44px 0 310px}}.contact .card{{grid-template-columns:1fr}}
.fab{{display:flex}}.hphone .txt{{display:none}}.hphone{{padding:10px 12px}}}}
</style>
</head>
<body>
<header><div class="wrap hrow">
<a class="logo" href="#">{logo_html}</a>
<a class="hphone" href="tel:{tel_main}">📞 <span class="txt">{tel_main_fmt}</span></a>
</div></header>

<section class="hero">
  <div class="wrap">
    <div class="eyebrow">{eyebrow}</div>
    <h1>{headline}</h1>
    <p class="sub">{sub}</p>
    {ratebox}
    <div class="cta-row">
      <a class="btn btn-main" href="tel:{tel_main}">{cta}</a>
      <a class="btn btn-ghost" href="#services">Услуги</a>
    </div>
    {hours_hero}
  </div>
  <div class="wheel" aria-hidden="true">
    <svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
      <g class="roll">
        <circle cx="200" cy="200" r="176" fill="none" stroke="#2E3238" stroke-width="34" stroke-dasharray="20 12"/>
        <circle cx="200" cy="200" r="158" fill="#101215"/>
        <circle cx="200" cy="200" r="158" fill="none" stroke="#22252A" stroke-width="6"/>
        <circle cx="200" cy="200" r="106" fill="#22252A" stroke="#3A3E45" stroke-width="4"/>
        <g fill="#2E3238" stroke="#454A52" stroke-width="2">
          <g transform="rotate(0 200 200)"><rect x="188" y="108" width="24" height="80" rx="10"/></g>
          <g transform="rotate(72 200 200)"><rect x="188" y="108" width="24" height="80" rx="10"/></g>
          <g transform="rotate(144 200 200)"><rect x="188" y="108" width="24" height="80" rx="10"/></g>
          <g transform="rotate(216 200 200)"><rect x="188" y="108" width="24" height="80" rx="10"/></g>
          <g transform="rotate(288 200 200)"><rect x="188" y="108" width="24" height="80" rx="10"/></g>
        </g>
        <g fill="#5A6270">
          <circle cx="200" cy="156" r="7"/><circle cx="242" cy="187" r="7"/>
          <circle cx="226" cy="236" r="7"/><circle cx="174" cy="236" r="7"/>
          <circle cx="158" cy="187" r="7"/>
        </g>
      </g>
      <path d="M 200 200 m 0 -128 a 128 128 0 0 1 88 34" fill="none" stroke="{accent}" stroke-width="26" stroke-linecap="round"/>
      <circle cx="200" cy="200" r="34" fill="{accent}"/>
      <text x="200" y="211" text-anchor="middle" font-family="'Russo One',sans-serif" font-size="{cap_size}" fill="#17191C">{cap}</text>
    </svg>
  </div>
</section>

<section id="services">
  <div class="wrap">
    <div class="sec-head reveal"><div class="eyebrow">Что делаем</div><h2>{services_h2}</h2></div>
    <div class="grid">
{services_html}
    </div>
  </div>
</section>

<section class="why" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head reveal"><div class="eyebrow">Почему к нам</div><h2>{why_h2}</h2></div>
    <div class="grid">
{why_html}
    </div>
  </div>
</section>

{reviews_section}

<section class="contact" id="contact">
  <div class="wrap">
    <div class="sec-head reveal"><div class="eyebrow">Как нас найти</div><h2>Контакты</h2></div>
    <div class="card reveal">
      <dl>
        <dt>Адрес</dt><dd>{address}</dd>
        <dt>Режим работы</dt><dd>{hours_contact}</dd>
      </dl>
      <dl>
        <dt>Телефоны</dt><dd>{phones_html}</dd>
        <a class="btn btn-main" href="{maps_url}" target="_blank" rel="noopener">Маршрут в Яндекс.Картах</a>
      </dl>
    </div>
  </div>
</section>

<footer><div class="wrap">
<span>© 2026 {name} · Калуга</span>
<span class="demo-badge">Демонстрационный макет нового сайта</span>
</div></footer>

<a class="fab" href="tel:{tel_main}" aria-label="Позвонить">📞</a>

<script>
const els = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window) {{
  const io = new IntersectionObserver(es => es.forEach(e => {{
    if (e.isIntersecting) {{ e.target.classList.add('on'); io.unobserve(e.target); }}
  }}), {{threshold: .12}});
  els.forEach(el => io.observe(el));
}} else {{ els.forEach(el => el.classList.add('on')); }}
</script>
</body>
</html>
"""

def ratebox(score, count_txt, link):
    return f'''<div class="ratebox">
      <div class="score">{score}</div>
      <div><div class="stars">★★★★★</div>
      <small>{count_txt} · <a href="{link}" target="_blank" rel="noopener">отзывы на Яндекс.Картах</a></small></div>
    </div>'''

def badge(text):
    return f'''<div class="ratebox"><div class="score" style="font-size:22px">{text}</div></div>'''

def svc(h, p, price):
    return f'''      <div class="svc reveal"><h3>{h}</h3><p>{p}</p><div class="price">{price}</div></div>'''

def why(d, p):
    return f'''      <div class="why-item reveal"><div class="display">{d}</div><p>{p}</p></div>'''

def rev(author, text):
    return f'''      <div class="rev reveal"><p>«{text}»</p>
        <div class="who"><span>{author}</span><span class="stars">★★★★★</span></div></div>'''

def reviews_section(revs, src_line, link):
    if not revs:
        return ""
    items = "\n".join(revs)
    return f'''<section class="reviews">
  <div class="wrap">
    <div class="sec-head reveal"><div class="eyebrow">Слово клиентам</div><h2>Отзывы с Яндекс.Карт</h2></div>
    <div class="grid">
{items}
    </div>
    <p class="rev-src reveal">{src_line} <a href="{link}" target="_blank" rel="noopener">Читать все →</a></p>
  </div>
</section>'''

COMPANIES = {}

COMPANIES["nikservice"] = dict(
    name="НикСервис", logo_html='НИК<span>СЕРВИС</span>',
    title="НикСервис — ремонт двигателей, АКПП и подвески в Калуге",
    meta_desc="Автотехцентр НикСервис: диагностика и ремонт иномарок в Калуге с 2008 года. Двигатель, АКПП, подвеска, ТО.",
    accent="#E5453A", accent_dark="#C93327", cap="NS", cap_size="26",
    eyebrow="Калуга · Московская, 289 к. 7", headline="Ремонтируем иномарки с 2008 года",
    sub="Диагностика и ремонт любой сложности: двигатель, АКПП и вариаторы, подвеска, электрика. Своя площадка под ремонт коробок — не отдаём вашу машину «подрядчикам».",
    ratebox=ratebox("4,8", "177 оценок", "https://yandex.ru/maps/org/nikservice/223086700773/"),
    cta="Записаться на диагностику",
    hours_hero='<p class="hours-hero">Запись по телефону: <b>+7 (4842) 40-07-40</b></p>',
    services_h2="Услуги",
    services_html="\n".join([
        svc("Ремонт двигателей", "Бензиновые и дизельные, любой марки и года. Диагностика перед ремонтом — обязательно.", "цена по диагностике"),
        svc("АКПП, вариаторы, DSG", "Отдельная специализированная площадка: пер. Тульский, 66. Ремонт гидротрансформаторов.", "цена по диагностике"),
        svc("Ходовая и подвеска", "Диагностика, ремонт, развал-схождение после работ.", "от диагностики"),
        svc("Автодиагностика", "Компьютерная диагностика двигателя, коробки, электрики.", "по звонку"),
        svc("Техобслуживание", "Масло, фильтры, колодки, регламентное ТО с отметкой.", "по звонку"),
        svc("Рулевые рейки и электрика", "Ремонт рулевых реек, поиск неисправностей электросистем.", "по звонку"),
    ]),
    why_h2="18 лет в ремонте",
    why_html="\n".join([
        why('С <em>2008</em> года', "Тысячи отремонтированных машин и своя клиентская база."),
        why('Запчасти <em>найдём сами</em>', "Не надо искать детали — подберём и привезём под ремонт."),
        why('<em>2</em> площадки', "Основная на Московской и отдельный цех АКПП на Тульском."),
        why('Честная диагностика', "Сначала показываем причину, потом ремонтируем."),
    ]),
    reviews_section=reviews_section([
        rev("Игорь Е.", "Отличный сервис, грамотный персонал. Качественное выполнение работ и очень демократичные цены. И не надо заботиться о поиске запасных частей. Словом, СУПЕР!"),
        rev("Наталья Н.", "Очень быстро решили проблему — починили буквально за 20 минут."),
    ], "Рейтинг 4,8 — 177 оценок на Яндекс.Картах.", "https://yandex.ru/maps/org/nikservice/223086700773/reviews/"),
    address="Калуга, ул. Московская, 289 корп. 7<br><small style='color:#5A6270'>Цех АКПП: пер. Тульский, 66</small>",
    hours_contact="Запись по телефону",
    tel_main="+74842400740", tel_main_fmt="+7 (4842) 40-07-40",
    phones_html='<a href="tel:+74842400740">+7 (4842) 40-07-40</a><br><a href="tel:+79307540740">+7 (930) 754-07-40</a><br><a href="tel:+79206113611">+7 (920) 611-36-11</a> — цех АКПП',
    maps_url="https://yandex.ru/maps/org/nikservice/223086700773/",
)

COMPANIES["volvo"] = dict(
    name="Volvo-Калуга", logo_html='VOLVO<span>·КАЛУГА</span>',
    title="Volvo-Калуга — специализированный сервис Volvo",
    meta_desc="Сервис только для Volvo в Калуге: ТО, ремонт КПП, автоэлектрика. Знаем эти машины досконально.",
    accent="#4A90D9", accent_dark="#3577BD", cap="V", cap_size="30",
    eyebrow="Калуга · Октябрьский округ", headline="Сервис только для Volvo",
    sub="Работаем с одной маркой — и знаем её до последнего болта. ТО, ремонт КПП, автоэлектрика и те неисправности, от которых отказываются универсальные сервисы.",
    ratebox=badge("Только Volvo · 20 отзывов на Картах"),
    cta="Записаться",
    hours_hero='<p class="hours-hero">Запись по телефону: <b>+7 (4842) 57-84-08</b></p>',
    services_h2="Услуги",
    services_html="\n".join([
        svc("Техобслуживание Volvo", "Регламентное ТО по карте производителя, оригинальные и проверенные аналоги.", "по звонку"),
        svc("Ремонт КПП", "Автоматические и механические коробки Volvo — диагностика и ремонт.", "цена по диагностике"),
        svc("Автоэлектрика", "Сложные электрические неисправности, с которыми «гоняют по сервисам».", "цена по диагностике"),
        svc("Диагностика", "Фирменная диагностика систем Volvo, честное заключение.", "по звонку"),
    ]),
    why_h2="Почему владельцы Volvo едут к нам",
    why_html="\n".join([
        why('<em>Одна</em> марка', "Только Volvo — типовые болячки каждой модели знаем наизусть."),
        why('Центр города', "Удобно доехать из любого района Калуги."),
        why('Берёмся за <em>сложное</em>', "Чиним то, от чего отказались другие сервисы — см. отзывы."),
        why('Выручаем транзитных', "Сломались на трассе М3? Постараемся взять в работу без очереди."),
    ]),
    reviews_section=reviews_section([
        rev("Владелец XC60", "Уже 3 года пользуюсь услугами данного сервиса. Работают профессионалы своего дела: работают только с Volvo, знают все проблемы автомобилей этой марки."),
        rev("Семья из Санкт-Петербурга", "Ехали с детьми из СПб, по дороге сломалась машина (Volvo XC90) — поломка, которую могли устранить только в специализированном центре. Несмотря на очередь, взяли машину в работу почти сразу. Очень выручили!"),
        rev("Сергей Л.", "Проблема была с фарами: моргали, гасли, жили своей жизнью. Два года мучился, обращался в разные сервисы в Москве и Калуге — толку ноль. Здесь — решили."),
    ], "20 отзывов на Яндекс.Картах.", "https://yandex.ru/maps/org/volvo_kaluga/1008625236/reviews/"),
    address="Калуга, Октябрьский округ<br><small style='color:#5A6270'>Точный адрес и схему проезда подскажем по телефону</small>",
    hours_contact="Запись по телефону",
    tel_main="+74842578408", tel_main_fmt="+7 (4842) 57-84-08",
    phones_html='<a href="tel:+74842578408">+7 (4842) 57-84-08</a><br><a href="mailto:volvo-kaluga@yandex.ru">volvo-kaluga@yandex.ru</a>',
    maps_url="https://yandex.ru/maps/org/volvo_kaluga/1008625236/",
)

COMPANIES["van"] = dict(
    name="Автосервис ВАН", logo_html='ВАН<span>·СЕРВИС</span>',
    title="Автосервис ВАН — кузовной ремонт, покраска, мойка в Калуге",
    meta_desc="Автосервис полного цикла на Зерновой, 17А: кузовной ремонт, покраска, двигатель, ходовая. Мойка бесплатно при любом ремонте.",
    accent="#FF8A1E", accent_dark="#E07208", cap="ВАН", cap_size="19",
    eyebrow="Калуга · Зерновая, 17А", headline="Автосервис полного цикла + мойка в подарок",
    sub="Кузовной ремонт и покраска, двигатель, ходовая, стёкла, шумоизоляция — легковые и грузовые. При любом ремонте помоем машину бесплатно.",
    ratebox=ratebox("4,9", "87 отзывов · 1 место на Zoon по замене тормозных дисков", "https://yandex.ru/maps/org/van/1130906008/"),
    cta="Позвонить и записаться",
    hours_hero='<p class="hours-hero">Работаем: <b>пн–пт 9:00–19:00</b> · <b>сб 9:00–18:00</b></p>',
    services_h2="Услуги и цены",
    services_html="\n".join([
        svc("Кузовной ремонт и покраска", "Вмятины, царапины, полная окраска. Постоянным клиентам скидка 10% на покраску.", "от 2 000 ₽"),
        svc("Ремонт двигателя", "Бензиновые и дизельные, легковые и грузовые.", "от 1 000 ₽"),
        svc("Замена колодок и тормоза", "1 место в Калуге по замене тормозных дисков по версии Zoon.", "от 1 500 ₽"),
        svc("Сход-развал", "На стенде, после ремонта подвески — обязательно.", "по звонку"),
        svc("Автостёкла", "Замена лобового, ремонт сколов и трещин.", "по звонку"),
        svc("Мойка и шумоизоляция", "Мойка — бесплатно при любом ремонте. Шумоизоляция салона под ключ.", "0 ₽ при ремонте"),
    ]),
    why_h2="Почему к нам едут",
    why_html="\n".join([
        why('Мойка <em>в подарок</em>', "Любой ремонт — машину отдаём чистой, бесплатно."),
        why('<em>−10%</em> на покраску', "Постоянным клиентам скидка на кузовные работы."),
        why('Легковые <em>и грузовые</em>', "Берём в работу любые марки, включая коммерческий транспорт."),
        why('Гарантия на работы', "Срок зависит от вида работ — фиксируем при приёмке."),
    ]),
    reviews_section=reviews_section([
        rev("Avik M.", "Огромная благодарность сервису ВАН и команде мастеров! Обратился по рекомендации и ни разу не пожалел. Ребята настоящие профи, работают слаженно, как единый механизм."),
        rev("Клиент сервиса", "Обращался с проблемой в автомобиле и был приятно удивлён качеством обслуживания. Профессионализм и оперативность!"),
    ], "87 отзывов на Яндекс.Картах, рейтинг 4,9 на Zoon.", "https://yandex.ru/maps/org/van/1130906008/reviews/"),
    address="Калуга, Зерновая ул., 17А",
    hours_contact="Пн–пт 9:00–19:00<br>Сб 9:00–18:00",
    tel_main="+79807102370", tel_main_fmt="+7 (980) 710-23-70",
    phones_html='<a href="tel:+79807102370">+7 (980) 710-23-70</a><br><a href="tel:+79807101174">+7 (980) 710-11-74</a>',
    maps_url="https://yandex.ru/maps/org/van/1130906008/",
)

COMPANIES["avtoshina40"] = dict(
    name="Автошина40", logo_html='АВТОШИНА<span>40</span>',
    title="Автошина40 — шины и диски в Калуге: наличие, заказ, шиномонтаж",
    meta_desc="Магазин шин и дисков в Калуге: 70+ брендов, подбор по авто, шиномонтаж и сезонное хранение. Рейтинг 5,0 на Яндекс.Картах.",
    accent="#00B8A9", accent_dark="#00958A", cap="40", cap_size="30",
    eyebrow="Калуга · Зерновая, 50А", headline="Шины и диски: подберём, привезём, поставим",
    sub="70+ брендов — от Cordiant до Michelin. Подбор под ваш автомобиль и бюджет, быстрая доставка под заказ, свой шиномонтаж и сезонное хранение колёс.",
    ratebox=ratebox("5,0", "335 оценок · 203 отзыва", "https://yandex.ru/maps/org/avtoshina40/54453622118/"),
    cta="Подобрать шины по телефону",
    hours_hero='<p class="hours-hero">Консультация по телефону: <b>+7 (903) 636-55-80</b></p>',
    services_h2="Что предлагаем",
    services_html="\n".join([
        svc("Шины в наличии и под заказ", "Лето, зима, всесезонка. 70+ брендов, честная консультация под ваш бюджет.", "подбор бесплатно"),
        svc("Литые и стальные диски", "Подбор по параметрам вашего авто: PCD, вылет, диаметр.", "подбор бесплатно"),
        svc("Шиномонтаж и балансировка", "Купили у нас — сразу собрали и отбалансировали, заберёте готовые колёса.", "по звонку"),
        svc("Сезонное хранение", "Храним ваш второй комплект — дома место не занимает.", "по звонку"),
        svc("Быстрая доставка", "Под заказ привозим за 1–2 дня, даже «последним паровозом перед Новым годом».", "—"),
        svc("Шинный калькулятор", "Поможем понять, какие размеры взаимозаменяемы для вашей машины.", "бесплатно"),
    ]),
    why_h2="Рейтинг 5,0 — вот почему",
    why_html="\n".join([
        why('<em>5,0</em> из 335 оценок', "Высшая оценка на Яндекс.Картах среди шинных центров Калуги."),
        why('Под <em>ваш</em> бюджет', "Подбираем и премиум, и разумную альтернативу — без навязывания."),
        why('Всё в <em>одном месте</em>', "Купили → собрали → отбалансировали → поставили. Или сдали на хранение."),
        why('Всегда на связи', "Консультация по телефону сразу, статус заказа — без «перезвоните завтра»."),
    ]),
    reviews_section=reviews_section([
        rev("Дмитрий Т.", "Помогли подобрать диски с нужными параметрами, доставка быстрая, персонал вежливый и всегда на связи + качественный шиномонтаж. Рекомендую!"),
        rev("Сергеич", "По телефону сразу получил квалифицированную консультацию. На следующий день в магазине подобрали шины согласно моим запросам."),
        rev("Натали", "Предложили варианты на выбор, привезли практически последним паровозом перед Новым годом! Сразу собрали колёса и отбалансировали — забрала готовые, очень довольна."),
    ], "Рейтинг 5,0 — 335 оценок, 203 отзыва.", "https://yandex.ru/maps/org/avtoshina40/54453622118/reviews/"),
    address="Калуга, Зерновая ул., 50А",
    hours_contact="Уточняйте по телефону",
    tel_main="+79036365580", tel_main_fmt="+7 (903) 636-55-80",
    phones_html='<a href="tel:+79036365580">+7 (903) 636-55-80</a><br><a href="tel:+79106099905">+7 (910) 609-99-05</a><br><a href="tel:+74842595580">+7 (4842) 59-55-80</a>',
    maps_url="https://yandex.ru/maps/org/avtoshina40/54453622118/",
)

COMPANIES["avtologika"] = dict(
    name="АвтоЛогикА", logo_html='АВТО<span>ЛОГИКА</span>',
    title="АвтоЛогикА — автозапчасти и автосервис на Московской, Калуга",
    meta_desc="Запчасти под любой бюджет + автосервис в одном месте. Московская, 295А, Калуга.",
    accent="#2D7DFF", accent_dark="#1B62D6", cap="АЛ", cap_size="24",
    eyebrow="Калуга · Московская, 295А", headline="Запчасти под ваш бюджет + сервис рядом",
    sub="Подберём и привезём запчасти и техжидкости — быстро и под любой кошелёк. А поставить их можно тут же: свой автосервис с опытными механиками.",
    ratebox=ratebox("4,4", "35 оценок · 21 отзыв", "https://yandex.ru/maps/org/avtologika/228202284580/"),
    cta="Подобрать запчасть",
    hours_hero='<p class="hours-hero">Подбор по телефону: <b>+7 (920) 875-10-02</b></p>',
    services_h2="Магазин + сервис",
    services_html="\n".join([
        svc("Подбор запчастей", "По VIN и по образцу. Оригинал или аналог — под ваш бюджет, честно скажем разницу.", "бесплатно"),
        svc("Техжидкости и масла", "Масла, антифризы, тормозные жидкости — в наличии, цены приятно удивляют.", "в наличии"),
        svc("Замена масла и колодок", "Купили у нас — сразу установили. Не надо никуда ехать.", "по звонку"),
        svc("Слесарный ремонт", "Ходовая, тормоза, плановое ТО — опытные механики в сервисе при магазине.", "по звонку"),
    ]),
    why_h2="Магазин и сервис в одной точке",
    why_html="\n".join([
        why('Запчасть + <em>установка</em>', "Купили — тут же поставили. Экономия времени и без «не та деталь»."),
        why('Под <em>любой</em> кошелёк', "От бюджетных аналогов до оригинала — подберём и объясним разницу."),
        why('Быстрые <em>сроки</em>', "Поставки запчастей быстрее, чем ждут обычно."),
        why('Выручаем в аварийных', "Сорвало тормоза по пути? Закажем и заменим в тот же день — так уже было."),
    ]),
    reviews_section=reviews_section([
        rev("Иван М.", "Отличный магазин! Цены и сроки поставки запчастей приятно удивляют. Такого отношения к клиентам в Калуге я не встречал."),
        rev("Игорь", "Сорвало тормозные накладки, еле доехал до сервиса без тормозов. Заказали колодки и сразу заменили — уехал домой на машине. Отличный сервис!"),
        rev("Максим", "Подберут запчасти под любой кошелёк. В автосервисе позаботятся о вашем автомобиле, опытные механики. Цена = качество. Заеду ещё!"),
    ], "21 отзыв на Яндекс.Картах.", "https://yandex.ru/maps/org/avtologika/228202284580/reviews/"),
    address="Калуга, ул. Московская, 295А",
    hours_contact="Уточняйте по телефону",
    tel_main="+79208751002", tel_main_fmt="+7 (920) 875-10-02",
    phones_html='<a href="tel:+79208751002">+7 (920) 875-10-02</a>',
    maps_url="https://yandex.ru/maps/org/avtologika/228202284580/",
)

COMPANIES["zona-komforta"] = dict(
    name="Zona Комфорта", logo_html='ZONA<span>·КОМФОРТА</span>',
    title="Zona Комфорта — детейлинг и химчистка авто в Калуге",
    meta_desc="Химчистка салона, керамомойка, твёрдый воск, мойка днища. Зона ожидания с чаем и кальяном. Зерновая, 22.",
    accent="#9B6CFF", accent_dark="#7E4FE6", cap="ZK", cap_size="24",
    eyebrow="Калуга · Зерновая, 22 стр. 1", headline="Детейлинг, после которого машина как новая",
    sub="Химчистка салона, керамомойка, твёрдый воск, мойка днища. Пока мы наводим красоту — вы отдыхаете в зоне ожидания с чаем и кальяном.",
    ratebox=ratebox("4,6", "13 оценок · 10 отзывов", "https://yandex.ru/maps/org/zona_komforta/116958229636/"),
    cta="Записаться",
    hours_hero='<p class="hours-hero">Запись по телефону: <b>+7 (962) 171-00-08</b></p>',
    services_h2="Услуги",
    services_html="\n".join([
        svc("Химчистка салона", "Полная химчистка: сиденья, потолок, пластик. Машина пахнет как новая.", "по звонку"),
        svc("Керамомойка", "Мойка с керамическим составом — блеск и защита ЛКП.", "по звонку"),
        svc("Твёрдый воск", "Защитное покрытие на месяцы: вода и грязь скатываются сами.", "по звонку"),
        svc("Мойка днища", "Смываем реагенты и грязь там, куда обычная мойка не добирается.", "по звонку"),
    ]),
    why_h2="Комфорт — в названии",
    why_html="\n".join([
        why('Зона <em>ожидания</em>', "Чай и кальян, пока машину приводят в порядок."),
        why('Скидки по записи', "Записались заранее — получили скидку на комплекс."),
        why('Аккуратно к <em>ЛКП</em>', "Профессиональная химия и мягкие технологии мойки."),
        why('Довозим до идеала', "Не отдаём машину, пока результат не устроит нас самих."),
    ]),
    reviews_section=reviews_section([
        rev("Ольга А.", "Приезжали на химчистку — всё сделали круто и чисто, приятная атмосфера, вежливый персонал. В зоне ожидания можно покурить кальян и попить вкусный чай!"),
        rev("Кирилл Н.", "Заезжал на мойку днища — сделали чётко. Записался на твёрдый воск, сказали сделают скидку."),
        rev("Александр С.", "Привозил автомобиль на керамомойку — отмыли отлично, очень доволен услугой, буду ещё приезжать."),
    ], "Рейтинг 4,6 на Яндекс.Картах.", "https://yandex.ru/maps/org/zona_komforta/116958229636/reviews/"),
    address="Калуга, Зерновая ул., 22, стр. 1",
    hours_contact="Запись по телефону",
    tel_main="+79621710008", tel_main_fmt="+7 (962) 171-00-08",
    phones_html='<a href="tel:+79621710008">+7 (962) 171-00-08</a>',
    maps_url="https://yandex.ru/maps/org/zona_komforta/116958229636/",
)

COMPANIES["selena"] = dict(
    name="Селена буссервис", logo_html='СЕЛЕНА<span>·БУС</span>',
    title="Селена буссервис — ремонт микроавтобусов в Калуге",
    meta_desc="Сервис коммерческого транспорта и микроавтобусов в Калуге: ходовая, двигатель, ТО перед рейсом. Складская, 11.",
    accent="#FFA000", accent_dark="#DB8700", cap="СБ", cap_size="24",
    eyebrow="Калуга · Складская, 11", headline="Сервис микроавтобусов: чиним, пока бизнес не стоит",
    sub="Газель, Sprinter, Transit, Ducato и другой коммерческий транспорт. Понимаем, что каждый день простоя — это ваши деньги, поэтому работаем быстро.",
    ratebox=badge("Специализация: микроавтобусы и LCV"),
    cta="Позвонить в сервис",
    hours_hero='<p class="hours-hero">Запись по телефону: <b>+7 (910) 915-13-19</b></p>',
    services_h2="Услуги",
    services_html="\n".join([
        svc("Ходовая и подвеска", "Усиленные узлы коммерческого транспорта — рессоры, ступицы, шаровые.", "по звонку"),
        svc("Двигатель", "Дизель и бензин: диагностика, ремонт, замена расходников.", "по звонку"),
        svc("ТО перед рейсом", "Проверка тормозов, света, жидкостей — чтобы в дороге не подвело.", "по звонку"),
        svc("Тормозная система", "Колодки, диски, суппорты — с учётом нагрузки гружёной машины.", "по звонку"),
    ]),
    why_h2="Для тех, кто на колёсах зарабатывает",
    why_html="\n".join([
        why('Минимум <em>простоя</em>', "Понимаем цену каждого дня без машины — не тянем со сроками."),
        why('Знаем <em>LCV</em>', "Специализируемся на коммерческом транспорте, а не чиним «всё подряд»."),
        why('Удобно для баз', "Складская улица — рядом с логистическими базами города."),
        why('Честная смета', "Цена до начала работ, без «выросло в процессе»."),
    ]),
    reviews_section="",
    address="Калуга, Складская ул., 11",
    hours_contact="Запись по телефону",
    tel_main="+79109151319", tel_main_fmt="+7 (910) 915-13-19",
    phones_html='<a href="tel:+79109151319">+7 (910) 915-13-19</a>',
    maps_url="https://yandex.ru/maps/org/selena_busservis/121702676968/",
)

COMPANIES["profi"] = dict(
    name="Профи", logo_html='ПРОФИ<span>·ТОНИРОВКА</span>',
    title="Профи — тонирование автостёкол в Калуге",
    meta_desc="Тонировка стёкол, атермальная плёнка на лобовое. Семейная мастерская на Михалёвской, 60.",
    accent="#35B6E8", accent_dark="#1E9CCE", cap="П", cap_size="30",
    eyebrow="Калуга · Михалёвская, 60", headline="Тонировка — как для своих",
    sub="Семейная мастерская: тонируем без пыли и пузырей, клеим атермальную плёнку на лобовое, честно отвечаем на любые вопросы — даже «неадекватные».",
    ratebox=ratebox("4,5", "65 оценок · 28 отзывов", "https://yandex.ru/maps/org/profi/152167768886/"),
    cta="Записаться на тонировку",
    hours_hero='<p class="hours-hero">Запись по телефону: <b>+7 (903) 636-05-43</b></p>',
    services_h2="Услуги",
    services_html="\n".join([
        svc("Тонирование задней полусферы", "Качественная плёнка, ровная поклейка без пузырей и отслоений.", "по звонку"),
        svc("Атермальная плёнка на лобовое", "Меньше жара летом, разрешена к эксплуатации. Быстро и качественно.", "по звонку"),
        svc("Снятие старой плёнки", "Уберём старую тонировку и клей без следов.", "по звонку"),
        svc("Мелкий сервис", "Плановое ТО и мелкий ремонт — заказажем детали заранее к вашему приезду.", "по звонку"),
    ]),
    why_h2="Семейная мастерская",
    why_html="\n".join([
        why('Как <em>к друзьям</em> в гараж', "Без пафоса: всё расскажем, покажем и объясним."),
        why('Плёнка <em>не пузырится</em>', "Аккуратная работа — смотрите оценки на Картах."),
        why('Детали <em>заранее</em>', "Созвонились — заказали всё нужное к вашему приезду."),
        why('Цена и качество', "Атермалка на лоб: «качество и цена отличные» — из отзыва."),
    ]),
    reviews_section=reviews_section([
        rev("Артём Б.", "Попал к мастерам своего дела: профессионально и без пафоса отвечают на все вопросы. Всё здорово — как к друзьям в гараж заехал."),
        rev("Александр К.", "Владимир быстро и качественно наклеил атермалку на лобовое. Качество и цена отличные!"),
        rev("Ирина Р.", "Семейная мастерская! Очень приятный и радушный хозяин: всё рассказал, показал, объяснил. Заранее заказал все необходимые детали после нашего созвона."),
    ], "Рейтинг 4,5 — 65 оценок.", "https://yandex.ru/maps/org/profi/152167768886/reviews/"),
    address="Калуга, Михалёвская ул., 60",
    hours_contact="Запись по телефону",
    tel_main="+79036360543", tel_main_fmt="+7 (903) 636-05-43",
    phones_html='<a href="tel:+79036360543">+7 (903) 636-05-43</a>',
    maps_url="https://yandex.ru/maps/org/profi/152167768886/",
)

COMPANIES["avtobanya"] = dict(
    name="Автобаня «Без разводов»", logo_html='АВТОБАНЯ<span>·БЕЗ РАЗВОДОВ</span>',
    title="Автобаня «Без разводов» — мойка по записи в Калуге",
    meta_desc="Автомойка по записи: без очередей и без разводов на кузове. Комплексная мойка, воск, ковры. Пер. Труда, 5А.",
    accent="#00C2FF", accent_dark="#00A5DB", cap="АБ", cap_size="24",
    eyebrow="Калуга · пер. Труда, 5А", headline="Мойка по записи: без очереди и без разводов",
    sub="Записались — приехали — вас уже ждут. Моем быстро и качественно, название обязывает: никаких разводов на кузове.",
    ratebox=ratebox("4,3", "75 оценок · 31 отзыв", "https://yandex.ru/maps/org/avtobanya_bez_razvodov/227923520849/"),
    cta="Записаться на мойку",
    hours_hero='<p class="hours-hero">Запись по телефону: <b>+7 (906) 506-61-88</b></p>',
    services_h2="Услуги",
    services_html="\n".join([
        svc("Комплексная мойка", "Кузов + салон + коврики. Быстро и без разводов.", "по звонку"),
        svc("Мойка ковров", "Отмываем даже сложные загрязнения — процесс отладили.", "по звонку"),
        svc("Воск и защита", "Покрытие после мойки: блеск дольше, грязь липнет меньше.", "по звонку"),
        svc("Уборка салона", "Пылесос, пластик, стёкла изнутри — полный порядок.", "по звонку"),
    ]),
    why_h2="Почему по записи — это плюс",
    why_html="\n".join([
        why('<em>Без</em> очередей', "Ваше время забронировано — приехали и сразу на пост."),
        why('Постоянные клиенты', "«Мою машину только здесь» — типичный отзыв на Картах."),
        why('Быстро <em>и</em> тщательно', "Отработанный процесс: моем быстро, но не «на отвяжись»."),
        why('Слышим критику', "Проблемные места (например, ковры) — дорабатываем, это видно в отзывах."),
    ]),
    reviews_section=reviews_section([
        rev("Егор Ч.", "Отличная автомойка, мою машину только здесь. Ребята моют быстро и очень качественно, очередей нет — ждать не приходится."),
    ], "31 отзыв на Яндекс.Картах.", "https://yandex.ru/maps/org/avtobanya_bez_razvodov/227923520849/reviews/"),
    address="Калуга, пер. Труда, 5А",
    hours_contact="По записи",
    tel_main="+79065066188", tel_main_fmt="+7 (906) 506-61-88",
    phones_html='<a href="tel:+79065066188">+7 (906) 506-61-88</a>',
    maps_url="https://yandex.ru/maps/org/avtobanya_bez_razvodov/227923520849/",
)

for slug, c in COMPANIES.items():
    d = os.path.join(BASE, slug)
    os.makedirs(os.path.join(d, "assets"), exist_ok=True)
    html = TEMPLATE.format(**c)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("OK", slug)
print("DONE", len(COMPANIES))
