import pandas as pd
from importlib import resources

def _load_csv(path='palettes.csv'):
    with resources.open_binary('pypalettes', path) as f:
        return pd.read_csv(f)
