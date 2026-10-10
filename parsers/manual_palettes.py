import pandas as pd

from parsers.list_manual_palettes import palettes


def get_manual_palettes(palettes=palettes):
    df = pd.DataFrame()
    for value in palettes.values():
        palette_df = pd.DataFrame(value)
        df = pd.concat([df, palette_df], axis=0)
    print(f"Manually defined palettes added: {len(palettes)} palettes found")
    return df


if __name__ == "__main__":
    get_manual_palettes()
