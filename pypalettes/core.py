from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from difflib import get_close_matches
from pypalettes.utils import load_csv

def load_palettes(palettes_path='palettes.csv'):
    df = load_csv(palettes_path)
    df.set_index('name', inplace=True)
    return df

def get_palette(palettes, name):
    if name == 'random':
        return palettes.sample(1).iloc[0]
    if name not in palettes.index:
        suggestions = get_close_matches(name, palettes.index, n=1, cutoff=0.1)
        raise ValueError(
            f"Palette with name '{name}' not found. Did you mean: '{', '.join(suggestions)}'?\n"
            "See available palettes at https://josephbarbierdarnal.github.io/pypalettes/"
        )
    return palettes.loc[name]

def load_cmap(name='random', type='discrete', palettes_path='palettes.csv'):
    type = type.lower()
    palettes = load_palettes(palettes_path)
    palette = get_palette(palettes, name)
    hex_list = eval(palette['palette'])

    if name == 'random':
        name = palette.name

    if type == 'continuous':
        cmap = LinearSegmentedColormap.from_list(name=f'{name}', colors=hex_list)
    elif type == 'discrete':
        cmap = ListedColormap(name=f'{name}', colors=hex_list)
    else:
        raise ValueError("type argument must be 'continuous' or 'discrete'")

    return cmap

def get_source(name='random', palettes_path='palettes.csv'):
    palettes = load_palettes(palettes_path)
    palette = get_palette(palettes, name)
    return palette['source']

def get_hex(name='random', palettes_path='palettes.csv'):
    palettes = load_palettes(palettes_path)
    palette = get_palette(palettes, name)
    return eval(palette['palette'])

def get_rgb(name='random', palettes_path='palettes.csv'):
    hex_list = get_hex(name, palettes_path)
    rgb_list = [tuple(int(hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) for hex in hex_list]
    return rgb_list


if __name__ == '__main__':
    pass
