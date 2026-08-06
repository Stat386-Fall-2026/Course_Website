# Images Folder

Place course images here (PNG, JPG, SVG, etc.).

## Naming Convention

Use descriptive, lowercase filenames with hyphens:

- `course-logo.png`
- `week-01-diagram.svg`
- `histogram-example.png`

## Referencing Images in Documents

From a `.qmd` file in the root directory, reference images like this:

```markdown
![Alt text](images/histogram-example.png)
```

From a `.qmd` file in a subdirectory (e.g., `demos/`), use a relative path:

```markdown
![Alt text](../images/histogram-example.png)
```