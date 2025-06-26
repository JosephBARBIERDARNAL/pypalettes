# Example usage

#### Categorical palette

```py
# mkdocs: render
import matplotlib.pyplot as plt
import seaborn as sns
from pypalettes import load_cmap

cmap = load_cmap("Fun")
palette = cmap.colors # list of hexadecimal values

df = sns.load_dataset("penguins")

g = sns.lmplot(
    data=df,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species",
    palette=palette,
)
g.set_axis_labels("Snoot length", "Snoot depth")
```

#### Show cmap

```py
# mkdocs: render
import matplotlib.pyplot as plt
import seaborn as sns
from pypalettes import load_cmap

cmap = load_cmap("Fun")
cmap
```
