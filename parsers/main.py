import pandas as pd

from scrape_coolors import get_coolors_palettes
from scrape_paletteer import get_paletteer_palettes
from matplot_and_seaborn import get_matplotlib_and_seaborn_palettes

coolors = get_coolors_palettes()
paletteer = get_paletteer_palettes()
matplot_seaborn = get_matplotlib_and_seaborn_palettes()

df = pd.concat([matplot_seaborn, coolors, paletteer])
df.reset_index(drop=True, inplace=True)
df.drop_duplicates(subset='name', keep='first', inplace=True)
df.sort_values('name', inplace=True)

print(f'\n\n Total (unique) palettes found: {len(df)}')
df.to_csv('pypalettes/palettes.csv', index=False)