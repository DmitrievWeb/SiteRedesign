# -*- coding: utf-8 -*-
"""Пересборка outreach-картинок после редизайна демо."""
import os, shutil
from PIL import Image, ImageDraw, ImageFont

HOME = os.path.expanduser("~")
SR = os.path.join(HOME, "Desktop", "SiteRedesign")
DEMOS, OUT = os.path.join(SR, "demos"), os.path.join(SR, "outreach")
H, W, PAD, LH = 1100, 760, 30, 90
F_BIG = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 44)
F_SM = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 24)

def crop_scale(img, w=W, h=H):
    r = w / img.width
    img2 = img.resize((w, int(img.height * r)), Image.LANCZOS)
    return img2.crop((0, 0, w, min(h, img2.height)))

def before_after(bp, ap, op, note):
    b, a = crop_scale(Image.open(bp)), crop_scale(Image.open(ap))
    c = Image.new("RGB", (W*2+PAD*3, H+LH+PAD*2), "#17191C")
    d = ImageDraw.Draw(c)
    d.text((PAD+W//2, PAD+22), "БЫЛО", font=F_BIG, fill="#8A919C", anchor="mm")
    d.text((PAD*2+W+W//2, PAD+22), "СТАЛО", font=F_BIG, fill="#FFC400", anchor="mm")
    d.text((PAD+W//2, PAD+62), note, font=F_SM, fill="#5A6270", anchor="mm")
    d.text((PAD*2+W+W//2, PAD+62), "новый сайт, 2026", font=F_SM, fill="#C6CBD4", anchor="mm")
    c.paste(b, (PAD, LH+PAD)); c.paste(a, (PAD*2+W, LH+PAD))
    c.save(op)

def demo_card(mp, op):
    img = crop_scale(Image.open(mp), 420, 1800)
    c = Image.new("RGB", (img.width+60, img.height+60), "#17191C")
    c.paste(img, (30, 30)); c.save(op)

BA = {
    "nikservice": ("after_nikservice.png", "ns40.ru, 2018 год"),
    "volvo": ("after_volvo.png", "volvo-kaluga.ru, без мобильной версии"),
    "van": ("after_van.png", "service-van.ru, страница-агрегатор"),
    "avtoshina40": ("after_avtoshina40.png", "avtoshina40.com, без мобильной версии"),
}
MOB = {
    "avtologika": "after_avtologika_m.png",
    "zona-komforta": "after_zona_m.png",
    "selena": "after_selena_m.png",
    "profi": "after_profi_m.png",
    "avtobanya": "after_avtobanya_m.png",
}
for slug, (af, note) in BA.items():
    ad = os.path.join(DEMOS, slug, "assets")
    before_after(os.path.join(ad, "before.png"), os.path.join(HOME, af),
                 os.path.join(OUT, slug, "1_было_стало.png"), note)
    shutil.copy(os.path.join(OUT, slug, "1_было_стало.png"), os.path.join(ad, "before_after.png"))
    shutil.move(os.path.join(HOME, af), os.path.join(ad, "after.png"))
    print("OK", slug)
for slug, mf in MOB.items():
    ad = os.path.join(DEMOS, slug, "assets")
    demo_card(os.path.join(HOME, mf), os.path.join(OUT, slug, "1_демо.png"))
    shutil.move(os.path.join(HOME, mf), os.path.join(ad, "after_mobile.png"))
    print("OK", slug)
for junk in ("qa_nikservice.png", "qa_zona.png"):
    p = os.path.join(HOME, junk)
    if os.path.exists(p): os.remove(p)
print("DONE")
