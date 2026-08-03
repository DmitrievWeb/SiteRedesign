# -*- coding: utf-8 -*-
"""Демо-карточки (1_демо.png) для 16 новых лидов из мобильных скринов."""
import os, shutil
from PIL import Image

HOME = os.path.expanduser("~")
SR = os.path.join(HOME, "Desktop", "SiteRedesign")

SLUGS = ["stomat-medesi","stomat-siyayushchaya","stomat-edvard","stomat-evrodent","stomat-dentalux",
         "kuhni-master","kuhni-novye","kuhni-italum","kuhni-refine","kuhni-uyut",
         "remont-comfort","remont-otdelkovo","remont-stroyprogress","remont-remkvartir","remont-stroyresurs","gelman"]

for slug in SLUGS:
    src = os.path.join(HOME, f"m_{slug}.png")
    if not os.path.exists(src):
        print("MISS", slug); continue
    img = Image.open(src)
    w = 420
    r = w / img.width
    img2 = img.resize((w, int(img.height * r)), Image.LANCZOS).crop((0, 0, w, 1800))
    c = Image.new("RGB", (img2.width + 60, img2.height + 60), "#1B1D21")
    c.paste(img2, (30, 30))
    od = os.path.join(SR, "outreach", slug)
    os.makedirs(od, exist_ok=True)
    c.save(os.path.join(od, "1_демо.png"))
    ad = os.path.join(SR, "demos", slug, "assets")
    os.makedirs(ad, exist_ok=True)
    shutil.move(src, os.path.join(ad, "after_mobile.png"))
    print("OK", slug)
print("DONE")
