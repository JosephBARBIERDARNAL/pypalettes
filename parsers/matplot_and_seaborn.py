import pandas as pd
import matplotlib as mpl
import seaborn as sns
from matplotlib import colors as mcolors
from matplotlib import colormaps

def get_matplotlib_and_seaborn_palettes():

    # get seaborn palettes
    def palette_to_hex(palette_name, n_colors=10):
        palette = sns.color_palette(palette_name, n_colors)
        hex_values = [mcolors.rgb2hex(color) for color in palette]
        return hex_values
    palette_names = ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind']
    diverging_palettes = ['vlag', 'icefire', 'Spectral', 'coolwarm', 'RdBu']
    sequential_palettes = ['rocket', 'mako', 'flare', 'crest', 'viridis', 'plasma', 'inferno', 'magma', 'cividis']
    qualitative_palettes = ['tab10', 'tab20', 'Set1', 'Set2', 'Set3', 'Paired', 'Accent', 'Dark2']
    all_palette_names = palette_names + diverging_palettes + sequential_palettes + qualitative_palettes
    seaborn_palettes = pd.DataFrame({
    'name': all_palette_names,
    'palette': [palette_to_hex(name) for name in all_palette_names],
    'source': ['matplotlib/seaborn builtin' for _ in all_palette_names]
    })

    # get matplotlib palettes
    def cmap_to_hex(cmap_name):
        cmap = mpl.colormaps[cmap_name]
        hex_values = [mpl.colors.rgb2hex(cmap(i)) for i in range(cmap.N)]
        return hex_values
    all_cmap_names = list(colormaps)
    matplotlib_palettes = pd.DataFrame({
        'name': all_cmap_names,
        'palette': [cmap_to_hex(name) for name in all_cmap_names],
        'source': ['matplotlib/seaborn builtin' for _ in all_cmap_names],
        'kind': ['unknown']*len(all_cmap_names),
        'paletteer-kind': ['unknown']*len(all_cmap_names)
    })

    # combine the palettes
    df = pd.concat([seaborn_palettes, matplotlib_palettes])
    df.reset_index(drop=True, inplace=True)
    df.drop_duplicates(subset='name', keep='first', inplace=True)

    print(f'Matplotlib/Seaborn built-in cmaps: {len(df)} palettes found')
    return df