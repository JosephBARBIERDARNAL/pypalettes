import pytest
import pandas as pd

from pypalettes.get_colors import _load_palettes, _PALETTES_CACHE


class TestLoadFile:
    def test_load_palettes(self):
        global _PALETTES_CACHE
        _PALETTES_CACHE = None

        palettes = pd.DataFrame(_load_palettes())[
            ["Abbott", "Acadia", "Acanthisthius_brasilianus"]
        ].to_dict()

        expected_palettes = {
            "Abbott": {
                "name": "Abbott",
                "palette": "['#950404FF', '#E04B28FF', '#C38961FF', '#9F5630FF', '#388F30FF', '#0F542FFF', '#007D82FF', '#004042FF']",
                "source": "The R package: {MoMAColors}",
                "kind": "qualitative",
                "paletteer-kind": "discrete-qualitative",
            },
            "Acadia": {
                "name": "Acadia",
                "palette": "['#FED789FF', '#023743FF', '#72874EFF', '#476F84FF', '#A4BED5FF', '#453947FF']",
                "source": "The R package: {nationalparkcolors}",
                "kind": "qualitative",
                "paletteer-kind": "discrete-qualitative",
            },
            "Acanthisthius_brasilianus": {
                "name": "Acanthisthius_brasilianus",
                "palette": "['#527E87FF', '#B88244FF', '#B8B69EFF', '#B48F2CFF', '#A37903FF']",
                "source": "The R package: {fishualize}",
                "kind": "qualitative",
                "paletteer-kind": "discrete-qualitative",
            },
        }

        assert palettes == expected_palettes


if __name__ == "__main__":
    pytest.main()
