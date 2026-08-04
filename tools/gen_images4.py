# -*- coding: utf-8 -*-
"""Волна 2: +2 фото для 15 демо с частичным апгрейдом."""
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
 "van/g2": f"Car body painter in protective suit polishing freshly painted hood, warm orange workshop light, {NO}",
 "van/g3": f"Professional body shop tools on workbench, spray gun and sanding blocks, warm industrial light, {NO}",
 "avtologika/g2": f"Auto parts store counter with catalog monitor and parts boxes, bright daylight, tidy retail, {NO}",
 "avtologika/g3": f"Stacked cardboard boxes with car spare parts on shelf, warm light, shallow depth, {NO}",
 "selena/g2": f"Row of white cargo vans parked at logistics base at dawn, amber morning light, {NO}",
 "selena/g3": f"Commercial vehicle workshop bay with tools and lift, warm practical light, {NO}",
 "profi/g2": f"Roll of window tint film with iridescent purple-blue reflections, macro on dark, {NO}",
 "profi/g3": f"Squeegee applying tint film to car glass with soap solution drops, cool blue light, macro, {NO}",
 "avtobanya/g2": f"High pressure washer spraying water on car surface, droplets frozen in air, aqua tones, bright, {NO}",
 "avtobanya/g3": f"Microfiber towel drying glossy car paint, soft aqua studio light, macro, {NO}",
 "stomat-siyayushchaya/g2": f"Cozy kids corner in dental clinic waiting room, soft coral and yellow toys, bright, {NO}",
 "stomat-siyayushchaya/g3": f"Modern dental chair in bright clinic with coral accent wall, daylight, {NO}",
 "stomat-dentalux/g2": f"Family friendly clinic hallway with soft lavender walls and plants, warm light, {NO}",
 "stomat-dentalux/g3": f"Dental treatment room with pastel tones, calm and clean, {NO}",
 "kuhni-italum/g2": f"Glossy graphite kitchen facade macro with elegant reflections, dark showroom light, {NO}",
 "kuhni-italum/g3": f"Kitchen bar zone with walnut wood and pendant lamps, italian modern style, evening, {NO}",
 "kuhni-refine/g2": f"Warm beige kitchen detail: open shelf with ceramics and linen towel, cozy light, {NO}",
 "kuhni-refine/g3": f"Interior designer sketch and fabric samples on wooden table, warm daylight, top view, {NO}",
 "kuhni-uyut/g2": f"Wood shavings and hand plane on workbench macro, warm workshop light, craft atmosphere, {NO}",
 "kuhni-uyut/g3": f"Wood texture samples fan on carpenter table, oak walnut ash, warm light, {NO}",
 "remont-comfort/g2": f"Renovated modern bathroom with large gray tiles and glass shower, hotel style, bright, {NO}",
 "remont-comfort/g3": f"Fresh renovated bedroom with white walls and wooden floor, staged, soft daylight, {NO}",
 "remont-otdelkovo/g2": f"Plastering trowel with smooth white plaster macro, clean renovation site, bright, {NO}",
 "remont-otdelkovo/g3": f"Paint roller with white paint on tray, tidy renovation, bright daylight, {NO}",
 "remont-stroyprogress/g2": f"Exposed brick wall texture with loft pendant lamp glowing warm, {NO}",
 "remont-stroyprogress/g3": f"Black metal loft lamps row under concrete ceiling, warm bulbs, {NO}",
 "remont-remkvartir/g2": f"Split concept: half bare concrete bedroom, half finished bedroom with bed and lamps, dramatic light, {NO}",
 "remont-stroyresurs/g2": f"Matte black bathroom faucet macro on gray tile background, droplets, {NO}",
 "remont-stroyresurs/g3": f"Tiler laying large format tile with spacers, clean site, bright, {NO}",
}

for key, prompt in P.items():
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
            print("FAIL", key, r.text[:100]); continue
        data = base64.b64decode(r.json()["data"][0]["b64_json"])
        tmp = out + ".tmp"
        with open(tmp, "wb") as f: f.write(data)
        Image.open(tmp).convert("RGB").save(out, "JPEG", quality=82)
        os.remove(tmp)
        print("OK", key)
    except Exception as e:
        print("ERR", key, str(e)[:100])
print("WAVE2 DONE")
