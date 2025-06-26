import pytest
import pandas as pd

from pypalettes.utils import _load_palettes, _get_one_palette, _get_palette

@pytest.mark.parametrize(
    "palette_name, expected_palette",
    [
        (
            "Abbott",
            {
                "name": "Abbott",
                "palette": "['#950404FF', '#E04B28FF', '#C38961FF', '#9F5630FF', '#388F30FF', '#0F542FFF', '#007D82FF', '#004042FF']",
                "source": "The R package: {MoMAColors}",
                "kind": "qualitative",
                "paletteer-kind": "discrete-qualitative",
            },
        ),
        (
            "Acadia",
            {
                "name": "Acadia",
                "palette": "['#FED789FF', '#023743FF', '#72874EFF', '#476F84FF', '#A4BED5FF', '#453947FF']",
                "source": "The R package: {nationalparkcolors}",
                "kind": "qualitative",
                "paletteer-kind": "discrete-qualitative",
            },
        ),
        (
            "Acanthisthius_brasilianus",
            {
                "name": "Acanthisthius_brasilianus",
                "palette": "['#527E87FF', '#B88244FF', '#B8B69EFF', '#B48F2CFF', '#A37903FF']",
                "source": "The R package: {fishualize}",
                "kind": "qualitative",
                "paletteer-kind": "discrete-qualitative",
            },
        ),
    ],
)
def test_load_palettes(palette_name, expected_palette):
    global _PALETTES_CACHE
    _PALETTES_CACHE = None

    palettes = pd.DataFrame(_load_palettes()).to_dict()

    assert palette_name in palettes
    assert palettes[palette_name] == expected_palette



def test_get_one_palette_errors():
    with pytest.raises(ValueError, match=r"^keep_first_n \("):
        _get_one_palette("Acadia", keep_first_n=10)

    with pytest.raises(ValueError, match=r"^keep_last_n \("):
        _get_one_palette("Acadia", keep_last_n=10)

    with pytest.raises(ValueError, match=r"^keep list must be the same length as the palette"):
        _get_one_palette("Acadia", keep=[True])


def test_get_palette_errors():
    with pytest.raises(TypeError, match="reverse must be a boolean."):
        _get_palette("Acadia", reverse="invalid type")

    with pytest.raises(TypeError, match=r"^keep_first_n must be a positive integer, not "):
        _get_palette("Acadia", keep_first_n="invalid type")

    with pytest.raises(TypeError, match=r"^keep_last_n must be a positive integer, not "):
        _get_palette("Acadia", keep_last_n="invalid type")

    with pytest.raises(TypeError, match=r"^keep must be a list of boolean values, not"):
        _get_palette("Acadia", keep="invalid type")

    with pytest.raises(TypeError, match=r"`name` must be a string or a list of strings"):
        _get_palette(17)

    with pytest.raises(ValueError, match="Cannot specify more than one of keep_first_n, keep_last_n, and keep arguments simultaneously."):
        _get_palette("Acadia", keep_first_n=3, keep_last_n=2)

    with pytest.warns(match="`keep_first_n`, `keep_last_n` and `keep` arguments are ignored when `name` is a list."):
        _get_palette(["Acadia", "Sunset"], keep_first_n=3, repeat=2)
