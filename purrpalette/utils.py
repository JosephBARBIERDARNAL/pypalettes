import pandas as pd
from importlib import resources

def load_csv(path='palettes.csv'):
    with resources.open_binary('purrpalette', path) as f:
        return pd.read_csv(f)
