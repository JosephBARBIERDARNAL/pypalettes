# Installation
***

To install the package, you can use pip:

```bash
pip install nyancat
```

# Usage
***

Load a color map using the `id`:

```python
from nyancat import NyanCat

nyancat = NyanCat()
cmap = nyancat.load_cmap('dafed9')
```

<br>

Load a random color map:

```python
from nyancat import NyanCat

nyancat = NyanCat()
cmap = nyancat.load_cmap('random')
```