# tester.py

from array2D import slice_me

def main():
    """Test the slice_me function with sample data."""
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2],
    ]

    try:
        # First test case
        bmi = slice_me(family, 0, 2)
        print(bmi)

        # Second test case
        bmi = slice_me(family, 1, -2)
        print(bmi)

    except (TypeError, ValueError) as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()