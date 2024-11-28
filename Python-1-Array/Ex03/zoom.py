"""
zoom.py

Script to load an image, zoom into it, and display it with information.
"""

import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def zoom_image(image: np.ndarray, start_x: int, end_x: int, start_y: int, end_y: int) -> np.ndarray:
    """
    Zoom into a specific area of the image by slicing it.

    Args:
        image (np.ndarray): The original image as a NumPy array.
        start_x (int): Start index on the X-axis for zooming.
        end_x (int): End index on the X-axis for zooming.
        start_y (int): Start index on the Y-axis for zooming.
        end_y (int): End index on the Y-axis for zooming.

    Returns:
        np.ndarray: The zoomed portion of the image.

    Raises:
        ValueError: If the slicing indices are invalid.
    """
    try:
        # Slice the image
        zoomed_image = image[start_y:end_y, start_x:end_x]

        # Print new shape after slicing
        print(f"New shape after slicing: {zoomed_image.shape}")
        print(zoomed_image)

        return zoomed_image
    except Exception as e:
        raise ValueError(f"An error occurred while zooming into the image: {e}")


def display_image(image: np.ndarray, title: str = "Image") -> None:
    """
    Display the image with scales on the X and Y axes.

    Args:
        image (np.ndarray): The image to display.
        title (str): The title of the displayed image.
    """
    plt.imshow(image, cmap='gray' if image.ndim == 2 else None)
    plt.title(title)
    plt.colorbar()
    plt.show()


def main() -> None:
    """
    Main function to load, zoom, and display the image.
    """
    try:
        # Load the image
        image_path = "animal.jpeg"  # Replace with the path to your image
        image = ft_load(image_path)

        # Calculate zoom area based on center coordinates
        center_x, center_y = 650, 300
        zoom_width, zoom_height = 400, 400

        # Calculate slicing coordinates
        start_x = max(0, center_x - zoom_width // 2)
        end_x = min(image.shape[1], center_x + zoom_width // 2)
        start_y = max(0, center_y - zoom_height // 2)
        end_y = min(image.shape[0], center_y + zoom_height // 2)

        # Apply zoom
        zoomed_image = zoom_image(image, start_x, end_x, start_y, end_y)

        # Display the original and zoomed images
        display_image(image, title="Original Image")
        display_image(zoomed_image, title="Zoomed Image")
    except (FileNotFoundError, ValueError, Exception) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()