# Installation
***

To install the package, you can use pip:

```bash
pip install purrpalette
```

# Usage
***

Load a color map using the `id`:

```python
from purrpalette import purrpalette

purrpalette = purrpalette()
cmap = purrpalette.load_cmap('dafed9')
```

<br>

Load a random color map:

```python
from purrpalette import purrpalette

purrpalette = purrpalette()
cmap = purrpalette.load_cmap('random')
```