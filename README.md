# purrpalette

A large (**~2500**) collection of color maps for matplotlib/seaborn.

All available palettes can be found [here](https://josephbarbierdarnal.github.io/purrpalette/)

<br><br>

## Installation

```bash
pip install purrpalette
```

<br><br>

## Quick start

```python
from purrpalette import PurrPalette
```

Load a color map using the `name`:

```python
purr = PurrPalette()
cmap = purr.load_cmap('Stegastes_variabilis')
cmap
```

<br>

Load a random color map:

```python
purr = PurrPalette()
cmap = purr.load_cmap('random')
cmap
```

<br>

Find where the source of the color map:

```python
purr = PurrPalette()
print(purr.source('bilbao'))
```

output: `'The R package: {khroma}'`

<br>

Get hex values of a color map:

```python
purr = PurrPalette()
purr.hex('42e4b0')
```

output: `['#000000', '#14213D', '#FCA311', '#E5E5E5', '#FFFFFF']`

<br><br>

## How data has been collected

- Sites used
   - https://coolors.co/palettes/trending
   - https://pmassicotte.github.io/paletteer_gallery/

These sites have been scraped with the scripts in `parsers/`. Data is then saved into a `.csv` format with name+palette.

<br><br>

## How to add a new palette

More is better: if you know how to add a significant amount of palettes (>30), please do so. PRs are welcome.