from .main import load_cmap
from .deprecated import get_source, get_hex, get_rgb, get_kind, add_cmap
from .create import create_cmap
from .show import show_cmap

__version__ = "0.1.5"
__all__ = [
    "load_cmap",
    "add_cmap",
    "create_cmap",
    "show_cmap",
    "get_source",
    "get_hex",
    "get_rgb",
    "get_kind",
]
