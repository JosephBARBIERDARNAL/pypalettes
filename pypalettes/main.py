from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from difflib import get_close_matches
from pypalettes.utils import load_csv

def load_palettes(palettes_path='palettes.csv'):
    """
    Load palettes from csv file
    
    Parameters
    - palettes_path: str
        Path to the csv file with the palettes
    """
    
    df = load_csv(palettes_path)
    if 'name' not in df.columns or 'palette' not in df.columns:
        raise ValueError("CSV file must contain 'name' and 'palette' columns.")
    
    df.set_index('name', inplace=True)
    return df

def _get_palette(palettes, name, reverse=False, keep_first_n=None):
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
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string.")
    if not isinstance(reverse, bool):
        raise TypeError("reverse must be a boolean.")
    if keep_first_n is not None and (not isinstance(keep_first_n, int) or keep_first_n <= 0):
        raise ValueError("keep_first_n must be a positive integer.")
    
    if name == 'random':
        palette = palettes.sample(1).iloc[0]
    else:
        if name not in palettes.index:
            suggestions = get_close_matches(name, palettes.index, n=1, cutoff=0.1)
            raise ValueError(
                f"Palette with name '{name}' not found. Did you mean: '{', '.join(suggestions)}'?\n"
                "See available palettes at https://josephbarbierdarnal.github.io/pypalettes/"
            )
        palette = palettes.loc[name]
    
    try:
        source = palette['source']
        kind = palette['kind']
        hex_list = eval(palette['palette'])
        if not isinstance(hex_list, list) or not all(isinstance(color, str) for color in hex_list):
            raise ValueError("palette must be a list of hex color strings.")
    except Exception as e:
        raise ValueError(f"Error parsing palette: {e}")
    
    if len(hex_list) == 0:
        raise ValueError("palette cannot be empty.")
    
    if keep_first_n is not None and keep_first_n > len(hex_list):
        raise ValueError(f"keep_first_n {keep_first_n} must be less than or equal to the length of the palette {len(hex_list)}.")
    
    if reverse:
        hex_list = hex_list[::-1]
    if keep_first_n:
        hex_list = hex_list[:keep_first_n]

    return hex_list, source, kind

def load_cmap(
    name='random',
    type='discrete',
    reverse=False,
    keep_first_n=None
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
    """
    if not isinstance(type, str) or type.lower() not in {'continuous', 'discrete'}:
        raise ValueError("type argument must be 'continuous' or 'discrete'")
    
    type = type.lower()
    palettes = load_palettes()
    hex_list, _, _ = _get_palette(palettes, name, reverse, keep_first_n)

    if type == 'continuous':
        cmap = LinearSegmentedColormap.from_list(name=f'{name}', colors=hex_list)
    elif type == 'discrete':
        cmap = ListedColormap(name=f'{name}', colors=hex_list)

    return cmap

def get_source(
    name='random'
):
    """
    Get source of the palette

    Parameters
    - name: str
        Name of the palette
    """
    palettes = load_palettes()
    _, source, _ = _get_palette(palettes, name)
    return source

def get_kind(
    name='random'
):
    """
    Get kind of the palette

    Parameters
    - name: str
        Name of the palette
    """
    palettes = load_palettes()
    _, _, kind = _get_palette(palettes, name)
    return kind

def get_hex(
    name='random',
    reverse=False,
    keep_first_n=None
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
    """
    palettes = load_palettes()
    hex_list, _, _ = _get_palette(palettes, name, reverse, keep_first_n)
    return hex_list

def get_rgb(
    name='random',
    reverse=False,
    keep_first_n=None
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
    """
    hex_list = get_hex(name, reverse, keep_first_n)
    rgb_list = [tuple(int(hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) for hex in hex_list]
    return rgb_list

if __name__ == '__main__':
    pass
