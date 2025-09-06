"""
array2D.py

Module to handle 2D array operations,
including slicing and shape determination.
"""

from typing import List, Union
import numpy as np


def slice_me(
    family: List[List[Union[int, float]]], start: int, end: int
) -> List[List[Union[int, float]]]:
    """
    Slice a 2D array based on start and end indices
    and return the truncated array.

    This function prints the original shape of the array,
    slices it using the provided
    start and end indices, prints the new shape of the truncated array,
    and returns
    the sliced array.

    Args:
        family (List[List[Union[int, float]]]): The 2D array to be sliced.
        start (int): The starting index for slicing.
        end (int): The ending index for slicing.

    Returns:
        List[List[Union[int, float]]]: The truncated 2D array after slicing.

    Raises:
        TypeError: If 'family' is not a list of lists containing integers
        or floats,
                   or if 'start'/'end' are not integers.
        ValueError: If the inner lists in 'family' are not of the same length.
    """
    # Validate that 'family' is a list
    if not isinstance(family, list):
        raise TypeError("The 'family' parameter must be a list of lists.")

    for row in family:
        if not isinstance(row, list):
            raise TypeError("Each element in 'family' must be a list.")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    "All elements within the lists must be integers or floats."
                )

    # Validate that all inner lists have the same length
    row_lengths = [len(row) for row in family]
    if len(set(row_lengths)) != 1:
        raise ValueError(
            "All inner lists in 'family' must have the same length."
            )

    # Validate that 'start' and 'end' are integers
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("The 'start' and 'end' parameters must be integers.")

    # Convert the list of lists to a NumPy array for efficient slicing
    array = np.array(family)

    # Print the original shape of the array
    print(f"My shape is : {array.shape}")

    # Perform slicing using the provided 'start' and 'end' indices
    sliced_array = array[start:end]

    # Print the new shape of the sliced array
    print(f"My new shape is : {sliced_array.shape}")

    # Return the sliced array as a list of lists
    return sliced_array.tolist()


def main() -> None:
    """
    Main function to demonstrate the usage of the 'slice_me' function.

    This function is intended for direct execution of the script and
    will run sample
    slicing operations. It is not invoked when the module is imported.
    """
    # Sample data for demonstration purposes
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2],
    ]

    try:
        # Example slicing from index 0 to 2
        bmi = slice_me(family, 0, 2)
        print(bmi)

        # Example slicing from index 1 to -2
        bmi = slice_me(family, 1, -2)
        print(bmi)

    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
        exit(1)


if __name__ == "__main__":
    main()
