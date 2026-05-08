# DESIGN.md: Visual Architect Design System

## Typography
- **Hero/Technical:** 'JetBrains Mono', monospace (for labels, readouts, metadata).
- **UI/Display:** 'Space Grotesk', sans-serif (for headings, navigation).
- **Body:** 'Inter', sans-serif (for long-form bio, descriptions).

## Color Palette (OKLCH)
- **Primary Accent:** Cinematic Cobalt (`#0ea5e9` / `oklch(67.21% 0.176 242.4)`)
- **Backgrounds:** 
  - `bg0`: `oklch(12% 0 0)` (Deep Black)
  - `bg1`: `oklch(16% 0.005 242.4)` (Subtle Blue-tinted Grey)
- **Neutrals:** Toned with Cinematic Cobalt (chroma 0.005-0.01).

## Components
- **Technical Hover Overlays:** YouTube and Project cards show Resolution, FPS, and Duration in a monospaced technical block.
- **Focus Lock Borders:** Cards feature SVG border animations that "draw" on hover.
- **System Pulse:** The AI RENDERING badge uses a soft pulse animation.

## Spacing & Rhythm
- Professional, dense layout typical of NLE software.
- High-contrast hierarchy between technical data and visual content.
