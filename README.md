
# Custom Map Generator using Streamlit and Prettymaps

This project is a custom web-based map generator built using [Streamlit](https://streamlit.io/) and [Prettymaps](https://github.com/marceloprates/prettymaps). The app allows users to create highly customizable maps by selecting various options such as location, radius, and color schemes. Users can then download the maps in either PNG or SVG format.

## Features
- **Custom Location Input**: Users can input any location and generate a map centered around that area.
- **Adjustable Radius**: The map radius can be adjusted to show a larger or smaller area.
- **Circle and Dilate Options**: Control the appearance of circular boundaries and dilation effects on the map.
- **Greyscale and Color Mode**: Users can choose between a greyscale or colored map theme.
- **Custom Layers**: Maps are built with customizable layers like streets, buildings, green spaces, and more.
- **Download Options**: Save maps as PNG or SVG files.
- **Curved Title**: The location and radius of the map are displayed as a title following the circular boundary of the map.

## Preview
A live demo or preview of the app is available [here](#).

## Installation

To run this project locally, follow these steps:

### Prerequisites
Ensure that you have Python 3.7 or higher installed.

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/custom-map-generator.git
cd custom-map-generator
```

### Step 2: Install Dependencies
All the required dependencies are listed in the `requirements.txt` file. You can install them using `pip`:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
Run the Streamlit app locally by executing the following command:

```bash
streamlit run app.py
```

The app will start and be available at `http://localhost:8501` by default.

## Usage

Once the app is running:
1. Enter a location in the text input field (default: Bristol, UK).
2. Adjust the map radius using the slider.
3. Select a color scheme (Greyscale or Colour).
4. Click the "Generate Map" button to create the map.
5. Once the map is generated, you can download it as either a PNG or SVG file.

### Customization Options:
- **Location**: Input any valid location (e.g., "London, UK", "New York, USA").
- **Radius**: Adjust the radius between 100 and 5000 meters.
- **Color Scheme**: Choose between Greyscale or Colour themes.
- **Download Formats**: Available formats are PNG and SVG.

## Project Structure

```bash
.
├── app.py                     # The main Streamlit app script
├── utils.py                   # Utility functions for map generation and file handling
├── layers_and_styles.py        # Contains layers and styling configurations
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation (this file)
```

## Dependencies

This project uses the following main libraries:
- **[Streamlit](https://streamlit.io/)**: For building the web app interface.
- **[Matplotlib](https://matplotlib.org/)**: For generating and customizing map visuals.
- **[Prettymaps](https://github.com/marceloprates/prettymaps)**: For generating beautiful maps.
- **[Pillow](https://python-pillow.org/)**: For handling images and saving files.
- **[Shapely](https://shapely.readthedocs.io/)**, **[Geopandas](https://geopandas.org/)**, **[Pyproj](https://pyproj4.github.io/)**, **[Rtree](https://toblerity.org/rtree/)**: For handling geospatial data.

## Contributing

Contributions are welcome! Here's how you can help:
- Report issues
- Suggest new features
- Submit pull requests to improve the project

### To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-new-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/my-new-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Acknowledgements
- Thanks to [marceloprates](https://github.com/marceloprates) for creating the Prettymaps library that serves as the backbone for this map generation project.
