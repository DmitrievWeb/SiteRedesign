# -*- coding: utf-8 -*-
"""Hero-фото для демо новых ниш (стоматологии, кухни, ремонт)."""
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

P = {
 "stomat-medesi": "Bright modern dental clinic treatment room, dental chair, clean white and soft blue tones, large window with daylight, calm premium atmosphere, no people, no text, photorealistic",
 "stomat-siyayushchaya": "Close-up of a beautiful natural smile with perfect white teeth, soft warm studio light, joyful mood, no text, photorealistic",
 "stomat-edvard": "Elegant dental clinic reception interior with warm wood and emerald green accents, soft lighting, premium boutique feel, no people, no text, photorealistic",
 "stomat-evrodent": "Dental clinic modern equipment close-up, dental mirror and tools on tray, clean turquoise and white palette, shallow depth of field, no text, photorealistic",
 "stomat-dentalux": "Family dental clinic bright waiting area with cozy sofa and plants, friendly warm atmosphere, light pastel colors, no people, no text, photorealistic",
 "kuhni-master": "Luxury dark green kitchen with brass handles and marble countertop, moody evening light, premium custom furniture photography, no people, no text, photorealistic",
 "kuhni-novye": "Bright scandinavian white and oak kitchen interior, morning sunlight, minimalist design, custom furniture, no people, no text, photorealistic",
 "kuhni-italum": "Modern italian style glossy kitchen, graphite and walnut tones, elegant pendant lights, showroom photography, no people, no text, photorealistic",
 "kuhni-refine": "Cozy beige matte kitchen with island and wooden bar stools, warm evening lamps, family atmosphere, no people, no text, photorealistic",
 "kuhni-uyut": "Craftsman workshop making custom furniture: wood panels, tools, sawdust in warm light, artisan atmosphere, no people faces, no text, photorealistic",
 "remont-comfort": "Freshly renovated modern living room, perfect white walls, parquet floor, designer lighting, staged interior photography, no people, no text, photorealistic",
 "remont-otdelkovo": "Interior renovation in progress: professional plastering tools, level, paint rollers on clean dust sheet, bright room, orderly work, no people, no text, photorealistic",
 "remont-stroyprogress": "Stylish renovated kitchen-living room with exposed brick accent wall and loft lamps, warm cozy light, no people, no text, photorealistic",
 "remont-remkvartir": "Before and after renovation concept: half of room bare concrete, half finished with white walls and wooden floor, dramatic light, no people, no text, photorealistic",
 "remont-stroyresurs": "Modern renovated bathroom with large format grey tiles, black fixtures, walk-in shower with glass, hotel style, no people, no text, photorealistic",
}

def gen(prompt):
    r = requests.post("https://api.openai.com/v1/images/generations",
        headers={"Authorization": f"Bearer {KEY}"},
        json={"model": "gpt-image-1", "prompt": prompt, "size": "1536x1024", "quality": "medium", "n": 1},
        timeout=300)
    if r.status_code != 200:
        raise RuntimeError(r.text[:200])
    return base64.b64decode(r.json()["data"][0]["b64_json"])

for slug, prompt in P.items():
    d = os.path.join(DEMOS, slug, "assets")
    os.makedirs(d, exist_ok=True)
    out = os.path.join(d, "hero.jpg")
    if os.path.exists(out):
        print("skip", slug); continue
    try:
        data = gen(prompt)
        tmp = out + ".tmp"
        with open(tmp, "wb") as f: f.write(data)
        Image.open(tmp).convert("RGB").save(out, "JPEG", quality=82)
        os.remove(tmp)
        print("OK", slug)
    except Exception as e:
        print("FAIL", slug, str(e)[:120])
