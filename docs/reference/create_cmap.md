# Create cmap

::: pypalettes.create_cmap

## Examples

```py
# mkdocs: render
import matplotlib.pyplot as plt
from pypalettes import create_cmap
import numpy as np

cmap = create_cmap(
    colors=["#D57A6DFF", "#E8B762FF", "#9CCDDFFF", "#525052FF"],
    name="myCmap",
    cmap_type="continuous",
)

x = np.linspace(0, 20, 1000)
y = np.sin(x)

plt.scatter(x, y, c=y, cmap=cmap)
plt.colorbar()
```
