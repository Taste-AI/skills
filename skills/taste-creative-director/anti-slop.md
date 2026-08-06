# Anti-slop floor

The floor governs every `INVENTED` entity and every choice the pins leave
open: spacing, states, contrast, motion feel, dark variants. Pinned evidence
outranks it wherever they conflict: a source whose identity is purple-on-white
keeps it. This floor is why an undefined entity must never be improvised.


**What slop is:** the high-probability default, what token statistics
produce when nobody decides (Inter, purple gradients, 16px corners, three
equal cards). It reads generic, erodes trust, and makes the product
interchangeable. **The bar:** template-predictable is slop;
clean-but-conventional is merely good; aim for intentional, distinctive,
design-driven — the grid is a tool, not a cage. Gut check: good design
mimics uncoated ink on paper, not raw screen light — conditioned color,
restraint, intention.

Slop → great, by axis (apply wherever no pin decides):

- **Typography**: default Inter/Roboto/knee-jerk Space Grotesk → a
  distinctive, context-appropriate face; weights clustered 400–600 → tension
  (100/200 against 800/900); ≤1.5× size jumps → 3×+ (16px body → 48px+
  headlines). Type may break the grid or become the focal element; display
  faces never set body copy.
- **Color**: `#000`/`#FFF` on big surfaces, 4+ saturated hues, gradient
  buttons, accidentally-tinted neutrals → restricted palette (1 punchy + 1
  heavy neutral, *or* 5+ perfectly balanced), 60/30/10 distribution, shared
  undertone, axis-aligned neutrals (`F3F3F0`), AA contrast (4.5:1 body /
  3:1 large text).
- **Layout**: centered safe-box, 50/50 splits, identical section spacing →
  full-canvas bleed with contained reading zones, 70/30 asymmetry, spacing
  rhythm (dense→calm→dense); one high-contrast focal element lands the eye
  per view. Sections read as chapters with deliberate mood shifts between
  them, never identical stacked slides.
- **Interaction**: neon glows, glassmorphism, gradient borders, 12–16px+
  radii, floaty/bouncy motion, only default+hover → restrained surfaces,
  2–6px (or 0) radii, snappy `ease-out` on transform/opacity, **all eight
  states** (default/hover/focus/active/disabled/loading/error/success),
  visible `:focus-visible`, ≥44px targets, `prefers-reduced-motion` honored.
- **Copy**: slop verbs (Empower/Transform/Unleash), invented -ai/-io/-ly
  names, fabricated "Trusted by 10,000+" → specific copy in the declared
  voice, every claim traceable to the client.
- **Dark mode**: shadows for elevation, saturated brand color, flat text
  brightness → lighter greys for elevation (`#121212`→`#1E1E1E`→`#2C2C2C`),
  desaturate brand 20–30%, text opacity tiers 87/60/38, drop one font weight
  step.

Measured defaults: numbers to reach for when no pin decides:

- **Motion:** durations 100/300/500ms tied to purpose; exits ≈75% of their
  entrances; feedback never over 500ms; out-quart
  `cubic-bezier(0.25,1,0.5,1)`; bounce or elastic only when a pin proves it.
  Spend motion on scattered micro-feedback (hover, input, reveal) plus the
  one signature — not page-wide transitions.
- **Color conditioning:** great palettes rarely touch the corners of the
  color space — condition values toward the center/bottom, and tint neutrals
  toward the brand hue at chroma 0.005–0.015.
- **Type measure:** body 65–75ch; display type tops out around 6rem; more
  space above a heading than below it.
- **Icons:** one family and stroke weight, sized per context (16/20/24px) —
  emojis and clichéd metaphors (lightbulb-for-idea, rocket-for-growth) are
  not icons.
- **Status colors:** keep their jobs — success green, error red, warning
  amber; a green destructive action confuses the user's subconscious.

Hard bans: a pin can overrule any of these; a habit cannot:

- Enumerative section headers and two-part "X. Y." taglines ("Ship bolder.
  Faster."). Headers lead with the subject.
- Invented brand names of the Lumina / NovaCraft / Zenith / Pulse family and
  -ai/-io/-ly recombinations.
- More than two card-grid sections per page; a page draws from at least four
  distinct layout primitives.
- Buttons that pass contrast against the page but fail against their
  container — ≥4.5:1 against the actual ground, with `.on-dark` variants for
  dark bands.
- Headlines starting left of the gutter; negative `margin-left` only when a
  pin proves the gutter-break and it pairs with a deliberate full-bleed move.
- A second arrow style: one `.arrow-mark` class, one family, one scale.
- Typographic play (an italic accent word inside a caps headline, and kin)
  without a pin showing that exact move — zero variation is restraint, not
  slop.
- An eyebrow or kicker label above a heading — the heading carries its own
  weight.
- Section numbers (01 / 02 / 03) unless the sequence itself carries
  information the reader needs.
- The hero-metric template: big number, small label, supporting stats,
  accent.
- Gradient text — emphasis comes from weight or size.
- A colored side-stripe (`border-left`) on cards, callouts, or alerts.
- Double-declared elevation (the ghost card: a 1px border under a wide soft
  shadow) — border or shadow, one; hard offset shadows belong only to a
  neobrutalist world a pin proves.
- Monospace as a "technical" costume — mono sets code, data, and
  measurement.
- Hardcoded one-off colors (`text-white`, inline `#000`) — every color
  flows through the declared semantic tokens (`--text-primary`,
  `--surface-elevated`).
- `border: 1px solid gray` and default box-shadows as filler — commit to a
  distinctive treatment or remove the line entirely.
- Decorative blobs and abstract filler shapes — a section that feels empty
  has a content or layout problem, not a missing ornament.
- Minimalism-by-omission and could-be-anyone corporate — emptiness is not
  minimalism, genericness is not neutrality; take the register's stance.

**Verbatim values.** Where a pin supplies a value, transplant it exactly: hex
as extracted, gradient `css_code` and `box-shadow` strings pasted whole, real
font files loaded from `technical.file_url` (when `font_variation_settings`
is present it is the real weight, not `font_weight`). The screenshot wins on
placement, proportion, spacing, and mood; extracted token values win on
values — never re-read a value off pixels.
