from matplotlib.colors import LinearSegmentedColormap, ListedColormap
import pandas as pd

class NyanCat:
    
    def __init__(self, palettes_path='palettes.csv'):
        self.palettes = pd.read_csv(palettes_path)
        self.palettes.set_index('id', inplace=True)

    def _get_palette(self, id):
        if id == 'random':
            return self.palettes.sample(1).iloc[0]
        if id not in self.palettes.index:
            raise ValueError(f"Palette with id '{id}' not found. Please choose from\n{self.palettes.index.values}")
        return self.palettes.loc[id]

    def load_cmap(self, id='random', cmap_type='continuous'):
        palette = self._get_palette(id)
        hex_list = eval(palette['hex'])

        if cmap_type == 'continuous':
            cmap = LinearSegmentedColormap.from_list(name=f'{id}', colors=hex_list)
        elif cmap_type == 'qualitative':
            cmap = ListedColormap(name=f'{id}', colors=hex_list)
        else:
            raise ValueError("cmap_type argument must be 'continuous' or 'qualitative'")

        self.id = id
        self.cmap = cmap
        return cmap

    def hex(self, id='random'):
        palette = self._get_palette(id)
        return eval(palette['hex'])

    def rgb(self, id='random'):
        hex_list = self.hex(id)
        rgb_list = [tuple(int(hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) for hex in hex_list]
        return rgb_list
