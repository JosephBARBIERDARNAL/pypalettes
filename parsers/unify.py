import pandas as pd

palette_path = [
    'pypalettes/matplot_and_seaborn.csv',
    'pypalettes/coolors.csv',
    'pypalettes/paletteer.csv',
]
df = pd.DataFrame()
for path in palette_path:
    temp = pd.read_csv(path)
    df = pd.concat([df, temp])
df.reset_index(drop=True, inplace=True)
df.drop_duplicates(subset='name', keep='first', inplace=True)
df.sort_values('name', inplace=True)
df.to_csv('pypalettes/palettes.csv', index=False)