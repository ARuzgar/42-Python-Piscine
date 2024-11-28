"""
load_image.py

Module to load an image, print its format and RGB pixel content.
Handles JPG and JPEG formats with comprehensive error handling.
"""

from typing import Union, List
import os
import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load an image, print its format and RGB pixel content.

    Args:
        path (str): Path to the image file.

    Returns:
        np.ndarray: Array of image pixels in RGB format.

    Raises:
        TypeError: If 'path' is not a string.
        FileNotFoundError: If the image file does not exist.
        ValueError: If the image format is not JPG or JPEG, or if an error occurs during loading.
    """
    # Validate that 'path' is a string
    if not isinstance(path, str):
        raise TypeError("The 'path' parameter must be a string.")

    # Check if the file exists
    if not os.path.isfile(path):
        raise FileNotFoundError(f"The file '{path}' does not exist.")

    # Check if the file has a valid image extension
    if not path.lower().endswith(('.jpg', '.jpeg')):
        raise ValueError("Unsupported file format. Only JPG and JPEG are supported.")

    try:
        # Open the image using Pillow
        with Image.open(path) as img:
            # Print the image format
            print(f"Image format: {img.format}")

            # Convert the image to RGB (in case it's in a different mode)
            img = img.convert('RGB')

            # Convert the image to a NumPy array
            img_array = np.array(img)

            # Print the shape of the image
            print(f"The shape of image is: {img_array.shape}")

            # Print the pixel content
            print(img_array)

            return img_array

    except Exception as e:
        raise ValueError(f"An error occurred while loading the image: {e}")


def main() -> None:
    """
    Main function to demonstrate the usage of ft_load.

    This function is intended for direct execution of the script.
    """
    try:
        # Example usage
        image_path = "landscape.jpg"
        ft_load(image_path)
    except (TypeError, FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
        exit(1)


if __name__ == "__main__":
    main()