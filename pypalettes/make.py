from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from typing import List, Optional

def make_cmap(
    colors: List,
    cmap_type: str = 'discrete',
    name: Optional[str] = "my cmap"
):  
    """
    Create a matplotlib colormap from an iterable of colors.

    Parameters
    - colors: List
        An iterable of valid matplotlib colors. More about valid colors: https://python-graph-gallery.com/python-colors/
    - cmap_type: str
        Type of colormap: 'continuous' or 'discrete'
    - name: Union[str, list]
        Optional palette name
    """
    if cmap_type == 'discrete':
        cmap = ListedColormap(colors=colors, name=name)
    elif cmap_type == 'continuous':
        cmap = LinearSegmentedColormap.from_list(name=name, colors=colors)
    else:
        raise ValueError("cmap_type argument must be 'continuous' or 'discrete'")

    return cmap