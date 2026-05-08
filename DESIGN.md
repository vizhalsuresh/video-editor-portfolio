---
name: Suresh Vizhal Portfolio
description: A high-end cinematic command center for a master video editor.
colors:
  primary: "#0ea5e9"
  secondary: "#a855f7"
  tertiary: "#3ecf6e"
  neutral-bg: "#050505"
  neutral-text: "#f5f5f7"
  warning: "#f04545"
  accent-orange: "#e8854a"
  accent-teal: "#3ecfb8"
typography:
  display:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(2rem, 8vw, 6rem)"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: "4px"
  body:
    fontFamily: "Inter, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.6
  ui:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "13px"
    fontWeight: 500
    letterSpacing: "0.05em"
  mono:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: "12px"
rounded:
  sm: "2px"
  md: "4px"
  lg: "8px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "40px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral-bg}"
    rounded: "{rounded.sm}"
    padding: "8px 20px"
  card-project:
    backgroundColor: "#141414"
    rounded: "{rounded.md}"
    padding: "16px"
---

# Design System: Suresh Vizhal Portfolio

## 1. Overview

**Creative North Star: "The Digital Command Center"**

This system replicates the precision and authority of professional NLE (Non-Linear Editing) software like Premiere Pro and After Effects. It is a high-density, technical workspace designed for power users and creative directors. The aesthetic is built on deep blacks, sharp UI elements, and vibrant "signal" colors that indicate status, workflow, and technical mastery. It explicitly rejects "normal website" patterns in favor of a specialized tool-like interface.

**Key Characteristics:**
- **High Information Density**: UI elements are compact, utilizing every pixel for technical metadata or navigation.
- **Systematic Accents**: Color is never decorative; it represents specific software (PR, AE) or programmatic status (AI, Code).
- **Monolithic Typography**: Large, all-caps display type contrasts with precise, monospace technical data.

## 2. Colors

The palette is a high-contrast "Command Mode" spectrum, anchored in deep obsidian with electric functional accents.

### Primary
- **Command Center Cyan** (#0ea5e9): The primary action and focus color. Used for selection states, primary buttons, and the Visual Architect system identity.

### Secondary
- **Neural Purple** (#a855f7): Represents complex motion graphics and After Effects workflows. Used for secondary highlights and specialized project tags.

### Tertiary
- **Logic Green** (#3ecf6e): Indicates success, "ready" states, and completed renders.

### Neutral
- **Obsidian Base** (#050505): The foundational background color. Pure black is avoided in favor of deep, tinted greys (#0c0c0c, #141414) to maintain depth.
- **Titanium White** (#f5f5f7): The primary text color, optimized for readability against dark backgrounds.

**The Signal Rule.** Accent colors are used only to denote functional meaning or software alignment. A screen should never be "colorful" for the sake of it; colors must represent data or state.

## 3. Typography

**Display Font:** Bebas Neue
**Body Font:** Inter
**UI Font:** Space Grotesk
**Mono Font:** JetBrains Mono

**Character:** A pairing of industrial-strength headers and high-precision UI fonts. The contrast between the massive, compressed display type and the tiny, sharp monospace type creates a feeling of professional scale.

### Hierarchy
- **Display** (400, clamp(2rem, 8vw, 6rem), 0.9): Hero headlines, massive name reveals, and section headers.
- **Headline** (700, 24px, 1.2): Project titles and major UI panel headers.
- **Body** (400, 16px, 1.6): Biographies and long-form descriptions. Max line length: 70ch.
- **UI Label** (500, 11px, 0.05em, Uppercase): Buttons, navigation items, and toolbar labels.
- **Mono Data** (400, 10px, 1.0): Timecodes, file sizes, technical metadata, and "code" logs.

## 4. Elevation

The system is primarily flat and structural, relying on tonal layering rather than shadows to convey hierarchy. Depth is created through "lit" borders and subtle background shifts.

**The Lit-Edge Rule.** Surfaces are differentiated by 1px borders (#2a2a2a) that act as "rim lights," separating panels in the dark environment. Shadows are used exclusively for modals and expanded cards to create a "floating" effect.

## 5. Components

### Buttons
- **Shape:** Sharp (2px radius)
- **Primary:** Command Center Cyan background, All-caps UI Label type, 8px 20px padding.
- **Tool Button:** Square (28px), ghost background, icons only. Turns primary on active/hover.

### Project Cards
- **Style:** Dark background (#141414), 1px subtle border.
- **Interaction:** On hover, a "scanning" line animation (CSS) moves vertically across the card, and the image scales slightly (1.05x).

### Timeline Clips
- **Style:** Colored blocks (matching category color), 3px radius.
- **Metadata:** White, 10px bold text, centered.
- **Active State:** 2px white outline to indicate "current selection."

## 6. Do's and Don'ts

### Do:
- **Do** use `JetBrains Mono` for any data that feels like "system output" or metadata.
- **Do** utilize `Bebas Neue` for large-scale impact, but keep it all-caps.
- **Do** use tinted greys for backgrounds to maintain a premium feel.

### Don't:
- **Don't** use standard rounded buttons or bubbly UI; keep corners sharp and professional.
- **Don't** use generic gradients; prefer solid "signal" colors or very subtle tonal shifts.
- **Don't** create a "normal website walkthrough" feel; everything should feel like a piece of high-end software.
