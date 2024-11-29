"""
zoom.py

Script to load an image, zoom into it in grayscale, display the zoomed area, and save it automatically.
"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from load_image import ft_load


def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Convert an RGB image to grayscale.

    Args:
        image (np.ndarray): The RGB image as a NumPy array.

    Returns:
        np.ndarray: Grayscale version of the image.
    """
    if len(image.shape) == 3 and image.shape[2] == 3:  # If RGB
        grayscale = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])  # Grayscale formula
        return grayscale.astype(np.uint8)
    elif len(image.shape) == 2:  # Already grayscale
        return image
    else:
        raise ValueError("Image format not supported for grayscale conversion.")


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
        zoomed_image = image[start_y:end_y, start_x:end_x]
        print(f"New shape after slicing: {zoomed_image.shape}")
        print(zoomed_image)
        return zoomed_image
    except Exception as e:
        raise ValueError(f"An error occurred while zooming into the image: {e}")


def display_zoomed_image(image: np.ndarray) -> None:
    """
    Display the zoomed grayscale image.

    Args:
        image (np.ndarray): The zoomed grayscale image to display.
    """
    plt.imshow(image, cmap="gray")
    plt.axis("on")  # Keep axes for clarity
    plt.show()


def save_zoomed_image(image: np.ndarray, filename: str) -> None:
    """
    Save the zoomed grayscale image to a file.

    Args:
        image (np.ndarray): The zoomed grayscale image.
        filename (str): The filename to save the image as.
    """
    try:
        img = Image.fromarray(image.astype(np.uint8))
        img.save(filename)
    except Exception as e:
        print(f"Error saving the image: {e}")


def main() -> None:
    """
    Main function to load, zoom, display, and save the zoomed grayscale image.
    """
    try:
        # Load the image
        image_path = "animal.jpeg"
        image = ft_load(image_path)

        # Convert the image to grayscale
        grayscale_image = convert_to_grayscale(image)

        # Calculate zoom area based on center coordinates
        center_x, center_y = 650, 300
        zoom_width, zoom_height = 400, 400

        # Calculate slicing coordinates
        start_x = max(0, center_x - zoom_width // 2)
        end_x = min(grayscale_image.shape[1], center_x + zoom_width // 2)
        start_y = max(0, center_y - zoom_height // 2)
        end_y = min(grayscale_image.shape[0], center_y + zoom_height // 2)

        # Apply zoom
        zoomed_image = zoom_image(grayscale_image, start_x, end_x, start_y, end_y)

        # Save the zoomed grayscale image
        save_zoomed_image(zoomed_image, "zoomed_animal.jpeg")

        # Display only the zoomed grayscale image
        display_zoomed_image(zoomed_image)
    except (FileNotFoundError, ValueError, Exception) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()