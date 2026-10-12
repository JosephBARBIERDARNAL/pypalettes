from typing import Literal

from pypalettes.create_cmap import create_cmap
from pypalettes.deprecated import add_cmap, get_hex, get_kind, get_rgb, get_source
from pypalettes.load_cmap import load_cmap
from pypalettes.load_palette import load_palette
from pypalettes.show_cmap import show_cmap

__version__: Literal["0.2.2"] = "0.2.2"
__all__: list[str] = [
    "add_cmap",
    "create_cmap",
    "get_hex",
    "get_kind",
    "get_rgb",
    "get_source",
    "load_cmap",
    "load_palette",
    "show_cmap",
]
