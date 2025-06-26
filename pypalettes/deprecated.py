from typing import Union, List, Optional
from PIL import ImageColor
import warnings
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

from .utils import _get_palette

warnings.simplefilter("always")


def make_warning_message(func, name, attribute):
    message = f"""
The {func.__name__}() function is deprecated and will be removed in a future version.
Please, use: load_cmap('{name}').{attribute}
"""
    return message


def get_source(name: Union[str, List[str]] = "random"):
    """
    Deprecated. Get source of the palette.

    Parameters
    - name
        Name of the palette
    """
    warning_message = make_warning_message(
        func=get_source, name=name, attribute="source"
    )
    warnings.warn(warning_message, category=DeprecationWarning)
    _, source, _, _ = _get_palette(name)
    return source


def get_kind(name: Union[str, List[str]] = "random"):
    """
    Deprecated. Get kind of the palette

    Parameters
    - name
        Name of the palette
    """
    warning_message = make_warning_message(func=get_kind, name=name, attribute="kind")
    warnings.warn(warning_message, category=DeprecationWarning)
    _, _, kind, _ = _get_palette(name)
    return kind


def get_hex(
    name: Union[str, List[str]] = "random",
    reverse: bool = False,
    keep_first_n: Optional[int] = None,
    keep_last_n: Optional[int] = None,
    keep: Optional[List[bool]] = None,
    raise_warn: bool = True,
):
    """
    Deprecated. Get hex colors from name.

    Parameters
    - name
        Name of the palette
    - reverse
        Whether to reverse the order of the colors or not
    - keep_first_n
        Keep only the first n colors of the palette
    - keep
        Specify which colors to keep in the palette
    """
    if raise_warn:
        warning_message = make_warning_message(func=get_hex, name=name, attribute="hex")
        warnings.warn(warning_message, category=DeprecationWarning)
    hex_list, _, _, _ = _get_palette(name, reverse, keep_first_n, keep_last_n, keep)
    return hex_list


def get_rgb(
    name: Union[str, List[str]] = "random",
    reverse: bool = False,
    keep_first_n: Optional[int] = None,
    keep_last_n: Optional[int] = None,
    keep: Optional[List[bool]] = None,
):
    """
    Deprecated. Get rgb colors from name.

    Parameters
    - name
        Name of the palette
    - reverse
        Whether to reverse the order of the colors or not
    - keep_first_n
        Keep only the first n colors of the palette
    - keep
        Specify which colors to keep in the palette
    """
    warning_message = make_warning_message(func=get_rgb, name=name, attribute="rgb")
    warnings.warn(warning_message, category=DeprecationWarning)
    hex_list = get_hex(name, reverse, keep_first_n, keep_last_n, keep, raise_warn=False)
    rgb_list = [ImageColor.getcolor(hex, "RGB") for hex in hex_list]
    return rgb_list


def add_cmap(
    colors: List, name: str, cmap_type: str = "discrete"
) -> Union[LinearSegmentedColormap, ListedColormap]:
    """
    Deprecated function, used `create_cmap()` instead
    """
    raise RuntimeError(
        "This function is no longer available, use `create_cmap()` instead."
    )
