from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from typing import List, Union


def create_cmap(
    colors: List, name: str, cmap_type: str = "discrete"
) -> Union[LinearSegmentedColormap, ListedColormap]:
    """
    Create a matplotlib colormap from an iterable of colors.

    Args:
        colors: An iterable of valid matplotlib colors. More about
            valid colors: https://python-graph-gallery.com/python-colors/
        name: Unique palette name
        cmap_type: Type of colormap: 'continuous' or 'discrete'
    """
    if cmap_type == "discrete":
        cmap = ListedColormap(colors=colors, name=name)
    elif cmap_type == "continuous":
        cmap = LinearSegmentedColormap.from_list(name=name, colors=colors)
    else:
        raise ValueError("cmap_type argument must be 'continuous' or 'discrete'")

    return cmap
