---
name: Heritage Hearth
colors:
  surface: '#fbf9f1'
  surface-dim: '#dcdad2'
  surface-bright: '#fbf9f1'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f4ec'
  surface-container: '#f0eee6'
  surface-container-high: '#eae8e0'
  surface-container-highest: '#e4e3db'
  on-surface: '#1b1c17'
  on-surface-variant: '#5a403e'
  inverse-surface: '#30312c'
  inverse-on-surface: '#f3f1e9'
  outline: '#8e706d'
  outline-variant: '#e2beba'
  surface-tint: '#b52424'
  primary: '#8f000d'
  on-primary: '#ffffff'
  primary-container: '#b22222'
  on-primary-container: '#ffc8c2'
  inverse-primary: '#ffb4ac'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#5d3f00'
  on-tertiary: '#ffffff'
  tertiary-container: '#7c5500'
  on-tertiary-container: '#ffce7f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad6'
  primary-fixed-dim: '#ffb4ac'
  on-primary-fixed: '#410003'
  on-primary-fixed-variant: '#92030f'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#ffdeac'
  tertiary-fixed-dim: '#ffba38'
  on-tertiary-fixed: '#281900'
  on-tertiary-fixed-variant: '#604100'
  background: '#fbf9f1'
  on-background: '#1b1c17'
  surface-variant: '#e4e3db'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md-mobile:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  title-lg:
    fontFamily: Montserrat
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.5'
  body-lg:
    fontFamily: Montserrat
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Montserrat
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Montserrat
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

This design system captures the essence of Raksha Bandhan through a "Modern Heritage" aesthetic. It balances the warmth of traditional Indian celebrations with the slick, high-conversion functionality of premium e-commerce. The target audience seeks high-quality, thoughtful gifts that honor familial bonds without feeling dated or cluttered.

The visual style is **Corporate Modern with Tactile Accents**. It utilizes clean layouts and ample whitespace to ensure the products remain the focus, while injecting "festive soul" through intricate patterns and a rich, royal color palette. The emotional response should be one of joy, trust, and premium craftsmanship.

## Colors

The palette is rooted in the traditional significance of the festival.

- **Primary (Deep Crimson):** Used for key calls-to-action, branding, and high-emphasis elements. It conveys passion and the sacred thread of protection.
- **Secondary (Royal Gold):** Used for decorative accents, premium badges, and subtle dividers to elevate the "luxury" feel.
- **Tertiary (Marigold Orange):** Employed for attention-grabbing notifications or secondary buttons, evoking the brightness of festive marigolds.
- **Backgrounds (Warm Cream/Parchment):** Avoid pure white to maintain a soft, inviting, and organic feel that complements skin tones in lifestyle photography.
- **Accent (Emerald Green):** Used sparingly for success states or to highlight "Eco-friendly" or "Handmade" credentials, providing a necessary cool contrast to the warm palette.

## Typography

The typographic hierarchy creates an editorial feel. **Playfair Display** provides the "Heritage" element, used for product names, section headers, and storytelling hero banners. It should be typeset with slightly tighter letter spacing for a modern look.

**Montserrat** handles all functional e-commerce tasks. Its geometric clarity ensures that prices, product descriptions, and checkout steps are highly legible. Use `label-bold` for navigation items and small badges to maintain a crisp, professional edge.

## Layout & Spacing

The layout follows a **Fluid Grid** model with a maximum container width of 1280px to prevent excessive line lengths on wide monitors.

- **Desktop:** 12-column grid with 24px gutters. Use generous vertical "stack" spacing (48px+) between homepage sections to allow the decorative patterns to breathe.
- **Mobile:** 2-column grid for product listings to maximize visual density while maintaining accessibility. 16px side margins are required.
- **Rhythm:** Utilize the 8px base unit for all component internal spacing (padding/margins). Consistency in these increments creates a sense of "premium" order.

## Elevation & Depth

This design system uses **Tonal Layers** combined with **Ambient Shadows** to create a sophisticated sense of depth.

- **Surfaces:** Use the "Parchment" shade for secondary containers (like cards) against the "Warm Cream" background to create subtle distinction without harsh lines.
- **Shadows:** Avoid pure black shadows. Use a "Deep Crimson" or "Deep Brown" tint at very low opacity (5-8%) for shadows. This keeps the elevation feeling warm and integrated rather than "floating" on a clinical digital plane.
- **Borders:** Use a thin 1px border in a slightly darker "Parchment" shade for input fields and cards to ensure structural clarity on all screens.

## Shapes

The shape language is **Rounded**, reflecting the soft and friendly nature of family bonds.

- **Standard Elements:** Buttons, input fields, and small cards use a 0.5rem (8px) corner radius.
- **Feature Elements:** Product images in hero sections or special promotional banners can use `rounded-xl` (1.5rem / 24px) to feel more like high-end gift packaging.
- **Decorative:** Subtle Henna or Mandala patterns should be used as background masks or corner overlays, never as the primary container shape, to keep the UI clean and functional.

## Components

- **Buttons:** Primary buttons use the Deep Crimson background with White text and a subtle 2px Gold bottom border (simulating depth). Secondary buttons use an outline style in Royal Gold.
- **Cards:** Product cards should have a "Soft Parchment" background and no visible border unless hovered. On hover, the ambient shadow increases slightly and the image scales 2%.
- **Chips/Badges:** Use "Marigold Orange" for "Best Seller" and "Emerald Green" for "In Stock." Shape should be pill-styled (`rounded-xl`).
- **Inputs:** Clean, 1px bordered fields with Montserrat body-sm text. Focus state should change the border color to Deep Crimson with a soft outer glow.
- **Specialty Component - "The Rakhi Ribbon":** A decorative divider component that uses a repeating Henna-inspired pattern in low-opacity Gold to separate major sections of the page.
- **Lists:** Bullet points in product descriptions should be replaced with small "Marigold" flower icons or simple geometric diamonds to maintain the festive theme.
