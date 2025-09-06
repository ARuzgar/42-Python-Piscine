# tester.py

from give_bmi import give_bmi, apply_limit


def main():
    """Test the give_bmi and apply_limit functions."""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    try:
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))

        bmi_limit = apply_limit(bmi, 26)
        print(bmi_limit)

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
