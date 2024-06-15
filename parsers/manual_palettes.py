import pandas as pd

# manually defined palettes
wanteeed = {
   "name": ["Wanteeed"],
   "palette": ["['#10345c', '#ffacac']"],
   "source": ["wanteeed.com"],
   "kind": ["sequential"]
}
data_to_viz = {
   "name": ["data_to_viz"],
   "palette": ["['#70b4a4', '#280c6c', '#ffffff']"],
   "source": ["data-to-viz.com"],
   "kind": ["categorical"]
}

# list of all manually defined palettes
palettes = [
   wanteeed,
   data_to_viz,
]

def get_manual_palettes(palettes=palettes):
   
   # initialize an empty dataframe
   df = pd.DataFrame()

   # add all palettes to dataframe
   for palette in palettes:
      palette_df = pd.DataFrame(palette)
      df = pd.concat([df, palette_df], axis=0)

   print(f'Manually defined palettes added: {len(palettes)} palettes found')
   return df