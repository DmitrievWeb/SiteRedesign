# Sequel — Style Reference (рабочая выжимка)
> Private screening after dark — a single warm lamp in an unlit cinema. Theme: dark.

## Цвета (только эти!)
--void:#000000 (канвас, всё строится НА войде) · --white:#ffffff (текст) ·
--charcoal:#202020 (карточки — единственная ступень высоты, БЕЗ теней) ·
--graphite:#333333 (хайрлайны, рамки бейджей) · --cream:#f5f5f0 (ЕДИНСТВЕННАЯ заливка CTA) ·
--smoke:#999999 (вторичный текст). Хроматических цветов НЕТ вообще — 0% colorfulness.

## Типографика (VisueltPro→Inter, Bradford→Playfair Display Italic)
- Заголовки: вес 300 на 54px (шёпот) или 500 на 57–128px; НИКОГДА не bold(700+).
- Display ≥57px: tracking -0.05em. Body: 16px/400 минимум. 
- Лейблы/бейджи: 10–13px UPPERCASE tracking +0.03..0.08em.
- Одно эмоциональное слово в заголовке — Bradford(Playfair) italic, тем же кеглем, инлайн, lowercase.

## Формы
Кнопки/бейджи/чипы: radius 9999px (pill). Карточки/фото: 10px. Инпуты: 0.
Тени ТОЛЬКО две: под cream-кнопкой rgba(0,0,0,.15) 0 4px 20px; glass-бейдж:
rgba(0,0,0,.35) 0 10px 30px + inset rgba(255,255,255,.08) 0 1px 0.

## Компоненты
- Primary pill: bg #f5f5f0, текст #000, 16px/500, padding 0 24px.
- Ghost pill: прозрачный, 1px #fff бордер, текст #fff.
- Frosted badge: rgba(200,200,200,.1) + backdrop blur(20px) saturate(1.4), 11px caps.
- Cinematic card: фото full-bleed, radius 10, текст поверх нижнего скрима
  linear-gradient(transparent→rgba(0,0,0,.55) низ 40%) — единственный градиент системы.
- Hero: фотография И ЕСТЬ фолд; заголовок снизу-слева; круглый play/акцент снизу-справа.

## Do / Don't
DO: канвас строго #000; карточки #202020 тоном, не тенью; caps-лейблы с трекингом.
DON'T: хром-цвета; тени на карточках; бордеры #fff (только #333); вес >500 или <300
в заголовках; текст на фото без скрима; body <16px.

## Motion
0.2–0.3s cubic-bezier(.625,.05,0,1) — slow-out, как медленный зум киностилла.
Только opacity/transform. Никаких spring/bounce.
