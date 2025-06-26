from pypalettes import show_cmap
import matplotlib as mpl


def test_show_cmap():
    fig = show_cmap("Acadia")
    assert isinstance(fig, mpl.figure.Figure)
