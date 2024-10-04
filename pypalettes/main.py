from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from typing import Union, List, Optional
from PIL import ImageColor
import warnings
import colorsys

from .get_colors import _get_palette

def load_cmap(
    name: Union[str, List[str]] = 'random',
    cmap_type: str = 'discrete',
    reverse: bool = False,
    keep_first_n: Optional[int] = None,
    keep: Optional[List[bool]] = None,
    type_warning: bool = True
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
    - type_warning
        Display warning when using a continuous palette with categorical colors
    """
    if not isinstance(cmap_type, str) or cmap_type not in {'continuous', 'discrete'}:
        raise ValueError("cmap_type argument must be 'continuous' or 'discrete'")
    
    hex_list, source, kind, paletteer_kind = _get_palette(name, reverse, keep_first_n, keep)

    if cmap_type == 'continuous':
        if paletteer_kind == 'discrete-qualitative':
            if type_warning == True:
                warnings.warn(
                    "Using a continuous palette for a non-sequential palette can pose a problem in terms of the meaning of the graphs."
                    " Shut down this warning with `type_warning = False`. See https://blog.datawrapper.de/colors/ for more information."
                )
        cmap = LinearSegmentedColormap.from_list(name=f'{name}', colors=hex_list)
    elif cmap_type == 'discrete':
        cmap = ListedColormap(name=f'{name}', colors=hex_list)

    cmap.source = source
    cmap.kind = kind
    cmap.hex = hex_list
    cmap.rgb = [ImageColor.getcolor(hex, "RGB") for hex in hex_list]
    cmap.yiq = [colorsys.rgb_to_yiq(rgb[0], rgb[1], rgb[2]) for rgb in cmap.rgb]
    cmap.hls = [colorsys.rgb_to_hls(rgb[0], rgb[1], rgb[2]) for rgb in cmap.rgb]
    cmap.hsv = [colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2]) for rgb in cmap.rgb]

    return cmap
