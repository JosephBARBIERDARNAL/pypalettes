import pandas as pd
from bs4 import BeautifulSoup

from utils import split_string

# load the HTML file (https://pmassicotte.github.io/paletteer_gallery/)
with open('parsers/paletteer.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# initialize lists to store data and the soup
names = []
palettes = []
sources = []
sections = soup.find_all('section', class_='level3')

# iterate over each section found
for section in sections:
    
   # get the name of the palette
   name_tags = section.find_all('center')
   for name_tag in name_tags:
      name = name_tag.text.strip()
      source, name = split_string(name)
      names.append(name)
      sources.append(source)

   # get the hex values of the palette
   palette_tags = section.find_all('hr')
   for palette_tag in palette_tags:
      all_spans = palette_tag.find_previous_sibling('p').find_all('span')
      palette = [span.text for span in all_spans]
      palettes.append(palette)

# save palettes to csv
df = pd.DataFrame({
   "name": names,
   "palette": palettes,
   "source": sources
})
df.to_csv("purrpalette/paletteer.csv", index=False)

print(f'Paletteer parsing finished with: {len(palettes)} palettes found')