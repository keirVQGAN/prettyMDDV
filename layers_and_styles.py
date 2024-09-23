# layers_and_styles.py

def get_layers():
    """
    Define all possible layers for the map.

    Returns:
        dict: Dictionary of layers with their respective OSM tags.
    """
    return {
        'perimeter': {},
        'streets': {

            'width': {
                'motorway': 4,
                'trunk': 4,
                'primary': 3.5,
                'secondary': 3,
                'tertiary': 2,
                'residential': 2,
                'unclassified': 1,
                'service': 0.8,
                'pedestrian': 0.5,
                'path': 0.5,
                'footway': 0.4,
                'cycleway': 0.4
            }
        },
        'buildings': {'tags': {'building': True}},
        'landuses': {'tags': {'landuse': True}},
        'naturals': {'tags': {'natural': True, 'leisure': 'nature_reserve'}},
        # 'naturals': {'tags': {'natural': ['wood', 'scrub', 'heath', 'grass', 'grassland', 'beach', 'coastline'], 'leisure': "nature_reserve"}},        
        'boundarys': {'tags': {'boundary': True}},
        'railways': {'tags': {'railway': True}},
        # 'power': {'tags': {'power': True}},
        'waters': {'tags': {'natural': ['water', 'sea', 'river', 'canal', 'pond', 'spring', 'stream','lake']},},
        'green_spaces': {'tags': {'leisure': True, 'landuse': 'grass', 'natural': True}}
        # 'man_made': {'tags': {'man_made': True}},
        # 'tourism': {'tags': {'tourism': True}},
        # 'public_transport': {'tags': {'public_transport': True}},
        # 'place': {'tags': {'place': True}},
        # 'amenity': {'tags': {'amenity': True}},
    }

def get_default_colors(color_scheme):
    """
    Get the default colors for each layer based on the color scheme.

    Args:
        color_scheme (str): 'Greyscale' or 'Colour'.

    Returns:
        dict: Dictionary of colors for each layer.
    """
    greyscale = {
        'perimeter': '#ffffff',
        'streets': '#969595',
        'buildings': '#7F7F7F',
        'amenity': '#BFBFBF',
        'landuses': '#A9A9A9',
        'naturals': '#D3D3D3',
        'boundarys': '#b5b5b5',
        'railways': '#666666',
        'man_made': '#A0A0A0',
        'tourism': '#C0C0C0',
        'power': '#696969',
        'public_transport': '#999999',
        'place': '#4F4F4F',
        # 'waters': '#8c8c8c', #mid-grey
        'waters': '#dfe7ed', #light blue        
        # 'green_spaces': '#474747' # dark grey
        'green_spaces': '#d3ebdc' # light green        
    }
    colour = {
        'perimeter': '#2C3E50',
        'streets': '#E67E22',
        'building': '#95A5A6',
        'amenity': '#F1C40F',
        'landuse': '#27AE60',
        'natural': '#229954',
        'boundary': '#3498DB',
        'railways': '#9B59B6',
        'man_made': '#E74C3C',
        'tourism': '#F39C12',
        'power': '#C0392B',
        'public_transport': '#16A085',
        'place': '#D35400',
        'water': '#2980B9',
        'green_space': '#1ABC9C'
    }
    return greyscale if color_scheme == 'Greyscale' else colour

def get_styles(ec, lw):
    """
    Generate styles for each layer.

    Args:
        ec (dict): Edge colors for each layer.
        lw (dict): Line widths for each layer.

    Returns:
        dict: Style dictionary compatible with prettymaps.
    """
    style = {'background': {'ec': '#F2F4CB', 'lw': 0, 'fill': None}}
    for layer in ec.keys():
        # Do not set 'lw' for 'highway' layer
        if layer == 'streets':
            style[layer] = {
                'ec': ec[layer],
                'fc': ec[layer],
                'fill': ec[layer],
                'lw': 0.2,
                'zorder': 2

            }

        elif layer == 'waters':
            style[layer] = {
                'ec': ec[layer],
                'fc': ec[layer],
                # 'fill': None,
                'lw': 0.2,
                'hatch': '......',
                'zorder': -1
            }

        elif layer == 'green_spaces':
            style[layer] = {
                'ec': ec[layer],
                'fc': ec[layer],
                # 'fill': None,
                'lw': 0.4,
                'hatch': '/////////',
                'zorder': -2
            }

        elif layer == 'railways':
            style[layer] = {
                'ec': ec[layer],
                # 'fc': ec[layer],
                'fill': None,
                'lw': 0.3,
                'zorder': -3
             }            

        else:
            style[layer] = {
                'ec': ec[layer],
                'lw': lw.get(layer, 0.3),
                'fill': None
            }
    return style
