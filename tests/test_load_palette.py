import pytest

from pypalettes import load_palette


def test_load_palette():
    assert load_palette("Acadia") == [
        "#FED789FF",
        "#023743FF",
        "#72874EFF",
        "#476F84FF",
        "#A4BED5FF",
        "#453947FF",
    ]

    assert load_palette("kadabra") == [
        "#D0B000FF",
        "#F8E828FF",
        "#886000FF",
        "#603000FF",
        "#886010FF",
        "#A88028FF",
        "#F8F8F8FF",
        "#585858FF",
        "#F8F878FF",
        "#D8D8D8FF",
        "#B0B0B0FF",
        "#F04030FF",
        "#F08888FF",
        "#D0B050FF",
    ]


@pytest.mark.parametrize("repeat", [1, 3])
@pytest.mark.parametrize("keep_first_n", [None, 1])
@pytest.mark.parametrize("reverse", [True, False])
@pytest.mark.parametrize("shuffle", [True, 1, False])
def test_load_palette_random(shuffle, repeat, keep_first_n, reverse):
    """Randomly load 30 palettes"""
    n: int = 30
    for _ in range(n):
        palette: list[str] = load_palette(
            shuffle=shuffle,
            repeat=repeat,
            keep_first_n=keep_first_n,
            reverse=reverse,
        )
        assert isinstance(palette, list)
        assert all(isinstance(color, str) for color in palette)


def test_load_palette_remove_single():
    """Test removing a single color by index"""
    palette = load_palette("Acadia", remove=2)
    assert palette == [
        "#FED789FF",
        "#023743FF",
        "#476F84FF",
        "#A4BED5FF",
        "#453947FF",
    ]
    assert len(palette) == 5


def test_load_palette_remove_multiple():
    """Test removing multiple colors by index"""
    palette = load_palette("Acadia", remove=[1, 3])
    assert palette == [
        "#FED789FF",
        "#72874EFF",
        "#A4BED5FF",
        "#453947FF",
    ]
    assert len(palette) == 4


def test_load_palette_remove_first_and_last():
    """Test removing first and last colors"""
    palette = load_palette("Acadia", remove=[0, 5])
    assert palette == [
        "#023743FF",
        "#72874EFF",
        "#476F84FF",
        "#A4BED5FF",
    ]
    assert len(palette) == 4


def test_load_palette_remove_with_reverse():
    """Test remove combined with reverse"""
    # First reverse, then remove
    palette = load_palette("Acadia", reverse=True, remove=0)
    expected = [
        "#A4BED5FF",
        "#476F84FF",
        "#72874EFF",
        "#023743FF",
        "#FED789FF",
    ]
    assert palette == expected


def test_load_palette_remove_invalid_index():
    """Test that invalid indices raise appropriate errors"""
    with pytest.raises(ValueError, match="out of range"):
        load_palette("Acadia", remove=10)

    with pytest.raises(ValueError, match="non-negative"):
        load_palette("Acadia", remove=-1)

    with pytest.raises(ValueError, match="out of range"):
        load_palette("Acadia", remove=[0, 10])


def test_load_palette_remove_invalid_type():
    """Test that invalid types raise appropriate errors"""
    with pytest.raises(TypeError, match="remove must be an int or list of ints"):
        load_palette("Acadia", remove="2")

    with pytest.raises(TypeError, match="remove must be an int or list of ints"):
        load_palette("Acadia", remove=[1, "2"])
