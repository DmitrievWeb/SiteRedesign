# Aurora UI — Style Reference (рабочая выжимка)
> Northern Lights: mesh-градиенты, медленное движение. Light/Dark: оба.

## Цвета
--primary:#0080FF (electric blue) · --secondary:#FF1493 (magenta) · --tertiary:#00FFFF (cyan).
Насыщенность акцентов ≤80%. Чистый #000 запрещён — off-black/charcoal.
Градиенты: большие текучие mesh/CSS-градиенты из этих трёх цветов.

## Типографика
Системный стек (-apple-system) или Inter. Hero clamp(2.5rem,5vw,4rem)/700 tight tracking.
Body 1rem/1.6 вес 400, max 72ch. Лейблы 0.75rem/500 с лёгким трекингом. Моно: JetBrains Mono.

## Motion (сигнатура)
Анимация градиентов циклами 8–12s (медленно! не мельтешить). Entry: fade + translateY(16px→0)
480ms ease-out, каскад списков по 100ms. Hover: scale(1.03) + тень 200ms.
Анимировать ТОЛЬКО transform/opacity.

## Layout
Grid, контейнер 1280px, отступы секций clamp(4rem,8vw,8rem). Hero: сплит текст-слева/визуал-справа.
Фичи: зигзаг (НЕ три равные колонки). Всё складывается <768px.

## Компоненты
Primary кнопка: radius 0.75rem, заливка primary, hover darken 8% + lift, active -1px press, вес 600.
Ghost: 1.5px muted бордер. Карточки: 0.75rem, тень 0 2px 12px rgba(0,0,0,.06), 1px бордер.
Инпуты: лейбл сверху, focus-ring 2px accent offset 2px.

## Don't
Эмодзи в UI (только иконки Lucide/Heroicons); #000000; перенасыщенные акценты;
3 равные колонки; h-screen (использовать min-h-[100dvh]); клише «Elevate/Seamless/Unleash».
