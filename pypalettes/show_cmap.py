from typing import TYPE_CHECKING, Any

from pypalettes.load_cmap import load_cmap

if TYPE_CHECKING:
    from matplotlib.figure import Figure


def show_cmap(
    *args: Any,
    max_cols: int = 8,
    spacing: float = 0.1,
    square_size: float = 1,
) -> "Figure":
    """
    Show the colors from a colormap as a grid of colored squares.

    Displays the colormap with one square per color, left-aligned, with a
    maximum number of columns per row. Automatically adjusts layout based on
    the number of colors.

    Args:
        *args: Arguments to pass to `load_cmap` to load the desired colormap.
        max_cols (int): Maximum number of color squares per row.
        spacing (float): Spacing between squares.
        square_size (float): Size of each square.

    Returns:
        matplotlib.figure.Figure: The figure object containing the colormap visualization.
    """
    import matplotlib.pyplot as plt
    from matplotlib.axes import Axes
    from matplotlib.colors import LinearSegmentedColormap, ListedColormap
    from matplotlib.figure import Figure
    from matplotlib.patches import Rectangle

    cmap: LinearSegmentedColormap | ListedColormap = load_cmap(*args)
    colors: list = cmap.colors  # ty: ignore
    num_colors: int = len(colors)
    num_rows: int = (num_colors + max_cols - 1) // max_cols

    fig_height: int | float = max(num_rows * (square_size + spacing), 2)
    fig_width: int | float = max_cols * (square_size + spacing)

    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=150)
    ax.axis("off")

    for idx, color in enumerate(colors):
        row: int = idx // max_cols
        col: int = idx % max_cols

        x: int | float = col * (square_size + spacing)
        y: int | float = -row * (square_size + spacing)

        rect: Rectangle = plt.Rectangle(
            (x, y), square_size, square_size, color=color, clip_on=False
        )
        ax.add_patch(rect)

    ax.set_xlim(0, fig_width)
    ax.set_ylim(-num_rows * (square_size + spacing), spacing * 2)
    ax.set_aspect("equal", adjustable="box")
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    return fig
