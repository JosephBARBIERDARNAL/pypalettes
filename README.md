# purrpalette

A large (**~2500**) collection of color maps for matplotlib/seaborn.

All available palettes can be found [here](https://josephbarbierdarnal.github.io/purrpalette/)

<br><br>

## Installation

```bash
pip install git+https://github.com/JosephBARBIERDARNAL/purrpalette.git
```

<br><br>

## Quick start

- Load the package:

```python
from purrpalette import PurrPalette
purr = PurrPalette()
```

<br>

- Load a color map:

```python
cmap = purr.load_cmap('Darjeeling2')
cmap
```

![Darjeeling2](images/Darjeeling2-qualitative.png)

<br>

- Transform a qualitative color map into a continuous one:

```python
cmap = purr.load_cmap('Darjeeling2', type='continuous')
cmap
```

![Darjeeling2](images/Darjeeling2-continuous.png)

<br>

- Load a random color map:

```python
cmap = purr.load_cmap('random')
cmap
```

![random](images/random.png)

<br>

- Find where a color map comes from:

```python
print(purr.source('bilbao'))
```

`'The R package: {khroma}'`

<br>

- Get hex values of a color map:

```python
print(purr.hex('42e4b0'))
```

`['#000000', '#14213D', '#FCA311', '#E5E5E5', '#FFFFFF']`

<br>

- Get rgb values of a color map:

```python
print(purr.rgb('AirNomads'))
```

`[(255, 153, 51),
 (194, 72, 65),
 (255, 255, 51),
 (139, 91, 69),
 (135, 175, 209),
 (238, 176, 90),
 (219, 197, 160)]`

<br><br>

## Related projects

`purrpalette` is **highly** inspired from the R package [paletteer](https://github.com/EmilHvitfeldt/paletteer) and the python package [palettable](https://github.com/jiffyclub/palettable).

<br><br>

## How data has been collected

- Sites used
   - https://coolors.co/palettes/trending
   - https://pmassicotte.github.io/paletteer_gallery/

These sites have been scraped with the scripts in `parsers/`. Data is then saved into a `.csv` format with name+palette.

<br><br>

## How to add a new palette

More is better: if you know how to add a significant amount of palettes (>30), please do so. PRs are welcome.

TODO: detail the process