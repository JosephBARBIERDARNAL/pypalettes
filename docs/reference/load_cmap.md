# Load cmap

::: pypalettes.load_cmap

## Examples

```py
# mkdocs: render
import matplotlib.pyplot as plt
import numpy as np
from pypalettes import load_cmap

np.random.seed(0)
data = np.random.randn(20, 20)

cmap = load_cmap("Sunset", cmap_type="continuous")

plt.imshow(
   X=data,
   cmap=cmap
)
plt.colorbar()
```

```py
# mkdocs: render
import matplotlib.pyplot as plt
import numpy as np
from pypalettes import load_cmap

np.random.seed(0)
data = np.random.randn(20, 20)

cmap = load_cmap("Acadia", cmap_type="continuous")

plt.imshow(
   X=data,
   cmap=cmap
)
plt.colorbar()
```

```py
# mkdocs: render
import matplotlib.pyplot as plt
import numpy as np
from pypalettes import load_cmap

np.random.seed(0)
data = np.random.randn(20, 20)

cmap = load_cmap("Acanthurus_olivaceus", cmap_type="continuous")

plt.imshow(
   X=data,
   cmap=cmap
)
plt.colorbar()
```

[**See all palettes**](https://python-graph-gallery.com/color-palette-finder/){target="\_blank"}
