
<br>

This directory contains scripts that at the end generate `palettes.csv` (and `palettes.json`).

- `scrape_paletteer.py` scrapes the [paletteer gallery](https://pmassicotte.github.io/paletteer_gallery/)
- `matplotlib_and_seaborn.py` gets color maps from matplotlib and seaborn.

<br><br>

## Palette source

- Sources
   - https://pmassicotte.github.io/paletteer_gallery/
   - and color maps already availables in `matplotlib` and `seaborn`

Data is then saved into a `.csv` (and `.json`) format with name + palette + source + kind, where:
- `name`: palette name (such as viridis or inferno)
- `palette`: list of string (hexadecimal format)
- `source`: a simple string that says where the palette comes from
- `kind`: the type of palette (categorical, sequential or diverging, according to the [paletteer gallery](https://pmassicotte.github.io/paletteer_gallery/))

<br><br>

## Dupplicates

*Warning: Since some color maps have the **same name**, some specific palettes can be different from the ones expected. If you find a mistake, please **open an issue**.*

<br><br>

## Source of a specific palette

The easiest way to find the original source is to use the `get_source()` function, and I highly suggest you to find your dream color map using the [original site](https://python-graph-gallery.com/color-palette-finder/).