import pytest
import re
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from pypalettes import create_cmap, add_cmap


def test_create_cmap_discrete():
    colors = ["red", "green", "blue"]
    cmap = create_cmap(colors, cmap_type="discrete", name="test_discrete")

    assert isinstance(cmap, ListedColormap)
    assert cmap.name == "test_discrete"
    assert cmap.colors == colors


def test_create_cmap_continuous():
    colors = ["red", "green", "blue"]
    cmap = create_cmap(colors, cmap_type="continuous", name="test_continuous")

    assert isinstance(cmap, LinearSegmentedColormap)
    assert cmap.name == "test_continuous"


def test_create_cmap_default_type():
    colors = ["red", "green", "blue"]
    cmap = create_cmap(colors, name="mycustomcmap")

    assert isinstance(cmap, ListedColormap)
    assert cmap.name == "mycustomcmap"
    assert cmap.colors == colors


def test_create_cmap_invalid_type():
    colors = ["red", "green", "blue"]

    with pytest.raises(
        ValueError, match="cmap_type argument must be 'continuous' or 'discrete'"
    ):
        create_cmap(colors, cmap_type="invalid", name="mycustomcmap")


def test_create_cmap_single_color():
    cmap = create_cmap(["red"], name="mycustomcmap")

    assert isinstance(cmap, ListedColormap)
    assert cmap.colors == ["red"]


def test_create_cmap_many_colors():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    cmap = create_cmap(colors, cmap_type="continuous", name="mycustomcmap")

    assert isinstance(cmap, LinearSegmentedColormap)
    assert cmap.name == "mycustomcmap"


def test_invalid_function():
    with pytest.raises(
        RuntimeError,
        match=re.escape(
            "This function is no longer available, use `create_cmap()` instead."
        ),
    ):
        add_cmap(
            ["red", "orange", "yellow"],
            cmap_type="continuous",
            name="mycustomcmap",
        )
