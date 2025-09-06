"""tester.py

Demonstration script for Exercise 05 (Pimp my image).
Loads the image and applies all five filters, displaying them in a 2x3 grid.
"""
from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
from pimp_image import (
    ft_invert,
    ft_red,
    ft_green,
    ft_blue,
    ft_grey,
)


def show_results(original: np.ndarray) -> None:
    """Render original + filtered versions in a matplotlib figure."""
    fig, axes = plt.subplots(3, 2, figsize=(10, 12))
    fig.suptitle("Exercise 05 - Pimp my image", fontsize=14)
    axes = axes.ravel()

    # Original
    axes[0].imshow(original)
    axes[0].set_title("Figure V.1: Original")
    axes[0].axis("off")

    # Invert
    inv = ft_invert(original)
    axes[1].imshow(inv)
    axes[1].set_title("Figure V.2: Invert")
    axes[1].axis("off")

    # Red
    red = ft_red(original)
    axes[2].imshow(red)
    axes[2].set_title("Figure V.3: Red")
    axes[2].axis("off")

    # Green
    green = ft_green(original)
    axes[3].imshow(green)
    axes[3].set_title("Figure V.4: Green")
    axes[3].axis("off")

    # Blue
    blue = ft_blue(original)
    axes[4].imshow(blue)
    axes[4].set_title("Figure V.5: Blue")
    axes[4].axis("off")

    # Grey
    grey = ft_grey(original)
    axes[5].imshow(grey)
    axes[5].set_title("Figure V.6: Grey")
    axes[5].axis("off")

    plt.tight_layout()
    plt.show()


def main() -> None:
    try:
        array = ft_load("landscape.jpg")
        show_results(array)
        # Example of docstring access
        print(ft_invert.__doc__.splitlines()[0])
    except Exception as err:  # noqa: BLE001
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
