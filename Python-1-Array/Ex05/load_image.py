"""load_image.py

Image loading utility for Exercise 05.
Provides a single function `ft_load` that loads a JPG/JPEG image,
converts it to
an RGB NumPy array, prints its shape and contents (as per previous exercises),
and returns the array.
"""
from __future__ import annotations
import os
import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load a JPG/JPEG image and return it as a NumPy RGB array.

    Behavior:
        * Validates path type & existence.
        * Ensures extension is .jpg/.jpeg.
        * Converts image to RGB.
        * Prints the shape and raw pixel content (like earlier modules).

    Args:
        path: Path to the image file.

    Returns:
        A NumPy ndarray with shape (H, W, 3) and dtype uint8.

    Raises:
        TypeError: If path is not a string.
        FileNotFoundError: If the file does not exist.
        ValueError: If the format is unsupported or loading fails.
    """
    if not isinstance(path, str):
        raise TypeError("The 'path' parameter must be a string.")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"The file '{path}' does not exist.")
    if not path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError(
            "Unsupported file format. Only JPG and JPEG are supported."
            )

    try:
        with Image.open(path) as img:
            img = img.convert("RGB")
            arr = np.array(img)
            print(f"The shape of image is: {arr.shape}")
            print(arr)
            return arr
    except Exception as exc:  # noqa: BLE001
        raise ValueError(
            f"An error occurred while loading the image: {exc}"
            ) from exc


def main() -> None:  # pragma: no cover - manual usage
    try:
        ft_load("landscape.jpg")
    except Exception as err:  # noqa: BLE001
        print(f"Error: {err}")


if __name__ == "__main__":  # pragma: no cover
    main()
