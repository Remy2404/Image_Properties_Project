import os
import sys
sys.path.append(os.path.abspath('..'))
from src.image_utils import uiia_cat_meme_video

if __name__ == "__main__":
    # Determine the project root (one level up)
    project_root = os.path.abspath('..')
    
    # Build the image path and output path
    image_path = os.path.join(project_root, "data", "uiia_cat.png")
    results_folder = os.path.join(project_root, "results")
    os.makedirs(results_folder, exist_ok=True)
    output_path = os.path.join(results_folder, "uiia_cat_meme.mp4")
    
    # Create the video with a 5-second duration
    uiia_cat_meme_video(image_path, output_path, duration=10)
