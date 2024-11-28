"""
Module to implement a custom tqdm-like progress bar using the yield operator.
"""

import sys
import time
from typing import Generator


def ft_tqdm(lst: range) -> Generator[int, None, None]:
    """
    Custom implementation of tqdm using a generator and the yield operator.

    Args:
        lst (range): The iterable to iterate over.

    Yields:
        int: The next element in the iterable.

    Side Effects:
        Prints a progress bar to the console similar to tqdm.
    """
    total = len(lst)
    start_time = time.time()
    bar_length = 50  # Length of the progress bar

    for i, elem in enumerate(lst, start=1):
        yield elem

        # Calculate elapsed time
        elapsed = time.time() - start_time

        # Calculate iterations per second
        it_per_sec = i / elapsed if elapsed > 0 else 0

        # Estimate remaining time
        remaining = (total - i) / it_per_sec if it_per_sec > 0 else 0

        # Calculate percentage of completion
        percentage = (i / total) * 100

        # Calculate the number of filled blocks in the bar
        filled_length = int(bar_length * i // total)

        # Create the bar string using '█' for filled and ' ' for unfilled
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)

        # Format elapsed and remaining time as mm:ss
        elapsed_str = time.strftime("%M:%S", time.gmtime(elapsed))
        remaining_str = time.strftime("%M:%S", time.gmtime(remaining))

        # Format the progress bar string
        progress_bar = (
            f"{int(percentage)}%|{bar}| {i}/{total} "
            f"[{elapsed_str}<{remaining_str}, {it_per_sec:.2f}it/s]"
        )

        # Print the progress bar
        sys.stdout.write('\r' + progress_bar)
        sys.stdout.flush()

    # Move to the next line after completion
    sys.stdout.write('\n')


def main() -> None:
    """
    Main function to demonstrate the usage of ft_tqdm.

    This function is intended for testing purposes and will not execute
    when the module is imported.
    """
    sample_range = range(333)
    for _ in ft_tqdm(sample_range):
        time.sleep(0.005)  # Simulate work being done


if __name__ == "__main__":
    main()
