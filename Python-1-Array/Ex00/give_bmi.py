"""
give_bmi.py

Module to calculate BMI values and apply a limit to determine if they are above the threshold.
"""

from typing import List, Union
import numpy as np


def give_bmi(height: List[Union[int, float]], weight: List[Union[int, float]]) -> List[float]:
    """
    Calculate BMI values from lists of heights and weights.

    Args:
        height (List[Union[int, float]]): List of heights in meters.
        weight (List[Union[int, float]]): List of weights in kilograms.

    Returns:
        List[float]: List of BMI values.

    Raises:
        TypeError: If inputs are not lists or contain non-numeric values.
        ValueError: If input lists are of different lengths or contain non-positive values.
    """
    # Validate input types
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Both height and weight must be lists.")

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")

    # Convert lists to NumPy arrays for efficient computation
    try:
        height_array = np.array(height, dtype=float)
        weight_array = np.array(weight, dtype=float)
    except ValueError:
        raise TypeError("All elements in height and weight lists must be integers or floats.")

    # Check for non-positive values
    if np.any(height_array <= 0) or np.any(weight_array <= 0):
        raise ValueError("All height and weight values must be positive numbers.")

    # Calculate BMI: weight / (height^2)
    bmi_array = weight_array / (height_array ** 2)

    return bmi_array.tolist()


def apply_limit(bmi: List[Union[int, float]], limit: Union[int, float]) -> List[bool]:
    """
    Determine if each BMI value is above the specified limit.

    Args:
        bmi (List[Union[int, float]]): List of BMI values.
        limit (Union[int, float]): BMI threshold.

    Returns:
        List[bool]: List indicating whether each BMI is above the limit.

    Raises:
        TypeError: If bmi is not a list or contains non-numeric values, or if limit is not numeric.
    """
    # Validate input types
    if not isinstance(bmi, list):
        raise TypeError("BMI must be a list.")

    if not isinstance(limit, (int, float)):
        raise TypeError("Limit must be an integer or float.")

    # Convert bmi list to NumPy array for efficient computation
    try:
        bmi_array = np.array(bmi, dtype=float)
    except ValueError:
        raise TypeError("All elements in BMI list must be integers or floats.")

    # Determine if each BMI value is above the limit
    above_limit = bmi_array > limit

    return above_limit.tolist()


def main() -> None:
    """
    Main function to demonstrate the usage of give_bmi and apply_limit functions.

    This function is intended for testing purposes and will execute when the script is run directly.
    """
    try:
        # Sample data
        height = [2.71, 1.15]
        weight = [165.3, 38.4]

        # Calculate BMI
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))

        # Apply limit
        limit = 26
        bmi_above_limit = apply_limit(bmi, limit)
        print(bmi_above_limit)

    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
        exit(1)


if __name__ == "__main__":
    main()
