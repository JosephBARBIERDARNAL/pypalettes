from importlib import resources
import csv
import random
from difflib import get_close_matches
from typing import Union, List, Optional
import warnings

_PALETTES_CACHE = None


def _load_palettes(palettes_path: str = "palettes.csv"):
    """
    Load palettes from csv file.

    Parameters
    - palettes_path
        Path to the csv file with the palettes
    """
    global _PALETTES_CACHE

    if _PALETTES_CACHE is None:
        _PALETTES_CACHE = {}
        palettes_file = resources.files("pypalettes").joinpath(palettes_path)
        with palettes_file.open("r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                _PALETTES_CACHE[row["name"]] = row

    return _PALETTES_CACHE


def _get_one_palette(
    name: Union[str, List[str]],
    reverse: bool = False,
    keep_first_n: Optional[int] = None,
    keep_last_n: Optional[int] = None,
    keep: Optional[List[bool]] = None,
):
    """
    Get one palette from name.

    Parameters
    - name
        Name of the palette
    - reverse
        Whether to reverse the order of the colors or not
    - keep_first_n
        Keep only the first n colors of the palette
    - keep_last_n
        Keep only the last n colors of the palette
    - keep
        Specify which colors to keep in the palette
    """
    palettes = _load_palettes()
    if name == "random":
        palette = random.choice(list(palettes.values()))
    else:
        if name not in palettes:
            suggestions = get_close_matches(name, palettes.keys(), n=5, cutoff=0.01)
            raise ValueError(
                f"Palette with name '{name}' not found. Did you mean:\n{', '.join(suggestions)}?\n\n"
                "See available palettes at https://python-graph-gallery.com/color-palette-finder/"
            )
        palette = palettes[name]

    source = palette["source"]
    kind = palette["kind"]
    paletteer_kind = palette["paletteer-kind"]
    hex_list = eval(palette["palette"])

    if keep_first_n is not None and keep_first_n > len(hex_list):
        raise ValueError(
            f"keep_first_n ({keep_first_n}) must be less than or equal to the length of the palette ({len(hex_list)})."
        )

    if keep_last_n is not None and keep_last_n > len(hex_list):
        raise ValueError(
            f"keep_last_n ({keep_last_n}) must be less than or equal to the length of the palette ({len(hex_list)})."
        )

    if keep is not None and len(keep) != len(hex_list):
        raise ValueError(
            f"keep list must be the same length as the palette ({len(hex_list)}!={len(keep)})."
        )

    if reverse:
        hex_list = hex_list[::-1]

    if keep_first_n:
        hex_list = hex_list[:keep_first_n]
    elif keep_last_n:
        hex_list = hex_list[-keep_last_n:]
    elif keep is not None:
        hex_list = [color for color, keep_color in zip(hex_list, keep) if keep_color]

    return hex_list, source, kind, paletteer_kind


def _get_palette(
    name: Union[str, List[str]],
    reverse: bool = False,
    keep_first_n: Optional[int] = None,
    keep_last_n: Optional[int] = None,
    keep: Optional[List[bool]] = None,
    repeat: int = 1,
):
    """
    Get palette from name.

    Parameters
    - name
        Name of the palette. Also accepts list of palette names.
    - reverse
        Whether to reverse the order of the colors or not
    - keep_first_n
        Keep only the first n colors of the palette
    - keep_last_n
        Keep only the last n colors of the palette
    - keep
        Specify which colors to keep in the palette
    - repeat
        The number of times the palette must be present in the output. Used to access larger palettes that are repeated.
    """
    if not isinstance(reverse, bool):
        raise TypeError("reverse must be a boolean.")
    if keep_first_n is not None and (
        not isinstance(keep_first_n, int) or keep_first_n <= 0
    ):
        raise TypeError(f"keep_first_n must be a positive integer, not {keep_first_n}.")
    if keep_last_n is not None and (
        not isinstance(keep_last_n, int) or keep_last_n <= 0
    ):
        raise TypeError(f"keep_last_n must be a positive integer, not {keep_last_n}.")
    if keep is not None and (
        not isinstance(keep, list) or not all(isinstance(item, bool) for item in keep)
    ):
        raise TypeError(f"keep must be a list of boolean values, not {keep}.")
    if sum(x is not None for x in [keep_first_n, keep_last_n, keep]) > 1:
        raise ValueError(
            "Cannot specify more than one of keep_first_n, keep_last_n, and keep arguments simultaneously."
        )
    if not repeat >= 1 or not isinstance(repeat, int):
        raise TypeError("repeat must be a positive integer.")

    if isinstance(name, str):
        hex_list, source, kind, paletteer_kind = _get_one_palette(
            name=name,
            reverse=reverse,
            keep_first_n=keep_first_n,
            keep_last_n=keep_last_n,
            keep=keep,
        )
    elif isinstance(name, list):
        for param in [keep_first_n, keep_last_n, keep]:
            if param is not None:
                warnings.warn(
                    "`keep_first_n`, `keep_last_n` and `keep` arguments are ignored when `name` is a list."
                )
        hex_list = []
        source = []
        kind = []
        paletteer_kind = []
        for palette_name in name:
            one_hex_list, one_source, one_kind, one_paletteer_kind = _get_one_palette(
                name=palette_name
            )
            hex_list.extend(one_hex_list)
            source.append(one_source)
            kind.append(one_kind)
            paletteer_kind.append(one_paletteer_kind)
    else:
        raise TypeError("`name` must be a string or a list of strings")

    hex_list *= repeat
    return hex_list, source, kind, paletteer_kind
