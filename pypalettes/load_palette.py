import random

from pypalettes.utils import _get_palette


def load_palette(
    name: str | list[str] = "random",
    reverse: bool = False,
    keep_first_n: int | None = None,
    keep_last_n: int | None = None,
    keep: list[bool] | None = None,
    repeat: int = 1,
    shuffle: bool | int = False,
    remove: int | list[int] | None = None,
) -> list[str]:
    """
    Load a color palette from one of the 2500+ available palettes.

    You can find all valid palette names [here](https://python-graph-gallery.com/color-palette-finder/){target="_blank"}

    Args:
        name: Name of the palette
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
        A list of colors.
    """

    palette: dict = _get_palette(
        name, reverse, keep_first_n, keep_last_n, keep, repeat, remove
    )
    hex_list: list = palette["hex_list"]

    if shuffle:
        if isinstance(shuffle, int):
            random.seed(shuffle)
        random.shuffle(hex_list)

    return hex_list
