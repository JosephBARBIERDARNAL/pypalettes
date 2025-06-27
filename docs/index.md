# pypalettes

<img src="https://github.com/JosephBARBIERDARNAL/static/blob/main/python-libs/pypalettes/image.png?raw=true" alt="pypalettes logo" align="right" width="150px"/>

A large (**+2500**) collection of color maps for Python.

![PyPI - Downloads](https://img.shields.io/pypi/dm/pypalettes)

<br>

## Quick start

Let's see how to use the `"Sunset"` palette:

=== "Simple usage"

    ```py hl_lines="9"
    # mkdocs: render
    import matplotlib.pyplot as plt
    import numpy as np
    from pypalettes import load_cmap

    np.random.seed(0)
    data = np.random.randn(20, 20)

    cmap = load_cmap("Sunset")

    plt.imshow(
      X=data,
      cmap=cmap
    )
    plt.colorbar()
    ```

=== "Continuous palette"

    ```py hl_lines="9"
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

=== "Reverse palette"

    ```py hl_lines="9"
    # mkdocs: render
    import matplotlib.pyplot as plt
    import numpy as np
    from pypalettes import load_cmap

    np.random.seed(0)
    data = np.random.randn(20, 20)

    cmap = load_cmap("Sunset", reverse=True)

    plt.imshow(
      X=data,
      cmap=cmap
    )
    plt.colorbar()
    ```

> The `"Sunset"` is just one of 2500+ available palettes from `pypalettes`.

- [**See all palettes**](https://python-graph-gallery.com/color-palette-finder/){target="\_blank"}
- [**More examples**](./examples)

## Installation

=== "stable"

    ```bash
    pip install pypalettes
    ```

=== "dev"

    ```bash
    pip install git+https://github.com/JosephBARBIERDARNAL/pypalettes.git
    ```

<br><br>
