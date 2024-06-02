import pandas as pd

palette_path = [
   'purrpalette/coolors.csv',
   'purrpalette/paletteer.csv'
]
df = pd.DataFrame()
for path in palette_path:
    temp = pd.read_csv(path)
    df = pd.concat([df, temp])
df.reset_index(drop=True, inplace=True)
df.sort_values('name', inplace=True)
df.drop_duplicates(subset='name', keep='first', inplace=True)
df.to_csv('purrpalette/palettes.csv', index=False)