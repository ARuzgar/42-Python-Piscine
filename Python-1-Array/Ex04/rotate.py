"""
rotate.py

Script to load an image, adjust its size to 400x400 if necessary, convert it to grayscale, manually transpose it, and display the result.
"""

import matplotlib.pyplot as plt
import numpy as np
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
        raise ValueError("Unsupported image format for grayscale conversion.")


def crop_to_400x400(image: np.ndarray, center_x: int, center_y: int) -> np.ndarray:
    """
    Crop the image to 400x400 pixels based on given center coordinates. If the image
    is already 400x400, return it as is.

    Args:
        image (np.ndarray): The input image.
        center_x (int): X-coordinate of the center for cropping.
        center_y (int): Y-coordinate of the center for cropping.

    Returns:
        np.ndarray: A 400x400 cropped image.
    """
    if image.shape[0] == 400 and image.shape[1] == 400:
        return image

    # Calculate cropping boundaries
    square_size = 400
    start_x = max(0, center_x - square_size // 2)
    end_x = min(image.shape[1], center_x + square_size // 2)
    start_y = max(0, center_y - square_size // 2)
    end_y = min(image.shape[0], center_y + square_size // 2)

    # Adjust the slice if the cropped region is smaller than 400x400 (edge case)
    if end_x - start_x < 400:
        start_x = max(0, end_x - 400)
        end_x = start_x + 400
    if end_y - start_y < 400:
        start_y = max(0, end_y - 400)
        end_y = start_y + 400

    # Crop the image
    cropped_image = image[start_y:end_y, start_x:end_x]

    # Ensure the cropped image is exactly 400x400
    assert cropped_image.shape == (400, 400), f"Unexpected cropped shape: {cropped_image.shape}"
    return cropped_image


def transpose_image(image: np.ndarray) -> np.ndarray:
    """
    Manually transpose a 2D array (swap rows and columns).

    Args:
        image (np.ndarray): The grayscale image array to transpose.

    Returns:
        np.ndarray: The transposed image array.
    """
    rows, cols = image.shape
    transposed = np.zeros((cols, rows), dtype=image.dtype)
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = image[i][j]
    return transposed


def display_image(image: np.ndarray) -> None:
    """
    Display an image using matplotlib.

    Args:
        image (np.ndarray): The image to display.
    """
    plt.imshow(image, cmap="gray")
    plt.axis("on")  # Keep axes visible
    plt.show()


def main() -> None:
    """
    Main function to load, adjust, transpose, and display an image in grayscale.
    """
    try:
        # Load the image
        image_path = "animal.jpeg"
        image = ft_load(image_path)

        # Convert the image to grayscale
        grayscale_image = convert_to_grayscale(image)

        # Crop or adjust to 400x400 based on target coordinates
        center_x, center_y = 650, 300
        adjusted_image = crop_to_400x400(grayscale_image, center_x, center_y)

        # Perform the transpose manually
        transposed_image = transpose_image(adjusted_image)

        # Print the new shape and data
        print(f"New shape after Transpose: {transposed_image.shape}")
        print(transposed_image)

        # Display the transposed image
        display_image(transposed_image)
    except (FileNotFoundError, ValueError, Exception) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()