# The anti-slop floor

Slop is the high-probability default, what token statistics produce when
nobody decides: Inter, purple gradients on dark, 16px corners, three equal
cards. The floor governs every invented entity and every choice the
decisions leave open. A **pin** is a value cited to a named source in
`BRAND.json`; pinned evidence outranks this floor wherever they conflict.

The bar: template-predictable is slop; clean-but-conventional is merely
good; aim for intentional and distinctive.

## By axis, where no pin decides

- **Typography.** A distinctive, context-appropriate face, declared, never
  a stack that silently falls through to a default. Weights in
  tension (100/200 against 800/900), size jumps of 3x or more. Display
  faces never set body copy. Emphasis lives inside the family, italic or
  a weight jump of the same face; a lone serif word planted in a sans
  headline is the prior reaching for instant sophistication, unless a pin
  shows exactly that move.
- **Color.** A restricted palette, one punchy hue plus one heavy neutral,
  or five-plus in real balance, at 60/30/10, sharing an undertone, with
  neutrals tinted toward the brand hue (chroma 0.005–0.015). Taper chroma
  as lightness nears either extreme: `oklch(95% 0.02 H)`, never `0.18`,
  decide in oklch, record in `BRAND.json` as uppercase hex.
  Blue ~250 and warm orange are the reflex AI brand hues; reaching for
  either takes a justification from the brief. AA contrast: 4.5:1 body,
  3:1 large.
- **Layout.** Full-canvas bleed with contained reading zones, 70/30
  asymmetry, a spacing rhythm (dense → calm → dense), one focal element
  per view. Sections are chapters with mood shifts, never stacked slides;
  let the fold leak a peek of the next section. Proximity is hierarchy:
  tight groups against open gaps. The nav is one slim ribbon, logo
  x-height matched to the nav text. The hero resolves inside the first
  viewport at 1440: headline holds to two lines, the primary action shows
  unscrolled, content enters in the top fifth, surplus air above the
  headline is a bug, not restraint, and a three-line headline was a type
  scale error before it was a copy error. No layout family appears three
  sections running; two sections that could swap positions unnoticed
  share one family.
- **Components.** Restrained surfaces, 0–6px radii, all eight states
  (default/hover/focus/active/disabled/loading/error/success), visible
  `:focus-visible`, ≥44px touch targets. Border or shadow, one — never the
  ghost card wearing both. A grid holds exactly as many cells as there is
  content — a filler tile or a duplicated card to square the row means the
  grid shape is wrong: reshape to headliner-plus-support, never pad. Proof
  logos are real inline-SVG marks (an invented client earns an invented
  monogram in the system), never a row of styled text.
- **Motion.** Durations 100/300/500ms tied to purpose; exits ≈75% of
  entrances; out-quart `cubic-bezier(0.25,1,0.5,1)`; spend motion on
  micro-feedback plus the one signature, not page-wide transitions.
  `prefers-reduced-motion` honored.
- **Copy.** Specific claims in the declared voice, every claim traceable
  to the client; the harvested specimen phrases set one register and every
  new string is written inside it, mono-metadata, editorial prose, and
  marketing punch don't share a scroll unless a studied source braids
  exactly that mix. Headers lead with the subject; section labels do work
  or disappear ("Testimonials", never "Field notes", performative-
  craftsman warmth is the prior wearing a costume). Where no pin decides,
  a section states one thing: headline under eight words, body under
  twenty-five, one visual or one action. One intent, one label: contact is
  one phrase repeated verbatim nav-to-footer, and a primary CTA holds to
  three words. A quote is a glance, three lines cut to the sentence that
  earned its pin, attributed name **and** role. A page samples, it never
  inventories: the three-to-five items that earn the scroll plus a route
  to the rest.
- **Invented particulars.** Every invented name, metric, or address reads
  lived-in and locale-plausible, 47.2%, never a suspicious round 50%; a
  surname the register would actually meet. Precision the client never
  claimed is a fabricated atom.
- **Imagery.** The corpus decides what media this register carries: study
  what the references actually ship, photography and its treatment,
  illustration, texture, or pure type, and match it. If the references
  carry photography and the page ships none, the resemblance is broken,
  however clean the type. When the corpus splits photo against pure type,
  the brief's subject casts the deciding vote: a physical, atmospheric
  subject, a venue, a festival night, food, objects, people, takes
  photography; only an abstract or interface subject earns pure type. And
  "self-contained" means one FILE, never zero photographs: seeded
  placeholder URLs and embedded data-URIs are both self-contained,
  dropping the corpus's photography because the deliverable is a single
  file is an evasion, not a reading. And a seeded placeholder is a random
  photograph: the seed names your intent, not the pixels. LOOK at what
  each seed actually returns and keep only images that can honestly sit
  under their caption, a caption never claims what the pixels don't
  show; when no seed cooperates, crop tighter, treat harder, or caption
  looser. When photography is called for: an image-gen
  tool if one is available, else seeded placeholder photography
  (`https://picsum.photos/seed/<descriptive-seed>/<w>/<h>`, the seed
  naming the shot: `silo-river-dusk`) with the register's treatment
  applied in CSS (grayscale, duotone, grain). Photography is itself a
  facet: braid one page-wide image recipe, aspect ratios, crop
  discipline, grade, so every frame ships through the same treatment.
  Every image declares its box in the markup (width/height or
  aspect-ratio) so the loading page and the settled page are the same
  page; hero media eager, below the fold lazy. A purely typographic hero
  is a legitimate move only when a studied reference makes it, and a
  fake product UI built from styled divs is never photography's
  substitute: real image, generated image, or nothing.
- **Responsive.** Mobile-first `min-width` queries at content-driven
  breakpoints, `clamp()` for fluid values, `(hover: hover)` gating hover
  states, real input types, `font-display: swap`. Adapt the presentation;
  never amputate access.
- **Dark surfaces.** Elevation by lighter greys (`#121212 → #1E1E1E →
  #2C2C2C`), brand desaturated 20–30%, text at 87/60/38 opacity tiers
  resolved to solid tokens.

## Hard bans: a pin can overrule these; a habit cannot

- Invented names of the Lumina/NovaCraft/Zenith family and -ai/-io/-ly
  recombinations.
- More than two card-grid sections; more than three layout families on
  one page (a family: the shared skeleton two sections would swap
  unnoticed).
- Product UI faked from styled divs, mock terminals, dashboards, chat
  windows, contribution-graph clones. Every depicted interface is a real
  capture or a working miniature whose anatomy traces to a pin; a widget
  no source shows is the prior showing off.
- The interchangeable invented persona, a stock first-name-plus-title
  testimonial beside an initials circle. Voices come from the brief or
  the client's material; when neither supplies a person, the section has
  not earned its place.
- A second marquee. One ticker is a signature placed where a studied
  source shows the pattern; the second is the prior filling silence with
  movement.
- The hero-metric template (big number, small label, supporting stats).
- Gradient text; colored side-stripes on cards; decorative blobs;
  emoji-as-icon; clichéd icon metaphors.
- Eyebrow labels above headings; section numbers that carry no
  information; a second arrow style.
- Alpha as a color factory: `rgba` washes over varying grounds make
  contrast unpredictable, declare explicit overlay tokens per surface,
  resolve muted text to solid hexes, reserve transparency for states that
  must see through.
- Hardcoded one-off colors: every color flows through semantic tokens
  declared over primitives.
- Monospace as a "technical" costume, mono sets code, data, and
  measurement.
- Minimalism-by-omission and could-be-anyone corporate: emptiness is not
  minimalism, genericness is not neutrality; take the register's stance.
