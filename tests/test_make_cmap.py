import pytest
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
import matplotlib as mpl
from pypalettes import add_cmap


class TestMakeCmap:
    def test_add_cmap_discrete(self):
        colors = ["red", "green", "blue"]
        cmap = add_cmap(colors, cmap_type="discrete", name="test_discrete")

        assert isinstance(cmap, ListedColormap)
        assert cmap.name == "test_discrete"
        assert cmap.colors == colors

    def test_add_cmap_continuous(self):
        colors = ["red", "green", "blue"]
        cmap = add_cmap(colors, cmap_type="continuous", name="test_continuous")

        assert isinstance(cmap, LinearSegmentedColormap)
        assert cmap.name == "test_continuous"

    def test_add_cmap_default_type(self):
        colors = ["red", "green", "blue"]
        cmap = add_cmap(colors, name="mycustomcmap")

        assert isinstance(cmap, ListedColormap)
        assert cmap.name == "mycustomcmap"
        assert cmap.colors == colors

    def test_add_cmap_is_registered(self):
        colors = ["red", "green", "blue"]
        add_cmap(colors, name="mycustomcmap")
        cmap = mpl.colormaps["mycustomcmap"]
        assert isinstance(cmap, ListedColormap)
        assert cmap.name == "mycustomcmap"
        assert cmap.colors == colors

    def test_add_cmap_invalid_type(self):
        colors = ["red", "green", "blue"]

        with pytest.raises(ValueError) as excinfo:
            add_cmap(colors, cmap_type="invalid", name="mycustomcmap")

        assert (
            str(excinfo.value)
            == "cmap_type argument must be 'continuous' or 'discrete'"
        )

    def test_add_cmap_single_color(self):
        cmap = add_cmap(["red"], name="mycustomcmap")

        assert isinstance(cmap, ListedColormap)
        assert cmap.colors == ["red"]

    def test_add_cmap_many_colors(self):
        colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        cmap = add_cmap(colors, cmap_type="continuous", name="mycustomcmap")

        assert isinstance(cmap, LinearSegmentedColormap)
        assert cmap.name == "mycustomcmap"


if __name__ == "__main__":
    pytest.main()
