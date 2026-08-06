# Data Folder

Place course datasets here (CSV, JSON, Excel, etc.).

## Naming Convention

Use descriptive, lowercase filenames with hyphens:

- `student-scores.csv`
- `weather-data.csv`
- `survey-results.json`

## Referencing Data in Demos

From a `.qmd` file in the `demos/` directory, reference files here using a relative path:

```python
import pandas as pd
df = pd.read_csv("../data/student-scores.csv")
```