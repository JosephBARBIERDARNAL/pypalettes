import pytest
import pypalettes
from matplotlib import colormaps as cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


class TestRegisterCmap:

    def test_cmap_registered(self):
        cmap = cm.get_cmap("ClaudeMonet")
        assert isinstance(cmap, ListedColormap)
        assert cmap.name == "ClaudeMonet"
        assert cmap.colors == [
            "#184430FF",
            "#548150FF",
            "#DEB738FF",
            "#734321FF",
            "#852419FF",
        ]

    def test_cmap_gradient(self):
        cmap = cm.get_cmap("ClaudeMonet_gradient")
        assert isinstance(cmap, LinearSegmentedColormap)
        assert cmap.name == "ClaudeMonet_gradient"
        assert cmap.colors == [
            "#184430FF",
            "#548150FF",
            "#DEB738FF",
            "#734321FF",
            "#852419FF",
        ]


if __name__ == "__main__":
    pytest.main()
