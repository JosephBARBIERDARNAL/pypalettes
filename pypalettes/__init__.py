import matplotlib as mpl
from .main import load_cmap
from .deprecated import get_source, get_hex, get_rgb, get_kind
from .make import add_cmap
from .get_colors import _load_palettes

__all__ = ["load_cmap", "add_cmap"]

for palette_name in _load_palettes():
    cmap_discrete = load_cmap(name=palette_name)
    cmap_continuous = load_cmap(name=palette_name, cmap_type="continuous")
    cmap_continuous.name = cmap_continuous.name + "_gradient"
    try:
        mpl.colormaps.register(cmap=cmap_discrete)
        mpl.colormaps.register(cmap=cmap_continuous)
    except ValueError:
        pass
