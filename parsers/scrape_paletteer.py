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
   paletteer_kinds = []

   # find sections that separate discrete and continuous palettes
   sections = soup.find_all('section', class_='level2')

   for section in sections:

      # get whether we're in the discrete or continuous section
      first_kind = section['id'].split('-')[0]

      sub_sections = soup.find_all('section', class_='level3')

      # iterate over each sub_section found
      for sub_section in sub_sections:
         kind = sub_section['id']
         
         # get the name and source of the palette
         name_tags = sub_section.find_all('center')
         for name_tag in name_tags:
            name = name_tag.text.strip()
            source, name = split_string(name)
            source = f"The R package: {{{source}}}"
            names.append(name)
            sources.append(source)

         # get the hex values and kind of the palette
         palette_tags = sub_section.find_all('hr')
         for palette_tag in palette_tags:
            all_spans = palette_tag.find_previous_sibling('p').find_all('span')
            palette = [span.text for span in all_spans]
            palettes.append(palette)
            kinds.append(kind)
            paletteer_kind = f'{first_kind}-{kind}'
            paletteer_kind = paletteer_kind if not paletteer_kind.endswith('-1') else paletteer_kind[:-2]
            paletteer_kinds.append(paletteer_kind)

      # create pandas df with palette properties
      df = pd.DataFrame({
         "name": names,
         "palette": palettes,
         "source": sources,
         "kind": kinds,
         "paletteer-kind": paletteer_kinds
      })

      print(f'Paletteer parsing finished with: {len(palettes)} palettes found')
      return df

if __name__ == "__main__":
   get_paletteer_palettes()