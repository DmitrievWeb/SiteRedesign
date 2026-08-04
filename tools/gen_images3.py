# -*- coding: utf-8 -*-
"""Волна 1 редизайна: доп. изображения (g1..g4) под стиль каждого демо."""
import base64, os, sys
import requests
from PIL import Image

ENV = os.path.join(os.path.expanduser("~"), "Desktop", "WBAdsAgent", ".env")
KEY = None
with open(ENV, encoding="utf-8") as f:
    for line in f:
        if line.startswith("OPENAI_API_KEY="):
            KEY = line.split("=", 1)[1].strip()
DEMOS = os.path.join(os.path.expanduser("~"), "Desktop", "SiteRedesign", "demos")

NO = "no people faces, no text, no logos, photorealistic"
P = {
 # shinservice40 — ночной пит-стоп (Sequel-гибрид, тёплая лампа на чёрном)
 "shinservice40/g1": f"Cinematic night scene: single car wheel lit by one warm amber work lamp in a dark tire workshop, deep black shadows, film still mood, {NO}",
 "shinservice40/g2": f"Macro of new tire tread pattern, dramatic side warm light on black background, glistening rubber texture, {NO}",
 "shinservice40/g3": f"Wheel balancing machine spinning a wheel in dark garage, warm practical light, motion blur on rim, cinematic, {NO}",
 "shinservice40/g4": f"Gloved hands with pneumatic impact wrench tightening wheel bolts, warm light from side, dark cinematic garage, {NO}",
 # nikservice — Dala-гибрид (техно, циан-данные)
 "nikservice/g2": f"OBD diagnostic scanner screen glowing cyan in dark car service, plugged cable, shallow depth, tech atmosphere, {NO}",
 "nikservice/g3": f"Automatic transmission gears close-up, precise metal machinery, cool blue tech light on dark, {NO}",
 "nikservice/g4": f"Modern car service workshop at night, lifts and neat tool walls, cool blue-cyan ambient light, wide shot, {NO}",
 # volvo — Sequel полный
 "volvo/g2": f"Macro of a premium SUV LED headlight, elegant lines, warm lamplight reflections on dark background, cinematic film still, {NO}",
 "volvo/g3": f"Premium leather car seat stitching macro, warm cream tones on black, luxury calm mood, {NO}",
 "volvo/g4": f"Dark garage at night with soft warm lamp glow, silhouette of scandinavian SUV, cinematic minimalism, {NO}",
 # avtoshina40 — Apple-гибрид (шина как продукт)
 "avtoshina40/g1": f"Single new car tire standing as a product hero on pure white seamless studio background, soft even light, {NO}",
 "avtoshina40/g2": f"Extreme macro of tire tread blocks on light gray background, clean product photography, {NO}",
 "avtoshina40/g4": f"Polished alloy wheel rim on light gray studio background, product photography, soft shadows, {NO}",
 # zona-komforta — Aurora (иридесцент)
 "zona-komforta/g2": f"Macro water beads on freshly waxed car paint with iridescent blue-magenta-cyan reflections, glossy, {NO}",
 "zona-komforta/g3": f"Polishing machine pad on glossy car hood with colorful light streaks reflections, dark studio, {NO}",
 "zona-komforta/g4": f"Thick white foam texture macro with subtle iridescent color reflections, detailing shampoo, {NO}",
 # stomat-medesi — Apple-lite
 "stomat-medesi/g2": f"Bright dental clinic reception desk, white and soft blue, clean minimal, daylight, {NO}",
 "stomat-medesi/g3": f"Natural healthy smile close-up of adult, soft studio light, calm joyful, {NO}",
 # stomat-edvard — Sequel полный
 "stomat-edvard/g2": f"Dental chair in warm dim boutique clinic at evening, emerald and brass accents, single warm lamp, cinematic film still, {NO}",
 "stomat-edvard/g3": f"Dental instruments on tray catching warm golden lamplight against dark emerald background, macro cinematic, {NO}",
 "stomat-edvard/g4": f"Elegant brass door handle and dark green wall of private clinic entrance, warm evening light, cinematic, {NO}",
 # stomat-evrodent — Apple полный
 "stomat-evrodent/g2": f"Wide view of bright modern dental clinic hall, white and light teal, several rooms, airy daylight, {NO}",
 "stomat-evrodent/g3": f"Dental mirror tool on clean white surface, minimal product-style photo, soft shadow, {NO}",
 # kuhni-master — Sequel полный
 "kuhni-master/g2": f"Macro of brass kitchen cabinet handle on dark green matte facade, warm lamplight, luxury cinematic, {NO}",
 "kuhni-master/g3": f"Marble countertop veining macro in warm evening kitchen light, dark moody luxury, {NO}",
 "kuhni-master/g4": f"Kitchen island with pendant lamps glowing warm at night, dark luxury kitchen, cinematic wide, {NO}",
 "kuhni-master/g5": f"Open kitchen drawer with neat cutlery organizer, soft warm light, premium furniture detail, dark tones, {NO}",
 # kuhni-novye — Apple-гибрид
 "kuhni-novye/g2": f"Macro of light oak kitchen facade texture with minimalist milled handle profile, bright clean, {NO}",
 "kuhni-novye/g3": f"White kitchen worktop with single ceramic bowl, morning sunlight, scandinavian minimal, {NO}",
 "kuhni-novye/g4": f"Wooden dining table by big window with soft daylight, light interior, calm minimal, {NO}",
}

only = sys.argv[1:]
items = [(k, v) for k, v in P.items() if not only or any(k.startswith(o) for o in only)]
for key, prompt in items:
    slug, name = key.split("/")
    d = os.path.join(DEMOS, slug, "assets")
    os.makedirs(d, exist_ok=True)
    out = os.path.join(d, name + ".jpg")
    if os.path.exists(out):
        print("skip", key); continue
    try:
        r = requests.post("https://api.openai.com/v1/images/generations",
            headers={"Authorization": f"Bearer {KEY}"},
            json={"model": "gpt-image-1", "prompt": prompt, "size": "1536x1024", "quality": "medium", "n": 1},
            timeout=300)
        if r.status_code != 200:
            print("FAIL", key, r.text[:120]); continue
        data = base64.b64decode(r.json()["data"][0]["b64_json"])
        tmp = out + ".tmp"
        with open(tmp, "wb") as f: f.write(data)
        Image.open(tmp).convert("RGB").save(out, "JPEG", quality=82)
        os.remove(tmp)
        print("OK", key)
    except Exception as e:
        print("ERR", key, str(e)[:100])
print("WAVE1 DONE")
