# Create cmap

::: pypalettes.create_cmap

## Examples

- Create a categorical colormap

```py
# mkdocs: render
import matplotlib.pyplot as plt
from pypalettes import create_cmap
import numpy as np

cmap = create_cmap(["#D57A6D", "#E8B762", "#9CCDDF", "#525052"])

x = np.linspace(0, 20, 1000)
y = np.sin(x)

plt.scatter(x, y, c=y, cmap=cmap)
plt.colorbar()
```

<br>

- Create a continuous colormap

```py
# mkdocs: render
import matplotlib.pyplot as plt
from pypalettes import create_cmap
import numpy as np

cmap = create_cmap(
    ["#D57A6D", "#E8B762", "#9CCDDF", "#525052"],
    cmap_type="continuous",
)

x = np.linspace(0, 20, 1000)
y = np.sin(x)

plt.scatter(x, y, c=y, cmap=cmap)
plt.colorbar()
```
