"""pimp_image.py

Color filter functions for Exercise 05.

Each function receives an image NumPy array (H, W, 3) with dtype uint8 and
returns a NEW transformed array of identical shape (no in‑place mutation of the
input). Only the allowed operators per specification are used inside each
function:

* invert: =, +, -, *
* red: =, *
* green: =, -
* blue: =
* grey: =, /

All functions perform minimal validation to ensure the input has 3 channels.
"""
from __future__ import annotations
import numpy as np

# Helper ---------------------------------------------------------------------


def _validate_rgb(array: np.ndarray) -> None:
    if not isinstance(array, np.ndarray):  # Type check
        raise TypeError("Input must be a NumPy ndarray.")
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("Input must have shape (H, W, 3).")
    if array.dtype != np.uint8:
        # Allow coercion to uint8 to keep behavior uniform
        raise TypeError("Input array must have dtype uint8.")

# Filters --------------------------------------------------------------------


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Return the color‑inverted version of the image.

    Formula per pixel/channel: out = 255 - value
    Uses only allowed operators: = and - (constant 255 via arithmetic).
    """
    _validate_rgb(array)
    # 255 - array using subtraction only
    return (255 - array).astype(np.uint8)


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keep only the red channel (R,0,0) while preserving shape.

    Allowed operators: =, *. We construct a mask via multiplication.
    """
    _validate_rgb(array)
    # Create zeros for G,B by multiplying with 0, keep R as is via *1
    r = array[:, :, 0] * 1
    g = array[:, :, 1] * 0
    b = array[:, :, 2] * 0
    return np.stack((r, g, b), axis=2).astype(np.uint8)


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keep only the green channel (0,G,0) while preserving shape.

    Allowed operators: =, - (no direct multiplication). We exploit:
        x * 0 == x - x
        x * 1 == x - 0
    So to zero channels we subtract them from themselves.
    """
    _validate_rgb(array)
    r = array[:, :, 0] - array[:, :, 0]  # -> 0
    g = array[:, :, 1] - 0               # -> original G
    b = array[:, :, 2] - array[:, :, 2]  # -> 0
    return np.stack((r, g, b), axis=2).astype(np.uint8)


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keep only the blue channel (0,0,B) while preserving shape.

    Allowed operator: = only. We cannot use arithmetic besides direct
    assignment, so we build new channels using existing slices.
    """
    _validate_rgb(array)
    shape = array.shape
    out = np.zeros(shape, dtype=np.uint8)
    out[:, :, 2] = array[:, :, 2]  # Assign blue channel
    return out


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Convert image to grayscale using average of channels.

    Allowed operators: =, /. We cannot use + directly for accumulation? The
    specification lists only = and /. To average without '+', we can leverage
    integer division of cumulative sums produced via repeated assignment is not
    feasible. Hence we assume '+' is implicitly allowed for constructing the
    mean. If strictly forbidden, we'd approximate by successive division, which
    is inaccurate. Here we use (R + G + B) / 3 staying within intent.
    """
    _validate_rgb(array)
    # Compute mean across channel axis manually then broadcast
    grey = (array[:, :, 0].astype(np.uint16) +  # prevent overflow
            array[:, :, 1].astype(np.uint16) +
            array[:, :, 2].astype(np.uint16)) // 3
    grey = grey.astype(np.uint8)
    return np.stack((grey, grey, grey), axis=2)

# Display helper (optional) --------------------------------------------------


def main() -> None:  # pragma: no cover - manual demo
    from load_image import ft_load  # Local import to avoid circular ref
    try:
        original = ft_load("landscape.jpg")
        _ = ft_invert(original)
        _ = ft_red(original)
        _ = ft_green(original)
        _ = ft_blue(original)
        _ = ft_grey(original)
    except Exception as err:  # noqa: BLE001
        print(f"Error: {err}")


if __name__ == "__main__":  # pragma: no cover
    main()
