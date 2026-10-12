import warnings

from pypalettes.utils import _get_palette

warnings.simplefilter("always")


def make_warning_message(func, name, attribute) -> str:
    message: str = f"""
The {func.__name__}() function is deprecated and will be removed in a future version.
Please, use: load_cmap('{name}').{attribute}
"""
    return message


def get_source(name: str | list[str] = "random") -> str:
    """
    Deprecated. Get source of the palette.

    Parameters
    - name
        Name of the palette
    """
    warning_message: str = make_warning_message(
        func=get_source, name=name, attribute="source"
    )
    warnings.warn(warning_message, category=DeprecationWarning)
    palette: dict = _get_palette(name)
    return palette["source"]


def get_kind(name: str | list[str] = "random"):
    """
    Deprecated. Get kind of the palette

    Parameters
    - name
        Name of the palette
    """
    warning_message: str = make_warning_message(
        func=get_kind, name=name, attribute="kind"
    )
    warnings.warn(warning_message, category=DeprecationWarning)
    palette: dict = _get_palette(name)
    return palette["kind"]


def get_hex(
    name: str | list[str] = "random",
    reverse: bool = False,
    keep_first_n: int | None = None,
    keep_last_n: int | None = None,
    keep: list[bool] | None = None,
    raise_warn: bool = True,
) -> list:
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
        warning_message: str = make_warning_message(
            func=get_hex, name=name, attribute="hex"
        )
        warnings.warn(warning_message, category=DeprecationWarning)
    palette: dict = _get_palette(name, reverse, keep_first_n, keep_last_n, keep)
    return palette["hex_list"]


def get_rgb(
    name: str | list[str] = "random",
    reverse: bool = False,
    keep_first_n: int | None = None,
    keep_last_n: int | None = None,
    keep: list[bool] | None = None,
) -> list:
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
    from PIL import ImageColor

    warning_message: str = make_warning_message(
        func=get_rgb, name=name, attribute="rgb"
    )
    warnings.warn(warning_message, category=DeprecationWarning)
    hex_list: list = get_hex(
        name, reverse, keep_first_n, keep_last_n, keep, raise_warn=False
    )
    rgb_list: list = [ImageColor.getcolor(hex, "RGB") for hex in hex_list]
    return rgb_list


def add_cmap(colors: list, name: str, cmap_type: str = "discrete") -> None:
    """
    Deprecated function, used `create_cmap()` instead
    """
    raise RuntimeError(
        "This function is no longer available, use `create_cmap()` instead."
    )
