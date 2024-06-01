# purrpalette

A large (**~2500**) collection of color maps for matplotlib/seaborn.

## Installation

```bash
pip install purrpalette
```

## Quick start

Load a color map using the `name`:

```python
from purrpalette import PurrPalette

purr = PurrPalette()
cmap = purr.load_cmap('Stegastes_variabilis')
cmap
```

<br>

Load a random color map:

```python
from purrpalette import purrpalette

purrpalette = purrpalette()
cmap = purrpalette.load_cmap('random')
cmap
```

<br>

Find where the source of the color map:

```python
from purrpalette import PurrPalette

purr = PurrPalette()
print(purr.source('bilbao'))
```

output: `'The R package: {khroma}'`

### How data has been collected

- Sites used
   - https://coolors.co/palettes/trending
   - https://pmassicotte.github.io/paletteer_gallery/

These sites have been scraped with the scripts in `parsers/`. Data is then saved into a `.csv` format with name+palette.

### How to add a new palette

More is better: if you know how to add a significant amount of palettes (>30), please do so. PRs are welcome.