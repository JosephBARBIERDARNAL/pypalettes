from matplotlib.colors import LinearSegmentedColormap, ListedColormap
import matplotlib as mpl
import warnings
from typing import List, Union


def add_cmap(
    colors: List, name: str, cmap_type: str = "discrete", force: bool = True
) -> Union[LinearSegmentedColormap, ListedColormap]:
    """
    Create a matplotlib colormap from an iterable of colors.

    Parameters
    - colors:
        An iterable of valid matplotlib colors. More about valid colors: https://python-graph-gallery.com/python-colors/
    - name:
        Unique palette name
    - cmap_type:
        Type of colormap: 'continuous' or 'discrete'
    - force:
        If True, overwrites the registered colormap with the same name if it exists.
    """
    if cmap_type == "discrete":
        cmap = ListedColormap(colors=colors, name=name)
    elif cmap_type == "continuous":
        cmap = LinearSegmentedColormap.from_list(name=name, colors=colors)
    else:
        raise ValueError("cmap_type argument must be 'continuous' or 'discrete'")

    warnings.filterwarnings(
        "ignore", category=UserWarning, message=".*that was already in the registry.*"
    )

    mpl.colormaps.register(cmap=cmap, force=force)
    return cmap
