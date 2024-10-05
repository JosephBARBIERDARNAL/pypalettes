from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from typing import Union, List, Optional
from PIL import ImageColor
import random
import colorsys

from .get_colors import _get_palette


def load_cmap(
    name: Union[str, List[str]] = "random",
    cmap_type: str = "discrete",
    reverse: bool = False,
    keep_first_n: Optional[int] = None,
    keep: Optional[List[bool]] = None,
    repeat: int = 1,
    shuffle: Union[bool, int] = False,
):
    """
    Load colormap from name.

    Parameters
    - name
        Name of the palette
    - cmap_type
        Type of colormap: 'continuous' or 'discrete'
    - reverse
        Whether to reverse the order of the colors or not
    - keep_first_n
        Keep only the first n colors of the palette
    - keep
        Specify which colors to keep in the palette
    - repeat
        The number of times the palette must be present in the output. Used to access larger palettes that are repeated.
    - shuffle
        Used to mix the order of colors. If an integer is supplied, it will be used as the seed.
    """
    if cmap_type not in {"continuous", "discrete"}:
        raise ValueError("cmap_type argument must be 'continuous' or 'discrete'")

    hex_list, source, kind, _ = _get_palette(name, reverse, keep_first_n, keep, repeat)

    if shuffle:
        if isinstance(shuffle, int):
            random.seed(shuffle)
        random.shuffle(hex_list)

    if cmap_type == "continuous":
        cmap = LinearSegmentedColormap.from_list(name=f"{name}", colors=hex_list)
    elif cmap_type == "discrete":
        cmap = ListedColormap(name=f"{name}", colors=hex_list)

    cmap.source = source
    cmap.kind = kind
    cmap.hex = hex_list
    cmap.colors = hex_list
    cmap.rgb = [ImageColor.getcolor(hex, "RGB") for hex in hex_list]
    cmap.yiq = [colorsys.rgb_to_yiq(rgb[0], rgb[1], rgb[2]) for rgb in cmap.rgb]
    cmap.hsv = [colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2]) for rgb in cmap.rgb]

    return cmap
