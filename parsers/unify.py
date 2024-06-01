import pandas as pd

coolors = pd.read_csv('purrpalette/coolors.csv')
paletteer = pd.read_csv('purrpalette/paletteer.csv')

df = pd.concat([coolors, paletteer])
df.to_csv('purrpalette/palettes.csv', index=False)