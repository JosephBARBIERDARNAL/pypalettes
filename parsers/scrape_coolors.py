import pandas as pd
import random
from bs4 import BeautifulSoup

from utils import generate_palette_name

def get_coolors_palettes():

    # read the html content (from: https://coolors.co/palettes/trending)
    with open('parsers/html/coolors.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    palette_cols = soup.find_all('div', class_='explore-palettes_col')

    # initialize lists to store data
    palettes = []
    hex_values_list = []
    rgb_values_list = []

    # extract data from each palette column
    for palette_col in palette_cols:
        
        # generate palette id with letters and digits
        palette_name = generate_palette_name()
        color_divs = palette_col.find_all('div', class_='palette-card_colors')[0].find_all('div')
        
        # extract hex values and RGB values
        hex_values = []
        rgb_values = []
        for color_div in color_divs:
            hex_value = color_div.find('span').text.strip()
            rgb_style = color_div['style']
            rgb_value = tuple(map(int, rgb_style.split('(')[1].split(')')[0].split(',')))
            
            # append the values to the lists
            hex_values.append('#'+hex_value)
            rgb_values.append(rgb_value)
        
        # append the data to the lists
        palettes.append(palette_name)
        hex_values_list.append(hex_values)
        rgb_values_list.append(rgb_values)

    # store the palettes
    df = pd.DataFrame({
        'name': palettes,
        'palette': hex_values_list,
        'source': ['coolors.co']*len(palettes),
        'kind': ['unknown']*len(palettes),
        'paletteer-kind': ['unknown']*len(palettes)
    })

    print(f'Coolors.co parsing finished with: {len(palettes)} palettes found')
    return df