# PyPalettes

<p>
   
   <img
      src="https://raw.githubusercontent.com/JosephBARBIERDARNAL/pypalettes/master/images/Pypalettes-1.png"
      width="16%"
      alt="logo1"
   />
   <img
      src="https://raw.githubusercontent.com/JosephBARBIERDARNAL/pypalettes/master/images/Pypalettes-2.png"
      width="16%"
      alt="logo1"
   />
   <img
      src="https://raw.githubusercontent.com/JosephBARBIERDARNAL/pypalettes/master/images/Pypalettes-3.png"
      width="16%"
      alt="logo1"
   />
   <img
      src="https://raw.githubusercontent.com/JosephBARBIERDARNAL/pypalettes/master/images/Pypalettes-4.png"
      width="16%"
      alt="logo1"
   />
   <img
      src="https://raw.githubusercontent.com/JosephBARBIERDARNAL/pypalettes/master/images/Pypalettes-5.png"
      width="16%"
      alt="logo1"
   />
   <img
      src="https://raw.githubusercontent.com/JosephBARBIERDARNAL/pypalettes/master/images/Pypalettes-6.png"
      width="16%"
      alt="logo1"
   />

</p>

A large (**+2500**) collection of color maps for Python.

All available palettes can be found [**on the dedicated website**](https://python-graph-gallery.com/color-palette-finder/)

<center>
   
   ![](pypalettes.gif)
</center>

> You can find an [**introduction to PyPalettes**](https://python-graph-gallery.com/introduction-to-pypalettes/) in the [**Python Graph Gallery**](https://python-graph-gallery.com), with code samples and explanations about how to use this library in many different cases.






<br><br>

## Installation

You can install `pypalettes` directly from PyPI with:

```bash
pip install --upgrade pypalettes
```

Alternatively you can install the **development version** with:

```bash
pip install git+https://github.com/JosephBARBIERDARNAL/pypalettes.git
```

<br><br>

## Quick start

Once the `cmap` is loaded, you can use it as any other color map in `matplotlib` or `seaborn`.

```python
import matplotlib.pyplot as plt
from pypalettes import load_cmap
import seaborn as sns
import numpy as np

data = np.random.rand(10, 12)

cmap = load_cmap('Anemone', cmap_type='continuous')

sns.heatmap(data, cmap=cmap)
plt.show()
```

![heatmap example](https://raw.githubusercontent.com/JosephBARBIERDARNAL/pypalettes/main/images/heatmap.png)

<br><br>

## Getting started

<br>

- Load a color map:

```python
from pypalettes import load_cmap
cmap = load_cmap('Chaetodon_sedentarius')
cmap
```

![Darjeeling2](https://raw.githubusercontent.com/JosephBARBIERDARNAL/pypalettes/main/images/simple.png)

<br>

- Transform a qualitative color map into a continuous one:

```python
from pypalettes import load_cmap
cmap = load_cmap('Chaetodon_sedentarius', cmap_type='continuous')
cmap
```

![Darjeeling2](https://raw.githubusercontent.com/JosephBARBIERDARNAL/pypalettes/main/images/continuous.png)

<br>

- Invert a color map:

```python
from pypalettes import load_cmap
cmap = load_cmap('Chaetodon_sedentarius', reverse=True)
cmap
```

![Darjeeling2](https://raw.githubusercontent.com/JosephBARBIERDARNAL/pypalettes/main/images/reverse.png)

<br>

- Get hex values of a color map:

```python
from pypalettes import get_hex
get_hex('pupitar')
```

`['#7098C0FF',
 '#88C0E8FF',
 '#285880FF',
 '#B8E0F8FF',
 '#F8F8F8FF',
 '#404060FF',
 '#A8A8A8FF',
 '#C8C8D0FF',
 '#B04000FF']`

<br>

- Get rgb values of a color map:

```python
from pypalettes import get_rgb
get_rgb('AirNomads')
```

`[(255, 153, 51),
 (194, 72, 65),
 (255, 255, 51),
 (139, 91, 69),
 (135, 175, 209),
 (238, 176, 90),
 (219, 197, 160)]`

<br>

> More examples can be found in this [**introduction to PyPalettes**](https://python-graph-gallery.com/introduction-to-pypalettes/).

<br><br>

## Chart made with `pypalettes`

*Click on the image to get the associated code!*

<p>
   
   <a href='https://python-graph-gallery.com/web-map-with-custom-legend/'  target="_blank">
      <img
         src="https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/graph/web-map-with-custom-legend.png"
         width="30%"
         alt="choropleth map of europe"
      />
   </a>

   <a href='https://python-graph-gallery.com/web-stacked-area-with-inflexion-arrows/'  target="_blank">
      <img
         src="https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/graph/web-stacked-area-with-inflexion-arrows.png"
         width="69%"
         alt="stacked area chart of natural disasters"
      />
   </a>

   <br/>

   <a href='https://python-graph-gallery.com/591-arrows-with-inflexion-point/'  target="_blank">
      <img
         src="https://raw.githubusercontent.com/JosephBARBIERDARNAL/pypalettes/main/images/chart_example_1.png"
         width="60%"
         alt="gapminder bubble chart"
      />
   </a>

</p>

<br><br>

## Acknowledgements

`PyPalettes` is **highly** inspired (and relies on for the first one) from
- the R package [paletteer](https://github.com/EmilHvitfeldt/paletteer)
- the python package [palettable](https://github.com/jiffyclub/palettable).

A big thanks to [Yan Holtz](https://www.yan-holtz.com/) for:

- Creating the [web app for browsing palettes](https://python-graph-gallery.com/color-palette-finder/)
- Hosting the [documentation](https://python-graph-gallery.com/introduction-to-pypalettes/) and [examples](#chart-made-with-pypalettes) on the [Python Graph Gallery](https://python-graph-gallery.com)
- Providing valuable feedback on the code and design of the API

<br><br>

## How data has been collected

99% of the palettes come from the [Paletteer R package](https://github.com/EmilHvitfeldt/paletteer).

Learn more in the [dedicated directory](parsers/README.md).

<br><br>