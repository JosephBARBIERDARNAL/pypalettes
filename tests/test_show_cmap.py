from matplotlib.figure import Figure

from pypalettes import show_cmap


def test_show_cmap():
    fig: Figure = show_cmap("Acadia")
    assert isinstance(fig, Figure)
