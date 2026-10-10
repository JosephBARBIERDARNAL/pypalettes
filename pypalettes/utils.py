import csv
import random
import warnings
from difflib import get_close_matches
from importlib import resources


def _load_palettes():
    """
    Load palettes from csv file.

    Parameters
    - palettes_path
        Path to the csv file with the palettes
    """

    palettes_dict: dict = {}
    palettes_file = resources.files("pypalettes").joinpath("palettes.csv")
    with palettes_file.open("r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            palettes_dict[row["name"]] = row

    return palettes_dict


def _get_one_palette(
    name: str | list[str],
    reverse: bool = False,
    keep_first_n: int | None = None,
    keep_last_n: int | None = None,
    keep: list[bool] | None = None,
    remove: int | list[int] | None = None,
) -> dict:
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
    - remove
        Remove colors at specified indices (0-indexed). Can be a single int or list of ints.
    """
    palettes = _load_palettes()
    palette_dict: dict = {}
    if name == "random":
        palette = random.choice(list(palettes.values()))
    else:
        if name not in palettes:
            suggestions: list = get_close_matches(
                name, palettes.keys(), n=5, cutoff=0.01
            )
            raise ValueError(
                f"Palette with name '{name}' not found. Did you mean:\n{', '.join(suggestions)}?\n\n"  # ty: ignore
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

    if remove is not None:
        remove_indices = [remove] if isinstance(remove, int) else remove
        for idx in remove_indices:
            if not isinstance(idx, int):
                raise TypeError(
                    f"remove indices must be integers, not {type(idx).__name__}."
                )
            if idx < 0 or idx >= len(hex_list):
                raise ValueError(
                    f"remove index {idx} is out of range. Must be between 0 and {len(hex_list) - 1}."
                )

    if reverse:
        hex_list: list = hex_list[::-1]

    if keep_first_n:
        hex_list: list = hex_list[:keep_first_n]
    elif keep_last_n:
        hex_list: list = hex_list[-keep_last_n:]
    elif keep is not None:
        hex_list: list = [
            color for color, keep_color in zip(hex_list, keep) if keep_color
        ]

    if remove is not None:
        remove_indices = [remove] if isinstance(remove, int) else remove
        remove_set = set(remove_indices)
        hex_list: list = [
            color for idx, color in enumerate(hex_list) if idx not in remove_set
        ]

    palette_dict["palette"] = palette
    palette_dict["hex_list"] = hex_list
    palette_dict["source"] = source
    palette_dict["kind"] = kind
    palette_dict["paletteer_kind"] = paletteer_kind

    return palette_dict


def _get_palette(
    name: str | list[str],
    reverse: bool = False,
    keep_first_n: int | None = None,
    keep_last_n: int | None = None,
    keep: list[bool] | None = None,
    repeat: int = 1,
    remove: int | list[int] | None = None,
) -> dict:
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
    - remove
        Remove colors at specified indices (0-indexed). Can be a single int or list of ints.
    """
    if not isinstance(reverse, bool):
        raise TypeError("reverse must be a boolean.")
    if keep_first_n is not None and (
        not isinstance(keep_first_n, int) or keep_first_n <= 0
    ):
        raise TypeError("keep_first_n must be a positive integer, not {keep_first_n}.")
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
            "Cannot specify more than one of keep_first_n, keep_last_n, "
            "and keep arguments simultaneously."
        )
    if remove is not None:
        if isinstance(remove, int):
            if remove < 0:
                raise ValueError("remove index must be non-negative.")
        elif isinstance(remove, list):
            if not all(isinstance(idx, int) for idx in remove):
                raise TypeError("remove must be an int or list of ints.")
            if any(idx < 0 for idx in remove):
                raise ValueError("remove indices must be non-negative.")
        else:
            raise TypeError("remove must be an int or list of ints.")
    if not repeat >= 1 or not isinstance(repeat, int):
        raise TypeError("repeat must be a positive integer.")

    if isinstance(name, str):
        palette_dict: dict = _get_one_palette(
            name=name,
            reverse=reverse,
            keep_first_n=keep_first_n,
            keep_last_n=keep_last_n,
            keep=keep,
            remove=remove,
        )
    elif isinstance(name, list):
        for param in [keep_first_n, keep_last_n, keep, remove]:
            if param is not None:
                warnings.warn(
                    "`keep_first_n`, `keep_last_n`, `keep` and `remove` arguments"
                    " are ignored when `name` is a list."
                )
        hex_list: list = []
        source: list = []
        kind: list = []
        paletteer_kind: list = []
        for palette_name in name:
            one_palette_dict: dict = _get_one_palette(name=palette_name)
            hex_list.extend(one_palette_dict["hex_list"])
            source.append(one_palette_dict["source"])
            kind.append(one_palette_dict["kind"])
            paletteer_kind.append(one_palette_dict["paletteer_kind"])

        palette_dict: dict = {}
        palette_dict["hex_list"] = hex_list
        palette_dict["source"] = source
        palette_dict["kind"] = kind
        palette_dict["paletteer_kind"] = paletteer_kind
    else:
        raise TypeError("`name` must be a string or a list of strings")

    palette_dict["hex_list"] *= repeat

    return palette_dict
