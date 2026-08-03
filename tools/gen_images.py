# -*- coding: utf-8 -*-
"""Генерация hero-изображений для демо через OpenAI Images API."""
import base64, json, os, sys
import requests

ENV = os.path.join(os.path.expanduser("~"), "Desktop", "WBAdsAgent", ".env")
KEY = None
with open(ENV, encoding="utf-8") as f:
    for line in f:
        if line.startswith("OPENAI_API_KEY="):
            KEY = line.split("=", 1)[1].strip()
if not KEY:
    sys.exit("no key")

DEMOS = os.path.join(os.path.expanduser("~"), "Desktop", "SiteRedesign", "demos")

PROMPTS = {
    "nikservice": "Dramatic close-up photograph of a modern car engine bay in a professional auto repair garage, moody deep blue technical lighting, clean metal surfaces, shallow depth of field, no people, no text, photorealistic",
    "volvo": "Minimalist scandinavian photography: dark blue premium SUV silhouette in a bright clean white studio garage, soft diffused nordic light, calm composition, no logos, no text, no people, photorealistic",
    "van": "Panel van in a body repair shop being spray painted, warm orange workshop lighting, paint mist in the air, industrial atmosphere, no people visible, no text, no logos, photorealistic",
    "avtoshina40": "Neat tall stacks of brand new car tires in a bright modern tire shop, clean showroom, subtle teal accent lighting, crisp tread patterns, no text, no logos, no people, photorealistic",
    "avtologika": "Bright modern auto parts store interior: shelves with car parts boxes, oil canisters, brake discs, clean blue-white lighting, organized retail space, no readable text on boxes, no people, photorealistic",
    "zona-komforta": "Glossy black sports car in a dark luxury detailing studio under violet neon light strips, reflective wet-look paint, premium atmosphere, no text, no logos, no people, photorealistic",
    "selena": "White cargo van (sprinter type) lifted in a spacious commercial vehicle workshop, warm amber industrial lighting, tools and workbench in background, no logos, no text, no people, photorealistic",
    "profi": "Close-up of dark tint film being applied to a car side window with a squeegee, cool blue-cyan light, droplets of application fluid, precise craft work, no people faces, no text, photorealistic",
    "avtobanya": "Car completely covered in thick white foam at a car wash, water droplets flying, fresh aqua-blue tones, bright and clean, joyful atmosphere, no people, no text, photorealistic",
}

def gen(model, prompt):
    r = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
        json={"model": model, "prompt": prompt, "size": "1536x1024", "quality": "medium", "n": 1}
        if model == "gpt-image-1" else
        {"model": model, "prompt": prompt, "size": "1792x1024", "quality": "standard", "n": 1, "response_format": "b64_json"},
        timeout=300,
    )
    if r.status_code != 200:
        raise RuntimeError(f"{r.status_code}: {r.text[:300]}")
    d = r.json()["data"][0]
    if "b64_json" in d:
        return base64.b64decode(d["b64_json"])
    return requests.get(d["url"], timeout=120).content

only = sys.argv[1:] or list(PROMPTS)
for slug in only:
    out = os.path.join(DEMOS, slug, "assets", "hero.jpg")
    prompt = PROMPTS[slug]
    try:
        data = gen("gpt-image-1", prompt)
    except Exception as e:
        print(slug, "gpt-image-1 fail:", str(e)[:160])
        try:
            data = gen("dall-e-3", prompt)
        except Exception as e2:
            print(slug, "dall-e-3 fail:", str(e2)[:160])
            continue
    tmp = out + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    # конвертация в сжатый jpg
    from PIL import Image
    img = Image.open(tmp).convert("RGB")
    img.save(out, "JPEG", quality=82)
    os.remove(tmp)
    print("OK", slug, os.path.getsize(out) // 1024, "KB")
