# Image Properties Project

This project demonstrates image processing utilities including loading images, displaying them, and creating animated effects (e.g., rotation cycles) using OpenCV and Matplotlib.

## Prerequisites

- Python 3.7+
- pip (Python package installer)
- Virtual environment (recommended)

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/remy2404/Image_Properties_Project.git
   cd Image_Properties_Project
   ```

2. **Create a Virtual Environment**

   On Windows, run:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   On macOS/Linux, run:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Required Packages**

   Install the dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

   If a 

requirements.txt

 file is not provided, you may need to install the following packages manually:

   ```bash
   pip install opencv-python numpy matplotlib
   ```

## Usage

### Running the Notebook

1. Ensure your virtual environment is activated.
2. From the project root, add the project to the Python path when starting Jupyter Notebook:

   ```bash
   set PYTHONPATH=%PYTHONPATH%;%CD%
   jupyter notebook
   ```

3. Open 

image_properties.ipynb

 and run the cells.

### Running Scripts

You can also run the provided functions directly from Python scripts. For example, to view the rotating UIIA cat meme:

```python
from src.image_utils import uiia_cat_meme

uiia_cat_meme()
```

Or to create a video with the rotation effect:

```python
import os
from src.image_utils import uiia_cat_meme_video

image_path = os.path.join("data", "uiia_cat.png")
output_path = os.path.join("results", "uiia_cat_meme.mp4")
uiia_cat_meme_video(image_path, output_path)
```

## Project Structure

```
Image_Properties_Project/
├── data/                  # Contains input images (e.g., uiia_cat.png)
├── results/               # Output files like processed images and videos
├── notebooks/             # Jupyter Notebooks
├── src/                   # Python source code (image_utils.py, etc.)
├── README.md
└── requirements.txt       # Project dependencies
```

## License

Include licensing information here if applicable.

## Contact

For any questions or contributions, please contact [rosexmee1122@gmail.com](mailto:rosexmee1122@gmail.com).
