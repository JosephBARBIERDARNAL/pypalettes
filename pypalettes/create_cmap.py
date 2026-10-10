from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from matplotlib.colors import LinearSegmentedColormap, ListedColormap


def create_cmap(
    colors: list,
    cmap_type: str = "discrete",
    name: str = "custom_cmap",
) -> Union["LinearSegmentedColormap", "ListedColormap"]:
    """
    Create a matplotlib colormap from an iterable of colors.

    Args:
        colors: An iterable of valid matplotlib colors. More about
            valid colors: https://python-graph-gallery.com/python-colors/
        name: A name for the palette
        cmap_type: Type of colormap: 'continuous' or 'discrete'
    """
    from matplotlib.colors import LinearSegmentedColormap, ListedColormap

    if cmap_type == "discrete":
        cmap: ListedColormap = ListedColormap(colors=colors, name=name)
    elif cmap_type == "continuous":
        cmap: LinearSegmentedColormap = LinearSegmentedColormap.from_list(
            name=name, colors=colors
        )
    else:
        raise ValueError("cmap_type argument must be 'continuous' or 'discrete'")

    return cmap
