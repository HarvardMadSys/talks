# MaDSys Marp slide template

A [Marp](https://marp.app) version of the MaDSys PowerPoint template (`template.potx`) with [additional utilities](#macros) for authoring slides, including LaTeX-style definitions, findings, questions and footnotes, plus booktabs-style tables. The theme is inline in the front
matter of `deck.md`, so a deck needs no settings and no theme file.

Maintainer of the Marp template: [Marthenn](https://github.com/Marthenn) · [mmarthen@g.harvard.edu](mailto:mmarthen@g.harvard.edu).

| file | what it is |
| --- | --- |
| `deck.md` | the main slide deck |
| `deck.pdf` | a snapshot export of `deck.md` for preview; it is not rebuilt automatically, so re-export it (see [Exporting](#exporting)) after you change `deck.md` |
| `make_figures.py` | uv script for generating figures |
| `figures/` | Assets used by the slide |

## Fonts

**Aptos may not be installed by default.** Aptos ships with Microsoft 365 but only for Office apps; Marp (Chrome) and matplotlib need it
installed system-wide. Download the Aptos family from Microsoft's
   [Aptos font page](https://learn.microsoft.com/en-us/typography/font-list/aptos) (free of charge; not
   an open licence, so avoid committing the font files to a repository).

## Viewing

1. Install the **Marp for VS Code** extension (`marp-team.marp-vscode`). No settings are needed.
2. Open `deck.md` and use *Open Preview to the Side*.

## Exporting

**From VS Code:** open `deck.md`, run *Marp: Export Slide Deck…* from the command palette, and pick
the format (PDF, PPTX, HTML, PNG or JPEG) in the save dialog.

**From a shell**, in the deck's folder. Needs Node.js, plus Chrome, Chromium or Edge for every
format except HTML.

| format | command |
| --- | --- |
| PDF | `npx @marp-team/marp-cli@latest deck.md --allow-local-files --pdf -o deck.pdf` |
| PowerPoint | `npx @marp-team/marp-cli@latest deck.md --allow-local-files --pptx -o deck.pptx` |
| HTML | `npx @marp-team/marp-cli@latest deck.md -o deck.html` |
| PNG, one per slide | `npx @marp-team/marp-cli@latest deck.md --allow-local-files --images png` |

- `--allow-local-files` lets the browser read `figures/`.
- **From a script, CI or an agent**, add `--no-stdin`: without a terminal, Marp waits for Markdown on
  standard input and never finishes.
- **PowerPoint** slides are images of the rendered slides, so the text cannot be edited. To give
  someone an editable deck, use the original `template.potx`.
- **HTML** loads the figures from `figures/`, so keep the two together when sharing it.
- **PNG** writes `deck.001.png`, `deck.002.png`, … next to `deck.md`.
- Add `--pdf-notes` to put presenter notes (HTML comments that are not directives) in the PDF.
- Marp has no animations: to build a figure up, repeat the slide and add one element per copy.

## Figures

`make_figures.py` is a [uv](https://docs.astral.sh/uv/) script: `uv run make_figures.py` installs
matplotlib, numpy and segno on the fly and writes everything in `figures/` except the logos.

- **Style.** Keep the `rcParams` block: Aptos (Arial until it is installed), 17 pt labels, no top or
  right spine, light grid, no legend frame, and the slide background `#F7F7F7` behind the plot so no
  white box shows. Panels get `(a) …`, `(b) …` titles with `title(ax, "a", "…")`.
- **Direction.** Put the better direction in the axis label (`↑ better`, `↓ better`), as the template
  asks.
- **Size.** Draw figures `W = 10` in wide at 200 dpi (2,000 px). The title band is tall, so figures are
  height-limited: about `![h:345](…)` under a one-line key message, `![h:290](…)` with two bullets
  under it. Pick the height to fit: about 3.5 in for one panel, 3.4–4 in for two.
- **Names.** `fNN_name.png`, numbered in slide order.
- **Helpers.** `bars()` for grouped bars, `bands()` for shaded phases on the x axis, `tint()` for a
  lighter shade of a series colour.
- **Data.** For a real project, read result tables (for example from `data/*.csv`) instead of the
  made-up data, and put the same numbers on the *Details* slide.

## Badges

Badges tag a finding with a category. The template ships three placeholders:

| badge | file | colour | category |
| --- | --- | --- | --- |
| **A** | `figures/badge_A.svg` | crimson `#A51C30` | first category |
| **B** | `figures/badge_B.svg` | navy `#0E2841` | second category |
| **C** | `figures/badge_C.svg` | green `#196B24` | third category |

**On a slide**, add the image after a title or in a list item. The theme sizes it to the text.

```markdown
## F1 · A finding that applies to categories B and C ![](figures/badge_B.svg) ![](figures/badge_C.svg)
```

**Your own badges** go in `BADGES` in `make_figures.py`, as letter and colour; `uv run
make_figures.py` writes `figures/badge_<letter>.svg`. Pick a dark colour so the white letter stays
readable: crimson, navy, green, orange, brown or grey. Each badge is one line of SVG, so it can also be
copied and edited by hand:

```bash
sed 's/#A51C30/#B04E12/; s/>A</>X</' figures/badge_A.svg > figures/badge_X.svg
```

## Macros

LaTeX-style environments. They use only HTML that Marp allows by default (`span`, `b`, `sup`, `mark`
and `div` with a `class`), so they render in the VS Code preview and in every export with no settings.

| macro | LaTeX | renders as |
| --- | --- | --- |
| `<span class="definition"><b>Term</b> …</span>` | `\begin{definition}[Term] … \end{definition}` | navy box, run-in **Definition (Term).** |
| `<span class="finding"><b>F1</b> …</span>` | `\begin{theorem}[F1] … \end{theorem}` | green box, run-in **Finding (F1).** |
| `<span class="question">…</span>` | | orange speech bubble with a **?** |
| `text<sup class="fn"></sup>` and `<span class="footnote">…</span>` | `\footnotemark` and `\footnotetext{…}` | superscript number; the note at the bottom of the slide |
| `<mark>…</mark>` | `\textcolor{crimson}{…}` | crimson text, the template's highlight |

- **The title is optional**, like LaTeX's optional argument: a `<b>…</b>` at the very start of
  the body. Without it the label is just *Definition.* or *Finding.* Use `**…**` for ordinary bold;
  only a leading `<b>` is read as the title.
- **Short bodies go on one line**, with Markdown inside:
  `<span class="definition"><b>Period</b> A stretch of data under **one configuration**.</span>`
- **Longer bodies** (several paragraphs, lists) need blank lines inside the tags:

  ```markdown
  <span class="finding">

  <b>F1</b> Ours doubles throughput on all four workloads.

  - and halves the p99 latency on two of them

  </span>
  ```

- **Footnotes go last on the slide**, one per line. Marks and notes are numbered per slide in
  order: the first `<sup class="fn"></sup>` matches the first footnote. On a slide with no marks,
  footnotes have no numbers, which suits a bare note.
- **Numbers are not automatic** across slides, since each slide is rendered on its own: put any
  number in the title (`<b>F1</b>`).
- **A new environment**, for example a brown `lemma`, takes two edits to the front-matter `style`:
  1. add its label and colours under the `section .finding` line:

     ```css
     section .lemma { --env: "Lemma"; --env-color: var(--brown); --env-tint: #EFE7E2; }
     ```

  2. replace every `.definition, .finding` with `.definition, .finding, .lemma` (one find-and-replace).

  Then write `<span class="lemma"><b>Name</b> …</span>`.

## Slide layouts

| layout | PowerPoint layout | how | example slide |
| --- | --- | --- | --- |
| title | Title Slide | `<!-- _class: title -->`; `#` title, `###` subtitle, a line with your name, then the logo line `![Harvard SEAS](figures/logo_seas.png) ![MaDSys](figures/logo_madsys.png)` after a blank line. No footer or page number. | 1 |
| bullets | Title and Content | `##` title, bullets; nested bullets step down 28 → 24 → 20 pt | 2–4, 7–10 |
| figure + footnotes | Title and Content | `<!-- _class: compact -->` (body one step smaller), figure, bullets with `<sup class="fn"></sup>` marks, then `<span class="footnote">` lines | 5 |
| divider | Custom Layout | `<!-- _class: divider -->`; `#` title and one line of text, centred | 6 |
| finding | Title and Content | `##` title with finding ID and badges, `>` key message, one figure (`![h:345](…)`), `######` source line | 11 |
| details | Title and Content | `<!-- _class: details -->`, `## Details · …`, booktabs tables and small bullets | 12 |
| two columns | Title and Content | `<div class="cols">`, then two `<div>`s, each with blank lines inside | 14 |
| summary | Title and Content | numbered list, a bold claim and its number per item, badges at the end | 15 |
| macros | Title and Content | definitions, findings and questions: see *Macros* | 13, 16 |
| personal use | | add the `personal-use` class for a red "PERSONAL USE" badge: a slide not meant for the audience | 17 |


## Colours

From the PowerPoint theme and its layouts. The theme defines each as a CSS variable.

| colour | hex | CSS variable | from the template | use |
| --- | --- | --- | --- | --- |
| crimson | `#A51C30` | `--crimson` | accent1 | highlight (`<mark>`), footer name, page number, key-message rule, your system in figures |
| dark crimson | `#7A1524` | `--crimson-dark` | hyperlink | links, the footer link |
| bar crimson | `#C7405A` | `--crimson-bar` | footer accent | the footer bar |
| navy | `#0E2841` | `--navy` | dk2 | definitions, baseline A |
| burnt orange | `#B04E12` | `--orange` | accent2 | questions, baseline B |
| green | `#196B24` | `--green` | accent3 | findings |
| brown | `#8F3E0E` | `--brown` | accent5 | |
| grey | `#595959` | `--grey`, `--muted` | accent6 | source lines, footnotes, detail titles |
| slate | `#6B777D` | `--slate` | footer link (Custom Layout) | baseline C |
| silver | `#C4CCD1` | `--silver` | footer separator | the footer dot |
| background | `#F7F7F7` | `--bg` | lt2 `#E8E8E8` at 36% over white | slides and figures |
| text | `#000000` | `--ink` | dk1 | titles and text |

Crimson and green have about the same lightness, so colour-blind viewers can confuse them: do not use
them for two series that must be told apart. Give each series one colour and keep it on every figure in
the deck. Record the mapping here, for example:

| series | colour |
| --- | --- |
| Ours | crimson `#A51C30` |
| Baseline A | navy `#0E2841` |
| Baseline B | burnt orange `#B04E12` |
| Baseline C | slate `#6B777D` |
