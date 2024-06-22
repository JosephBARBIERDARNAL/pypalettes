from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from difflib import get_close_matches
from PIL import ImageColor
import warnings

from pypalettes.utils import _load_csv

def _load_palettes(palettes_path: str='palettes.csv'):
    """
    Load palettes from csv file
    
    Parameters
    - palettes_path: str
        Path to the csv file with the palettes
    """
    
    df = _load_csv(palettes_path)
    if 'name' not in df.columns or 'palette' not in df.columns:
        raise ValueError("CSV file must contain 'name' and 'palette' columns.")
    
    df.set_index('name', inplace=True)
    return df

def _get_palette(
    palettes,
    name: str,
    reverse: bool = False,
    keep_first_n: int | None = None,
    keep: list[bool] | None = None
):
    """
    Get palette from name

    Parameters
    - name: str
        Name of the palette
    - palettes: pd.DataFrame
        DataFrame with the palettes
    - reverse: bool
        Whether to reverse the order of the colors or not
    - keep_first_n: int
        Keep only the first n colors of the palette
    - keep: list of bool | None
        Specify which colors to keep in the palette
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string.")
    if not isinstance(reverse, bool):
        raise TypeError("reverse must be a boolean.")
    if keep_first_n is not None and (not isinstance(keep_first_n, int) or keep_first_n <= 0):
        raise ValueError("keep_first_n must be a positive integer.")
    if keep is not None and (not isinstance(keep, list) or not all(isinstance(item, bool) for item in keep)):
        raise ValueError("keep must be a list of boolean values.")
    if keep_first_n is not None and keep is not None:
        raise ValueError("Cannot specify both keep_first_n and keep arguments simultaneously.")

    if name == 'random':
        palette = palettes.sample(1).iloc[0]
    else:
        if name not in palettes.index:
            suggestions = get_close_matches(name, palettes.index, n=5, cutoff=0.01)
            raise ValueError(
                f"Palette with name '{name}' not found. Did you mean:\n{', '.join(suggestions)}?\n\n"
                "See available palettes at https://python-graph-gallery.com/color-palette-finder/"
            )
        palette = palettes.loc[name]
    
    try:
        source = palette['source']
        kind = palette['kind']
        paletteer_kind = palette['paletteer-kind']
        hex_list = eval(palette['palette'])
        if not isinstance(hex_list, list) or not all(isinstance(color, str) for color in hex_list):
            raise ValueError("palette must be a list of hex color strings.")
    except Exception as e:
        raise ValueError(f"Error parsing palette: {e}")
    
    if keep_first_n is not None and keep_first_n > len(hex_list):
        raise ValueError(f"keep_first_n ({keep_first_n}) must be less than or equal to the length of the palette ({len(hex_list)}).")
    
    if keep is not None and len(keep) != len(hex_list):
        raise ValueError(f"keep list must be the same length as the palette ({len(hex_list)}!={len(keep)}).")
    
    if reverse:
        hex_list = hex_list[::-1]
    
    if keep_first_n:
        hex_list = hex_list[:keep_first_n]
    elif keep is not None:
        hex_list = [color for color, keep_color in zip(hex_list, keep) if keep_color]

    return hex_list, source, kind, paletteer_kind

def load_cmap(
    name: str = 'random',
    type: str = 'discrete',
    reverse: bool = False,
    keep_first_n: int | None = None,
    keep: list[bool] | None = None,
    type_warning: bool = True
):
    """
    Load colormap from name

    Parameters
    - name: str
        Name of the palette
    - type: str
        Type of colormap: 'continuous' or 'discrete'
    - reverse: bool
        Whether to reverse the order of the colors or not
    - keep_first_n: int
        Keep only the first n colors of the palette
    - keep: list of bool
        Specify which colors to keep in the palette
    - type_warning: bool
        Display warning when using a continuous palette with categorical colors
    """
    if not isinstance(type, str) or type.lower() not in {'continuous', 'discrete'}:
        raise ValueError("type argument must be 'continuous' or 'discrete'")
    
    type = type.lower()
    palettes = _load_palettes()
    hex_list, _, _, paletteer_kind = _get_palette(palettes, name, reverse, keep_first_n, keep)

    if type == 'continuous':
        if paletteer_kind == 'discrete-qualitative':
            if type_warning == True:
                warnings.warn(
                    "Using a continuous palette for a non-sequential palette can pose a problem in terms of the meaning of the graphs. "
                    "Shut down this warning with `type_warning = False`. "
                    "See https://blog.datawrapper.de/colors/ for more information."
                )
        cmap = LinearSegmentedColormap.from_list(name=f'{name}', colors=hex_list)
    elif type == 'discrete':
        cmap = ListedColormap(name=f'{name}', colors=hex_list)

    return cmap

def get_source(
    name = 'random'
):
    """
    Get source of the palette

    Parameters
    - name: str
        Name of the palette
    """
    palettes = _load_palettes()
    _, source, _, _ = _get_palette(palettes, name)
    return source

def get_kind(
    name = 'random'
):
    """
    Get kind of the palette

    Parameters
    - name: str
        Name of the palette
    """
    palettes = _load_palettes()
    _, _, kind, _ = _get_palette(palettes, name)
    return kind

def get_hex(
    name: str = 'random',
    reverse: bool = False,
    keep_first_n: int | None = None,
    keep: list[bool] | None = None
):
    """
    Get hex colors from name

    Parameters
    - name: str
        Name of the palette
    - reverse: bool
        Whether to reverse the order of the colors or not
    - keep_first_n: int
        Keep only the first n colors of the palette
    - keep: list of bool
        Specify which colors to keep in the palette
    """
    palettes = _load_palettes()
    hex_list, _, _, _ = _get_palette(palettes, name, reverse, keep_first_n, keep)
    return hex_list

def get_rgb(
    name: str = 'random',
    reverse: bool = False,
    keep_first_n: int | None = None,
    keep: list[bool] | None = None
):
    """
    Get rgb colors from name

    Parameters
    - name: str
        Name of the palette
    - reverse: bool
        Whether to reverse the order of the colors or not
    - keep_first_n: int
        Keep only the first n colors of the palette
    - keep: list of bool
        Specify which colors to keep in the palette
    """
    hex_list = get_hex(name, reverse, keep_first_n, keep)
    rgb_list = [ImageColor.getcolor(hex, "RGB") for hex in hex_list]
    return rgb_list

if __name__ == '__main__':
    pass
