import pandas as pd
from bs4 import BeautifulSoup

from utils import split_string

def get_paletteer_palettes():

   # load the HTML file (from: https://pmassicotte.github.io/paletteer_gallery/)
   with open('parsers/html/paletteer.html', 'r') as file:
      soup = BeautifulSoup(file, 'html.parser')

   # initialize lists to store data and the soup
   names = []
   palettes = []
   sources = []
   kinds = []
   sections = soup.find_all('section', class_='level3')

   # iterate over each section found
   for section in sections:
      kind = section['id']
      
      # get the name and source of the palette
      name_tags = section.find_all('center')
      for name_tag in name_tags:
         name = name_tag.text.strip()
         source, name = split_string(name)
         source = f"The R package: {{{source}}}"
         names.append(name)
         sources.append(source)

      # get the hex values and kind of the palette
      palette_tags = section.find_all('hr')
      for palette_tag in palette_tags:
         all_spans = palette_tag.find_previous_sibling('p').find_all('span')
         palette = [span.text for span in all_spans]
         palettes.append(palette)
         kinds.append(kind)

   # create pandas df with palette properties
   df = pd.DataFrame({
      "name": names,
      "palette": palettes,
      "source": sources,
      "kind": kinds
   })

   print(f'Paletteer parsing finished with: {len(palettes)} palettes found')
   return df