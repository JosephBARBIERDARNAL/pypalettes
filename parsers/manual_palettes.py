import pandas as pd
from list_manual_palettes import palettes

def get_manual_palettes(palettes=palettes):
   df = pd.DataFrame()
   for key, value in palettes.items():
      palette_df = pd.DataFrame(value)
      df = pd.concat([df, palette_df], axis=0)
   print(f'Manually defined palettes added: {len(palettes)} palettes found')
   return df


if __name__ == "__main__":
   get_manual_palettes()