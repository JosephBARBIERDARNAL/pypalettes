from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import ListedColormap
import pandas as pd

class NyanCat:
    
   def __init__(self):
      self.palettes = pd.read_csv('palettes.csv')

   def load_cmap(self, _from: str = 'id'):
      return None