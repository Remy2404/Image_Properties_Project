import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

def load_image(image_path):
    """Load an image from the given path."""
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    return img
def show_image(img, title="Image"):
    """
    Display an image using OpenCV.

    This function opens a window to display the given image using OpenCV.
    The window will remain open until any key is pressed.

    Parameters:
    img (numpy.ndarray): The image to be displayed, as a NumPy array.
    title (str, optional): The title of the window. Defaults to "Image".

    Returns:
    None

    Note:
    This function will block execution until a key is pressed to close the window.
    """
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_image(img, title="Image"):
    """Display an image using OpenCV."""
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_image_matplotlib(img):
    """Display an image using Matplotlib."""
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.axis('off')
    plt.show()

def get_image_properties(img):
    """Return image properties: shape, data type, and pixel values."""
    shape = img.shape
    dtype = img.dtype
    pixel_value = img[0, 0]  # Get pixel value at (0,0)
    return shape, dtype, pixel_value

def save_image(img, output_path):
    """Save an image to the specified path."""
    cv2.imwrite(output_path, img)
    print(f"Image saved at {output_path}")


def uiia_cat_meme():
    """
    Load 'uiia_cat.png' and continuously display it rotating from left to right like a video.
    Press 'q' to exit the rotation.
    """
    # Construct an absolute image path that adjusts for the current working directory.
    image_path = os.path.join(os.path.dirname(__file__), "..", "data", "uiia_cat.png")
    img = load_image(image_path)
    rows, cols = img.shape[:2]
    angle = 0
    while True:
        # Compute rotation matrix and rotated image
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
        rotated = cv2.warpAffine(img, M, (cols, rows))
        cv2.imshow("UIIA Cat Meme", rotated)
        # Wait 50ms; exit if 'q' is pressed
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
        angle = (angle + 2) % 360
    cv2.destroyAllWindows()
def uiia_cat_meme_video(image_path, output_path, duration=5):
    """Create a continuous rotation effect from left to right like a video.
    
    Parameters:
      image_path (str): Path to the input image.
      output_path (str): Path where the output video will be saved.
      duration (int, optional): Duration of the video in seconds. Default is 5.
    """
    # Load the image
    img = load_image(image_path)
    height, width, _ = img.shape

    # Define the number of frames and rotation angle
    fps = 30
    num_frames = fps * duration
    angle_step = 720 / num_frames  # Doubled the rotation speed

    # Create a video writer with MP4 codec
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for i in range(num_frames):
        # Calculate the rotation matrix for the current frame
        M = cv2.getRotationMatrix2D((width / 2, height / 2), angle_step * i, 1.0)

        # Apply the rotation to the image
        rotated_img = cv2.warpAffine(img, M, (width, height))

        # Write the frame to the video file
        video_writer.write(rotated_img)

    # Release the video writer and finish up
    video_writer.release()
    print(f"Rotation cycle video saved at {output_path}")


__all__ = [
    "load_image",
    "show_image",
    "show_image_matplotlib",
    "get_image_properties",
    "save_image",
    "uiia_cat_meme",
    "uiia_cat_meme_video"
]
