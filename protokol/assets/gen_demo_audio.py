# -*- coding: utf-8 -*-
"""Генерация демо-аудио совещания для лендинга: OpenAI TTS, разные голоса на спикеров,
склейка в один mp3 + реальные тайминги реплик (JSON) для синхронной подсветки на лендинге."""
import base64, json, os
import requests
from mutagen.mp3 import MP3

KEY = None
with open(os.path.expanduser("~") + r"\Desktop\WBAdsAgent\.env", encoding="utf-8") as f:
    for line in f:
        if line.startswith("OPENAI_API_KEY="):
            KEY = line.split("=", 1)[1].strip()

OUT = os.path.dirname(__file__)
TMP = os.path.join(OUT, "_parts")
os.makedirs(TMP, exist_ok=True)

# голос по спикеру (OpenAI TTS gpt-4o-mini-tts)
VOICE = {"Ведущий": "onyx", "Маша · фронт": "nova", "Дима · бэк": "echo", "Лена · мкт": "shimmer"}

LINES = [
    ("Ведущий",      "Коллеги, привет. Короткий синк по запуску нового кабинета. Маша, что по фронту?"),
    ("Маша · фронт", "Почти закрыли вёрстку дашборда, осталась адаптивка под мобильные и пара багов с графиками. К четвергу будет."),
    ("Ведущий",      "К четвергу — точно или «надеюсь»?"),
    ("Маша · фронт", "К четвергу вечером закоммичу, в пятницу с утра можно тестировать."),
    ("Ведущий",      "Дима, по бэкенду — успеваем с биллингом?"),
    ("Дима · бэк",   "Интеграция с платёжкой готова, но старые подписки надо мигрировать, а маппинга тарифов нет. Нужно решение от продукта."),
    ("Ведущий",      "Предлагаю старые тарифы заморозить, текущих оставить до конца оплаченного периода. Возражения?"),
    ("Дима · бэк",   "Меня устраивает. Миграция по этому принципу — к следующей среде."),
    ("Ведущий",      "Лена, лендинг к запуску?"),
    ("Лена · мкт",   "Черновик готов, жду финальные скриншоты кабинета для первого экрана."),
    ("Ведущий",      "Маша скинет скриншоты в пятницу. Лена — собрать лендинг до понедельника и запустить тест рекламы, полторы тысячи в день."),
    ("Лена · мкт",   "Поняла, к понедельнику соберу и запущу."),
]

def tts(text, voice, path):
    r = requests.post("https://api.openai.com/v1/audio/speech",
        headers={"Authorization": f"Bearer {KEY}"},
        json={"model": "gpt-4o-mini-tts", "input": text, "voice": voice, "speed": 1.05},
        timeout=120)
    r.raise_for_status()
    with open(path, "wb") as f:
        f.write(r.content)

timings, t = [], 0.0
combined = b""
for i, (who, text) in enumerate(LINES):
    part = os.path.join(TMP, f"{i:02d}.mp3")
    if not os.path.exists(part):
        tts(text, VOICE[who], part)
        print("tts", i, who)
    dur = MP3(part).info.length
    timings.append({"t": round(t, 2), "w": who, "s": text})
    t += dur + 0.35  # небольшая пауза между репликами
    with open(part, "rb") as f:
        combined += f.read()

with open(os.path.join(OUT, "meeting.mp3"), "wb") as f:
    f.write(combined)
with open(os.path.join(OUT, "meeting.json"), "w", encoding="utf-8") as f:
    json.dump({"dur": round(t, 1), "lines": timings}, f, ensure_ascii=False, indent=1)

print(f"\nГОТОВО: meeting.mp3 ({len(combined)//1024} КБ), длительность ~{t:.0f}с, реплик {len(timings)}")
print("Тайминги:", [x["t"] for x in timings])
