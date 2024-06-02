from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from difflib import get_close_matches

from purrpalette.utils import load_csv

class PurrPalette:
    
    def __init__(self, palettes_path='palettes.csv'):
        df = load_csv(palettes_path)
        self.palettes = df
        self.palettes.set_index('name', inplace=True)
        self.name = None

    def _get_palette(self, name):
        if name == 'random':
            return self.palettes.sample(1).iloc[0]
        if name not in self.palettes.index:
            suggestions = get_close_matches(name, self.palettes.index, n=1)
            raise ValueError(
                f"Palette with name '{name}' not found. Did you mean: '{', '.join(suggestions)}'?\n"
                "See available palettes at https://josephbarbierdarnal.github.io/purrpalette/"
            )
        return self.palettes.loc[name]

    def load_cmap(self, name='random', type='qualitative'):
        palette = self._get_palette(name)
        hex_list = eval(palette['palette'])

        if name == 'random':
            name = palette.name

        if type == 'continuous':
            cmap = LinearSegmentedColormap.from_list(name=f'{name}', colors=hex_list)
        elif type == 'qualitative':
            cmap = ListedColormap(name=f'{name}', colors=hex_list)
        else:
            raise ValueError("type argument must be 'continuous' or 'qualitative'")

        self.name = name
        self.cmap = cmap
        return cmap
    
    def source(self, name='random'):
        palette = self._get_palette(name)
        return palette['source']

    def hex(self, name='random'):
        palette = self._get_palette(name)
        return eval(palette['palette'])

    def rgb(self, name='random'):
        hex_list = self.hex(name)
        rgb_list = [tuple(int(hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) for hex in hex_list]
        return rgb_list



if __name__ == '__main__':
    pass