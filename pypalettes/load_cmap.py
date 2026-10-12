import colorsys
import random
from typing import TYPE_CHECKING, Union, cast

if TYPE_CHECKING:
    from matplotlib.colors import LinearSegmentedColormap, ListedColormap

from pypalettes.utils import _get_palette


def load_cmap(
    name: str | list[str] = "random",
    cmap_type: str = "discrete",
    reverse: bool = False,
    keep_first_n: int | None = None,
    keep_last_n: int | None = None,
    keep: list[bool] | None = None,
    repeat: int = 1,
    shuffle: bool | int = False,
    remove: int | list[int] | None = None,
) -> Union["LinearSegmentedColormap", "ListedColormap"]:
    """
    Load a matplotlib colormap from one of the 2500+ available palettes.

    You can find all valid palette names [here](https://python-graph-gallery.com/color-palette-finder/){target="_blank"}

    Args:
        name: Name of the palette
        cmap_type: Type of colormap: 'continuous' or 'discrete'
        reverse: Whether to reverse the order of the colors or not
        keep_first_n: Keep only the first n colors of the palette
        keep: Specify which colors to keep in the palette
        repeat: The number of times the palette must be present in
            the output. Used to access larger palettes that are repeated.
        shuffle: Used to mix the order of colors. If an integer is
            supplied, it will be used as the seed.
        remove: Remove colors at specified indices (0-indexed). Can be
            a single int or list of ints. For example, remove=2 removes
            the 3rd color, remove=[1, 3] removes the 2nd and 4th colors.

    Returns:
        A matplotlib colormap.
    """
    from matplotlib.colors import LinearSegmentedColormap, ListedColormap
    from PIL import ImageColor

    palette: dict = _get_palette(
        name, reverse, keep_first_n, keep_last_n, keep, repeat, remove
    )
    hex_list: list = palette["hex_list"]
    source: str = palette["source"]
    kind: str = palette["kind"]

    if shuffle:
        if isinstance(shuffle, int):
            random.seed(shuffle)
        random.shuffle(hex_list)

    if cmap_type == "continuous":
        cmap: LinearSegmentedColormap = LinearSegmentedColormap.from_list(
            name=f"{name}", colors=hex_list
        )
    elif cmap_type == "discrete":
        cmap: ListedColormap = ListedColormap(name=f"{name}", colors=hex_list)
    else:
        raise ValueError("cmap_type argument must be 'continuous' or 'discrete'")

    cmap.source: str = source  # ty: ignore
    cmap.kind: str = kind  # ty: ignore
    cmap.hex: list = hex_list  # ty: ignore
    cmap.colors: list = hex_list  # ty: ignore
    rgb_colors: list[tuple[int, int, int]] = [
        cast(tuple[int, int, int], ImageColor.getcolor(hex, "RGB")) for hex in hex_list
    ]
    cmap.rgb: list = rgb_colors  # ty: ignore
    cmap.yiq: list = [  # ty: ignore
        colorsys.rgb_to_yiq(*rgb) for rgb in rgb_colors
    ]
    cmap.hsv: list = [  # ty: ignore
        colorsys.rgb_to_hsv(*rgb) for rgb in rgb_colors
    ]

    return cmap
