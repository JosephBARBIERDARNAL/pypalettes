# Create cmap

::: pypalettes.create_cmap

## Examples

- Create a categorical colormap

```py
# mkdocs: render
import matplotlib.pyplot as plt
from pypalettes import create_cmap
import numpy as np

cmap = create_cmap(colors=["#D57A6DFF", "#E8B762FF", "#9CCDDFFF", "#525052FF"])

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
    colors=["#D57A6DFF", "#E8B762FF", "#9CCDDFFF", "#525052FF"],
    cmap_type="continuous",
)

x = np.linspace(0, 20, 1000)
y = np.sin(x)

plt.scatter(x, y, c=y, cmap=cmap)
plt.colorbar()
```
