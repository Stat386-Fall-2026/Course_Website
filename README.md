# Course Website Template

A reusable Quarto-based course website template for hosting class slides, in-class code demos, assignments, notes, and resources from one GitHub repository. Designed to be cloned at the start of each semester to quickly spin up a new course site.

## Quick Start: Create a New Course from This Template

1. **Create a new repo from this template** on GitHub (click "Use this template" → "Create a new repository"), or clone and push to a new repo.
2. **Find and replace all `TODO` placeholders** — search the repo for `TODO:` to find every spot that needs course-specific info:
   - `_variables.yml` — course title, number, term, instructor
   - `_quarto.yml` — website title, `site-url`, `repo-url`, GitHub navbar link
   - `slides/_metadata.yml` — slide footer text
   - `index.qmd` — course description, instructor details
   - `schedule.qmd` — weekly topics and dates
   - `resources.qmd` — software, readings, policies
   - `assignments/homework-01.qmd` — assignment content and due dates
3. **Update the schedule** with your actual weekly topics.
4. **Render and publish** (see below).

## Preview the Site Locally

```bash
quarto preview
```

This starts a local server and opens the site in your browser. Changes to `.qmd` files will live-reload.

## Render the Site

```bash
quarto render
```

This renders all `.qmd` files into the `docs/` directory, which is configured as the output directory in `_quarto.yml`.

## Publish with GitHub Pages

1. Render the site: `quarto render`
2. Commit the rendered output:
   ```bash
   git add .
   git commit -m "Render site"
   git push
   ```
3. In your GitHub repository, go to **Settings → Pages**.
4. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
5. Select the **main** branch and the **/docs** folder.
6. Save. The site will be live at `https://<username>.github.io/<repo>/` within a few minutes.

> **Note:** The `.nojekyll` file in the repository root tells GitHub Pages to serve the `docs/` directory as-is, bypassing Jekyll processing.

## Repository Structure

```text
.
├── _quarto.yml          # Project configuration
├── _variables.yml       # Shared course info (title, term, instructor)
├── theme.scss           # BYU-inspired Sass theme (navy/royal/tan) for HTML + Reveal.js
├── styles.css           # Minimal CSS overrides for HTML pages
├── index.qmd            # Home page
├── schedule.qmd         # Weekly schedule
├── slides.qmd           # Slide deck index
├── demos.qmd            # Code demo index
├── assignments.qmd      # Assignments index
├── resources.qmd        # Resources page
├── slides/              # Reveal.js slide decks
│   ├── _metadata.yml    #   shared Reveal.js defaults (theme, footer, etc.)
│   └── week-01.qmd
├── demos/               # Code demos
│   ├── _metadata.yml
│   ├── week-01.qmd
│   └── week-01-demo.py
├── assignments/         # Homework and projects
│   └── homework-01.qmd
├── _partials/           # Reusable content blocks (included via {{< include >}})
│   ├── questions.qmd
│   └── course-norms.qmd
├── _templates/          # Copyable starter decks
│   └── lecture.qmd
├── data/                # Course datasets
├── images/              # Course images
├── .nojekyll            # Disable Jekyll on GitHub Pages
├── .gitignore
└── README.md
```

## Theming System

The template includes a reusable styling system so you don't repeat configuration in every deck.

### Color Palette

Colors are defined as Sass variables at the top of `theme.scss`. Change them there and everything updates:

| Variable | Color | Used for |
|----------|-------|----------|
| `$course-navy` | #002E5D | Headings, section cards, takeaways |
| `$course-royal` | #0057A7 | Links, demo accents |
| `$course-tan` | #C8B88A | Slide heading borders, key-idea blocks |
| `$course-paper` | #FFFFFF | Page background |
| `$course-ink` | #1A1A1A | Body text |

### Reusable Slide Classes

Add these to any slide heading (e.g., `## Title {.section-card}`):

| Class | Effect |
|-------|--------|
| `{.section-card}` | Navy gradient background, white text |
| `{.question-slide}` | Warm cream background, tan accent |
| `{.demo-slide}` | Light blue background, royal accent |
| `{.takeaway-slide}` | Solid navy background, white text |

### Reusable Content Blocks

Use these divs inside any slide:

| Block | Effect |
|-------|--------|
| `{.key-idea}` | Cream box with tan left border |
| `{.discussion-box}` | Gray box with navy left border |
| `{.demo-box}` | Light blue box with royal left border |

### Shared Variables

`_variables.yml` holds course info you can insert with shortcodes:

```markdown
Welcome to {{< var course.number >}} — {{< var course.term >}}.
```

### Partials

`_partials/` contains slides included verbatim across decks:

- `questions.qmd` — standard closing Q&A slide
- `course-norms.qmd` — course expectations slide

Use them with: `{{< include ../_partials/questions.qmd >}}`

### Starter Templates

`_templates/lecture.qmd` is a copyable starter deck demonstrating all slide classes and blocks. Copy it to start a new week:

```bash
cp _templates/lecture.qmd slides/week-04.qmd
```

## Add a New Slide Deck

1. Copy `slides/week-01.qmd` (or `_templates/lecture.qmd`) to `slides/week-02.qmd`.
2. Edit the title, subtitle, and content.
3. Add a link on `slides.qmd`.
4. Add a row in `schedule.qmd`.
5. Add `slides/week-02.qmd` to the sidebar in `_quarto.yml` under the "Slides" section.
6. Run `quarto render`.

## Add a New Code Demo

1. Copy `demos/week-01.qmd` to `demos/week-02.qmd`.
2. Create `demos/week-02-demo.py` (or `.R`, `.jl`, etc.) with the standalone script.
3. Edit the demo content and link to the new source file.
4. Add a link on `demos.qmd`.
5. Add a row in `schedule.qmd`.
6. Add `demos/week-02.qmd` to the sidebar in `_quarto.yml` under the "Demos" section.
7. Run `quarto render`.

## Add a New Assignment

1. Copy `assignments/homework-01.qmd` to `assignments/homework-02.qmd`.
2. Edit the content.
3. Add a link on `assignments.qmd`.
4. Add `assignments/homework-02.qmd` to the sidebar in `_quarto.yml` under the "Assignments" section.
5. Run `quarto render`.

## Files Generated by Quarto (Do Not Edit Manually)

- `docs/` — the entire rendered website output. Everything here is regenerated by `quarto render` and should not be edited by hand.

## Tech Stack

- [Quarto](https://quarto.org) — scientific and technical publishing system
- [Reveal.js](https://revealjs.com) — HTML presentation framework (via Quarto)
- [GitHub Pages](https://pages.github.com) — static site hosting