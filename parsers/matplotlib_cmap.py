import pandas as pd
import matplotlib as mpl
from matplotlib import colormaps

def cmap_to_hex(cmap_name):
    cmap = mpl.colormaps[cmap_name]
    hex_values = [mpl.colors.rgb2hex(cmap(i)) for i in range(cmap.N)]
    return hex_values

all_cmap_names = list(colormaps)
cmap_data = {
    'name': all_cmap_names,
    'palette': [cmap_to_hex(name) for name in all_cmap_names],
    'source': ['matplotlib builtin' for _ in all_cmap_names]
}

df_cmaps = pd.DataFrame(cmap_data)
df_cmaps.to_csv('purrpalette/matplotlib.csv', index=False)

print(f'Matplotlib built-in cmaps: {len(all_cmap_names)} palettes found')