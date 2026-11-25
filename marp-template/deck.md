---
marp: true
theme: default
size: 16:9
paginate: true
title: Your awesome title
description: One-sentence description of the talk
footer: "**Harvard MaDSys** [madsys.seas.harvard.edu](https://madsys.seas.harvard.edu/)"
style: |
  /* MaDSys slide theme, measured from the MaDSys PowerPoint template (template.potx, 13.33 × 7.5 in):
     1 in = 96 px and 1 pt = 1.333 px at Marp's 1280 × 720.
     Fonts: Aptos Display (titles) and Aptos (text), as in the template; install both, or the deck
     falls back to Helvetica Neue / Arial. Colours: the template's theme (accent1 crimson #A51C30,
     dk2 navy #0E2841, accent2 orange #B04E12, accent3 green #196B24) and its footer colours. */
  section {
    --crimson: #A51C30; --crimson-dark: #7A1524; --crimson-bar: #C7405A; --navy: #0E2841;
    --orange: #B04E12; --green: #196B24; --brown: #8F3E0E; --grey: #595959; --slate: #6B777D;
    --silver: #C4CCD1; --mauve: #96607D;
    --ink: #000000; --muted: #595959; --bg: #F7F7F7; --code-bg: #E8E8E8; --tint: #F0E6E7;
    --font-title: "Aptos Display", "Aptos", "Helvetica Neue", Helvetica, Arial, sans-serif;
    --font-text: "Aptos", "Helvetica Neue", Helvetica, Arial, sans-serif;
    box-sizing: border-box; display: flex; flex-direction: column; justify-content: flex-start;
    /* the template's title and body placeholders: x 88–1192 px with 9.6 px insets; body ends at 644 px */
    padding: 43px 98px 76px 98px;
    background: var(--bg); color: var(--ink);
    font-family: var(--font-text); font-size: 37.33px; line-height: 1.1;
    /* footnote counters; Marp's container-type: size would restart them in every paragraph */
    counter-reset: fnmark footnote; container-type: normal;
  }
  /* slide title: Aptos Display 44 pt, black, left, centred in a 130 px band (the title placeholder) */
  section h1, section h2 { display: table-cell; vertical-align: middle; width: 1084px; height: 130px;
    margin: 0; padding: 0; border: none; font-family: var(--font-title); font-size: 58.67px;
    font-weight: 400; line-height: 1.08; color: var(--ink); }
  /* the gap between the title and body placeholders; !important beats the blocks' own margins */
  section :is(h1, h2) + * { margin-top: 24px !important; }
  section :is(h1, h2) img { height: 0.66em; vertical-align: -0.06em; margin-left: 4px; }
  section h3 { margin: 10px 0 8px; font-family: var(--font-title); font-size: 32px; font-weight: 600;
    line-height: 1.15; color: var(--crimson); }
  /* body: Aptos 28 / 24 / 20 pt, Arial bullets, 10 pt (level 1) and 5 pt (levels 2–3) before each item */
  section p { margin: 0 0 13.33px; }
  section ul, section ol { margin: 0 0 13.33px; padding-left: 24px; }
  section ul { list-style: none; }
  section ul > li { position: relative; }
  section ul > li::before { content: "•"; position: absolute; left: -24px; font-family: Arial, sans-serif; }
  section ol { padding-left: 1.25em; list-style-type: decimal; }
  section :is(ul, ol) ol { list-style-type: decimal; }
  section li { margin: 0; }
  section li + li { margin-top: 13.33px; }
  section li > :is(ul, ol) { margin: 6.67px 0 0; padding-left: 48px; font-size: 32px; }
  section li li + li { margin-top: 6.67px; }
  section li li > :is(ul, ol) { font-size: 26.67px; }
  section li img { height: 0.8em; vertical-align: -0.12em; }
  /* highlight: <mark>…</mark> is the template's crimson run (accent1) */
  section mark { background: none; color: var(--crimson); }
  section a { color: var(--crimson-dark); text-decoration: none; }
  section code { font-size: 0.85em; padding: 0 0.15em; background: var(--code-bg); border-radius: 3px; }
  section pre { margin: 0 0 13px; padding: 12px 16px; font-size: 20px; line-height: 1.35;
    background: var(--code-bg); border-radius: 4px; }
  section pre code { padding: 0; font-size: inherit; background: none; }
  /* key message */
  section blockquote { margin: 0 0 14px; padding: 9px 20px; border-left: 6px solid var(--crimson);
    background: var(--tint); color: var(--ink); font-size: 26.67px; line-height: 1.25; }
  section blockquote::before, section blockquote::after { content: none; }
  section blockquote p { margin: 0; }
  /* figures: a paragraph holding only an image */
  section img { background: transparent; }
  section p:has(> img) { margin: 0; text-align: center; }
  section p > img { object-fit: contain; }
  /* source line under a figure */
  section h6 { margin: 8px 0 0; font-size: 16px; font-weight: 400; line-height: 1.3; color: var(--muted); }
  /* booktabs-style tables */
  section table { margin: 4px auto 14px; font-size: 21.33px; line-height: 1.3; border-collapse: collapse;
    border-top: 2px solid var(--ink); border-bottom: 2px solid var(--ink); }
  section table th, section table td { border: none; padding: 5px 14px; background: transparent; }
  section table thead th { border-bottom: 1px solid var(--ink); }
  section table tr, section table tr:nth-child(2n) { background: transparent; border: none; }
  /* two columns: <div class="cols"> <div>…</div> <div>…</div> </div>, blank lines inside each <div> */
  section .cols { display: grid; grid-template-columns: 1fr 1fr; column-gap: 40px; align-items: center; }
  section .cols > div > :last-child { margin-bottom: 0; }
  /* LaTeX-style macros, built from HTML that Marp allows by default (no settings needed):
       <span class="definition"><b>Term</b> …</span>  like \begin{definition}[Term]
       <span class="finding"><b>F1</b> …</span>       like \begin{theorem}[F1]
       <span class="question">…</span>                a speech bubble
       text<sup class="fn"></sup> … <span class="footnote">…</span>   like \footnotemark … \footnotetext
     The <b>…</b> at the start is the optional title. To add an environment (e.g. lemma), give it
     a line like definition's and add .lemma after .finding in each :is() list below. */
  section .definition { --env: "Definition"; --env-color: var(--navy); --env-tint: #E4E8ED; }
  section .finding { --env: "Finding"; --env-color: var(--green); --env-tint: #E5EDE6; }
  section :is(.definition, .finding) { display: block; margin: 0 0 12px; padding: 8px 16px;
    border-left: 5px solid var(--env-color); background: var(--env-tint); font-size: 24px; line-height: 1.3; }
  section :is(.definition, .finding)::before { content: var(--env) ". "; font-weight: 700; color: var(--env-color); }
  section :is(.definition, .finding):has(> b:first-child, > p:first-child > b:first-child)::before {
    content: var(--env) " "; }
  section :is(.definition, .finding) > b:first-child,
  section :is(.definition, .finding) > p:first-child > b:first-child { color: var(--env-color); }
  section :is(.definition, .finding) > b:first-child::before,
  section :is(.definition, .finding) > p:first-child > b:first-child::before { content: "("; }
  section :is(.definition, .finding) > b:first-child::after,
  section :is(.definition, .finding) > p:first-child > b:first-child::after { content: "). "; }
  section :is(.definition, .finding, .question) > p:first-of-type { display: inline; }
  section :is(.definition, .finding, .question) > p:last-child { margin-bottom: 0; }
  section :is(.definition, .finding, .question) :is(ul, ol) { margin: 6px 0 0; }
  section :is(.definition, .finding, .question) li + li { margin-top: 2px; }
  section .question { display: block; position: relative; box-sizing: border-box; width: fit-content;
    max-width: 100%; margin: 4px 0 26px; padding: 10px 22px 10px 60px; background: #F4EAE2;
    border: 2px solid var(--orange); border-radius: 18px; font-size: 24px; line-height: 1.3; }
  section .question::before { content: "?"; position: absolute; left: 15px; top: 50%; width: 32px;
    height: 32px; margin-top: -16px; border-radius: 50%; background: var(--orange); color: #ffffff;
    font-size: 22px; font-weight: 700; line-height: 32px; text-align: center; }
  section .question::after { content: ""; position: absolute; left: 32px; bottom: -11px; width: 18px;
    height: 18px; background: #F4EAE2; border-right: 2px solid var(--orange);
    border-bottom: 2px solid var(--orange); transform: rotate(45deg); }
  /* a macro on its own line sits in a paragraph: drop its margin and line breaks */
  section p:has(> :is(.definition, .finding, .question)) { margin: 0; }
  section p:has(> :is(.definition, .finding, .question, .footnote)) > br { display: none; }
  /* footnotes go last on the slide and sit at the bottom; the n-th mark matches the n-th footnote */
  section sup.fn { counter-increment: fnmark; top: -0.7em; margin-left: 1px; font-size: 0.55em;
    font-weight: 700; color: var(--crimson); }
  section sup.fn::before { content: counter(fnmark); }
  section p:has(> .footnote) { margin: auto 0 2px; padding-top: 6px;
    background: linear-gradient(var(--muted), var(--muted)) no-repeat 0 0 / 180px 1px; }
  section p:has(> .footnote) + p:has(> .footnote) { margin-top: 0; padding-top: 0; background: none; }
  section .footnote { display: block; counter-increment: footnote; font-size: 16px; line-height: 1.35;
    color: var(--muted); }
  section:has(sup.fn) .footnote::before { content: counter(footnote); margin-right: 3px; font-size: 0.75em;
    font-weight: 700; line-height: 0; vertical-align: super; color: var(--crimson); }
  /* personal-use badge: a slide not meant for the audience */
  section.personal-use::before { content: "👤  PERSONAL USE"; position: absolute; top: 12px; right: 98px;
    padding: 9px 18px; background: #B91C1C; color: #ffffff; border-radius: 12px; font-size: 20px;
    font-weight: 700; line-height: 1.2; z-index: 10; }
  /* footer and page number as in the template's layouts: a crimson bar, "Harvard MaDSys" in bold
     crimson, a grey dot, then the link in dark crimson ("https://" is added) */
  section footer { left: 69px; right: auto; bottom: 6.33px; height: 26.67px; padding: 0; overflow: visible;
    font-size: 16px; line-height: 26.67px; color: var(--slate); }
  section footer::before { content: ""; position: absolute; left: -18.67px; top: 2.67px; width: 4.67px;
    height: 21.33px; background: var(--crimson-bar); }
  section footer strong { font-weight: 700; letter-spacing: 0.8px; color: var(--crimson); }
  section footer strong::after { content: "·"; margin: 0 0.8em; font-weight: 400; letter-spacing: 0;
    color: var(--silver); }
  section footer a { color: var(--crimson-dark); }
  section footer a::before { content: "https://"; }
  section::after { right: 55.2px; bottom: 6.33px; height: 26.67px; padding: 0; font-family: var(--font-text);
    font-size: 16px; font-weight: 700; line-height: 26.67px; color: var(--crimson); }
  /* compact slides: body one step smaller (24 / 20 / 18 pt), for figure + text slides */
  section.compact p, section.compact li { font-size: 32px; }
  section.compact li > :is(ul, ol) { font-size: 26.67px; }
  section.compact li li > :is(ul, ol) { font-size: 24px; }
  section.compact li + li, section.compact p { margin-bottom: 0; }
  section.compact li + li { margin-top: 8px; }
  /* detail slides: the numbers behind the previous figure */
  section.details h2 { font-size: 40px; color: var(--muted); }
  section.details table { font-size: 18.67px; }
  section.details :is(p, li) { font-size: 21.33px; }
  section.details li + li { margin-top: 4px; }
  /* title slide (the template's Title Slide layout and slide 1): title 60 pt and subtitle 38 pt in
     Aptos Display, name 24 pt, all centred; SEAS logo bottom left, MaDSys logo bottom right */
  section.title { padding: 0; }
  section.title footer, section.title::after { display: none; }
  section.title :is(h1, h2) + * { margin-top: 0 !important; }
  section.title h1 { display: block; position: absolute; left: 169.6px; bottom: 359.5px; width: 940.8px;
    height: auto; font-size: 80px; text-align: center; }
  section.title h3 { position: absolute; top: 381.8px; left: 213.2px; width: 853.6px; margin: 0;
    font-size: 50.67px; font-weight: 400; line-height: 1.08; color: var(--ink); text-align: center; }
  section.title p:not(:has(> img)) { position: absolute; top: 552px; left: 169.6px; width: 940.8px;
    margin: 0; transform: translateY(-50%); font-size: 32px; text-align: center; }
  section.title img[src$="logo_seas.png"] { position: absolute; left: 13px; top: 622.5px;
    width: 339.9px; height: 97.5px; }
  section.title img[src$="logo_madsys.png"] { position: absolute; left: 940.1px; top: 580.5px;
    width: 339.9px; height: 139.5px; }
  /* section divider (the template's Custom Layout): title 66 pt centred, a line of text below */
  section.divider { padding-top: 243.5px; align-items: center; text-align: center; }
  section.divider h1 { font-size: 88px; text-align: center; }
  section.divider h1 + * { margin-top: 56px !important; }
  section.divider p { max-width: 793px; }
---

<!-- _class: title -->

# Your awesome title

### A subtitle

Your name

![Harvard SEAS](figures/logo_seas.png) ![MaDSys](figures/logo_madsys.png)

---

## Content

- Please use illustrations
- **Background**: what the audience needs to know
- **Motivation**: where today's systems fall short
- **Design**: the overview, the key component, a walk-through
- **Evaluation**: the headline result, and why it holds

---

## Background: necessary knowledge

- Please use illustrations
- Assume the audience is an undergraduate in computer science
- Tell people anything they need to know about this talk

<span class="definition"><b>Tail latency</b> The 99th-percentile request latency (p99): one request in a hundred is slower.</span>

---

## Motivation: gap

- Provide today's landscape (state-of-the-art)
  - What people have done
  - Where they fall short
  - Why they do not work
- Show numbers and figures

---

<!-- _class: compact -->

## Today's systems fall over under bursts

![h:290](figures/f01_example_timeseries.png)

- **Bursts** triple the p99 latency of every baseline<sup class="fn"></sup>
- **Ours** stays within 1.4× of its steady-state p99<sup class="fn"></sup>

<span class="footnote">Burst: 55–88 s, at 1.8× the steady-state request rate.</span>
<span class="footnote">Footnotes sit at the bottom of the slide, numbered in the order of the marks.</span>

---

<!-- _class: divider -->
# Design

Overview, key component, and a walk-through

---

## Design 1

- Give an overview
- Different components in the system
- How they interact with each other
  - <mark>Highlight</mark> the one term the audience must keep in mind

---

## Design 2

- Focus on the key component
- Use illustrations with animation
  - Marp has no animations: build the figure up over consecutive slides

---

## Design 3

- Walk through a request / an example
  1. The client sends a request
  2. The scheduler places it on a worker
  3. The worker replies; the scheduler records the latency

---

## Evaluation

- Your system / algorithm beats the state-of-the-art on metric X
- Focus on high-level results and <mark>only show one or two figures</mark>
- Explain the figures in detail
  - Tell the audience what X and Y are, which direction is better, and how to read the figures
  - Show one system at a time
  - Explain the results

---

## F1 · Ours doubles throughput ![](figures/badge_A.svg)

> 1.5–1.9× the throughput of Baseline A, at 0.5–0.6× its p99 latency.

![h:345](figures/f02_example_bars.png)

###### (a) Throughput, higher is better. (b) p99 latency, lower is better. Made-up example data.

---

<!-- _class: details -->

## Details · F1

| workload | Ours (k req/s) | Baseline A | Baseline B | speed-up vs A |
| --- | ---: | ---: | ---: | ---: |
| W1 | 9.1 | 5.2 | 3.8 | 1.75× |
| W2 | 7.4 | 4.9 | 4.4 | 1.51× |
| W3 | 11.2 | 6.0 | 5.1 | 1.87× |
| W4 | 6.3 | 4.1 | 2.9 | 1.54× |

| workload | Ours p99 | Baseline A p99 | Baseline B p99 |
| --- | ---: | ---: | ---: |
| W1 | 38 ms | 71 ms | 95 ms |
| W4 | 64 ms | 120 ms | 151 ms |

- Detail slides hold the numbers behind the previous figure; skip them when presenting.
- Text columns are left-aligned (`---`), numeric columns right-aligned (`---:`).

---

## Evaluation 2

- Show why your system works <mark>← this is the insight people look for</mark>
- Do not add more figures beyond this for talk < 20 min

<span class="finding"><b>F2</b> Most of the gain comes from the key component: without it, the p99 under bursts is within 10% of Baseline A.</span>

---

## More in the paper

<div class="cols">
<div>

- Tell people what else you have done that they might be interested in
- Provide a link and QR code to the paper
- [madsys.seas.harvard.edu](https://madsys.seas.harvard.edu/)

</div>
<div>

![h:300](figures/qr_paper.svg)

</div>
</div>

---

## Summary and takeaway

1. **Use short bullet points**: one claim and its number. ![](figures/badge_A.svg)
2. **Second takeaway**: the supporting number. ![](figures/badge_B.svg) ![](figures/badge_C.svg)
3. **Add your name and contact**: Your Name · you@seas.harvard.edu

<span class="question">Questions?</span>

---

## Definitions, findings, questions

<span class="definition"><b>Period</b> A stretch of data collected under one configuration.</span>

<span class="finding"><b>F1</b> Ours doubles throughput on all four workloads.</span>

<span class="finding">

With blank lines inside the tags, the body takes **Markdown**, lists included:

- a finding without a title is labelled *Finding.*
- a definition without a title is labelled *Definition.*

</span>

<span class="question">Should this case count towards workload W1 or W2?</span>

---

<!-- _class: details personal-use -->

## Details · Notes for the speaker only

- The `personal-use` class adds the red badge at the top right: a slide not meant for the audience.
- Combine it with `details` as `<!-- _class: details personal-use -->`.
- Inline code renders like `uv run make_figures.py`.
