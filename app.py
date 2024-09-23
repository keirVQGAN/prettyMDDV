import streamlit as st
import io
from utils import create_pretty_map, save_plot
from layers_and_styles import get_layers, get_default_colors, get_styles

# Set up Streamlit interface
st.title("Custom Map Generator")

# Switches to control the display of UI elements
SHOW_LAYER_STYLE_OPTIONS = True
SHOW_DILATE_OPTION = False
SHOW_CIRCLE_OPTION = False
SHOW_COLOR_SCHEME_OPTION = False

# Initialize session state with default values
DEFAULTS = {
    'location': "Bristol, UK",
    'circle': True,
    'radius': 1000,
    'dilate': 200,
    'color_scheme': 'Greyscale',
    'active_ec': {},
    'active_lw': {}
}

for key, value in DEFAULTS.items():
    st.session_state.setdefault(key, value)

# Location and Radius input
cols = st.columns([2, 1, 1]) if SHOW_COLOR_SCHEME_OPTION else st.columns([2, 1])

with cols[0]:
    location = st.text_input("Location", st.session_state['location'])
with cols[1]:
    radius = st.slider("Radius", 100, 5000, st.session_state['radius'], 100)

# Color Scheme selection
if SHOW_COLOR_SCHEME_OPTION:
    with cols[2]:
        color_scheme = st.selectbox("Color Scheme", ['Greyscale', 'Colour'], index=0)
else:
    color_scheme = st.session_state['color_scheme']

# Circle and Dilate options
circle = st.session_state['circle']
dilate = st.session_state['dilate']

if SHOW_CIRCLE_OPTION or SHOW_DILATE_OPTION:
    options_cols = st.columns(2)
    if SHOW_CIRCLE_OPTION:
        with options_cols[0]:
            circle = st.checkbox("Circle", value=circle)
    if SHOW_DILATE_OPTION:
        with options_cols[1]:
            dilate = st.slider("Dilate", 0, 500, dilate, 50)

# Get default colors based on color scheme
default_colors = get_default_colors(color_scheme)
default_line_width = 0.3

# Get layers and styles
layers = get_layers()
active_ec = {layer: default_colors[layer] for layer in layers}
active_lw = {layer: default_line_width for layer in layers if layer != 'highway'}  # Exclude 'highway' layer
style = get_styles(ec=active_ec, lw=active_lw)

# Generate Map
if st.button("Generate Map"):
    st.session_state.update({
        'location': location,
        'circle': circle,
        'radius': radius,
        'dilate': dilate,
        'color_scheme': color_scheme,
        'active_ec': active_ec,
        'active_lw': active_lw
    })

    fig, ax = create_pretty_map(
        location=location,
        radius=radius,
        circle=circle,
        dilate=dilate,
        style=style
    )

    # Convert figure to PNG
    png_buffer = io.BytesIO()
    fig.savefig(png_buffer, format='png', bbox_inches='tight')
    png_buffer.seek(0)
    st.session_state['fig'] = fig
    st.session_state['png_buffer'] = png_buffer

# Display Map and Download Options
if 'png_buffer' in st.session_state:
    st.image(st.session_state['png_buffer'])

    col1, col2 = st.columns(2)
    with col1:
        svg_buffer = save_plot(
            st.session_state['fig'],
            file_type='svg',
            size_mm=(420, 297)
        )
        st.download_button(
            label="Download SVG",
            data=svg_buffer,
            file_name="map_output.svg",
            mime="image/svg+xml"
        )
    with col2:
        png_buffer_download = save_plot(
            st.session_state['fig'],
            file_type='png',
            dpi=300,
            size_mm=(420, 297)
        )
        st.download_button(
            label="Download PNG",
            data=png_buffer_download,
            file_name="map_output.png",
            mime="image/png"
        )
