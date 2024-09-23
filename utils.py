# utils.py
import io
import matplotlib.pyplot as plt
from prettymaps import plot
from layers_and_styles import get_layers

def create_pretty_map(location, circle=True, dilate=200, radius=500, style=None, preset=None):
    """
    Generate a pretty map using the prettymaps library.

    Args:
        location (str): The location to generate the map for.
        circle (bool): Whether to use a circular boundary.
        dilate (int): Dilation value for the boundary.
        radius (int): Radius for the map area.
        style (dict): Style dictionary for the map layers.

    Returns:
        tuple: Matplotlib figure and axis objects.
    """
    # Plot the map
    fig, ax = plt.subplots(figsize=(15, 15))
    plot(
        location,
        layers=get_layers(),
        style=style,
        ax=ax,
        preset=preset,
        circle=circle,
        dilate=dilate,
        radius=radius
    )
    plt.close(fig)  # Close the figure to prevent it from displaying in non-interactive environments
    return fig, ax

def save_plot(fig, file_type='png', dpi=300, size_mm=(420, 297)):
    """
    Save a Matplotlib figure to an in-memory buffer as PNG or SVG.

    Args:
        fig: Matplotlib figure object.
        file_type (str): File type, either 'png' or 'svg'.
        dpi (int): Dots per inch for PNG file.
        size_mm (tuple): Width and height in millimeters for the plot size.

    Returns:
        BytesIO: In-memory buffer containing the image data.
    """
    # Convert size from mm to inches for Matplotlib
    size_inch = tuple(s / 25.4 for s in size_mm)
    fig.set_size_inches(size_inch)

    # Create a BytesIO buffer to save the image
    buf = io.BytesIO()
    save_kwargs = {'format': file_type, 'bbox_inches': 'tight'}
    if file_type == 'png':
        save_kwargs['dpi'] = dpi
    fig.savefig(buf, **save_kwargs)
    buf.seek(0)
    return buf