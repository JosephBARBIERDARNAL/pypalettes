import pandas as pd

from scrape_paletteer import get_paletteer_palettes
from matplot_and_seaborn import get_matplotlib_and_seaborn_palettes
from manual_palettes import get_manual_palettes

paletteer = get_paletteer_palettes()
matplot_seaborn = get_matplotlib_and_seaborn_palettes()
manual_palettes = get_manual_palettes()

df = pd.concat([matplot_seaborn, paletteer, manual_palettes])
df.reset_index(drop=True, inplace=True)
df.drop_duplicates(subset='name', keep='first', inplace=True)
df.sort_values('name', inplace=True)

print(f'\n Total (unique) palettes found: {len(df)}')
df.to_csv('pypalettes/palettes.csv', index=False)
df.to_json('pypalettes/palettes.json', orient='records')