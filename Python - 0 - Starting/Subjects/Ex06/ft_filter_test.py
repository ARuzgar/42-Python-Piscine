import sys
import ft_filter


def test_filter_comparison():
    """
    Compare the behavior and documentation of built-in filter()
    and custom ft_filter() across various scenarios.

    Prints detailed comparison of filter results and docstrings
    to help verify functional and documentation equivalence.
    """
    def print_test_header(test_name):
        """
        Print a formatted header for each test case.

        Args:
            test_name (str): Name of the current test scenario
        """
        print(f"\n{'=' * 50}")
        print(f"TEST: {test_name}")
        print(f"{'=' * 50}")

    # Compare Docstrings
    print_test_header("DOCSTRING COMPARISON")
    builtin_filter_doc = filter.__doc__
    custom_filter_doc = ft_filter.ft_filter.__doc__

    print("Built-in filter() docstring:")
    print(builtin_filter_doc)
    print("\nCustom ft_filter() docstring:")
    print(custom_filter_doc)

    # Strict docstring comparison
    assert builtin_filter_doc == custom_filter_doc, \
        "Docstrings are not identical. They must match exactly."

    # Functional Comparisons
    print_test_header("Lambda Function Filtering")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    builtin_even = list(filter(lambda x: x % 2 == 0, numbers))
    custom_even = ft_filter.ft_filter(lambda x: x % 2 == 0, numbers)

    print("Built-in filter even numbers:", builtin_even)
    print("Custom ft_filter even numbers:", custom_even)
    assert builtin_even == custom_even, "Even number filtering failed"

    # Test Case 2: Filtering with None (remove falsy values)
    print_test_header("None Filter (Removing Falsy Values)")
    mixed_list = [0, 1, False, True, '', 'hello', None, 42]

    builtin_truthy = list(filter(None, mixed_list))
    custom_truthy = ft_filter.ft_filter(None, mixed_list)

    print("Built-in filter truthy values:", builtin_truthy)
    print("Custom ft_filter truthy values:", custom_truthy)
    assert builtin_truthy == custom_truthy, "Truthy value filtering failed"

    # Test Case 3: Custom function filtering
    print_test_header("Custom Function Filtering")
    def is_positive(x):
        return x > 0

    numbers_with_negatives = [-1, 0, 1, 2, -3, 4]

    builtin_positive = list(filter(is_positive, numbers_with_negatives))
    custom_positive = ft_filter.ft_filter(is_positive, numbers_with_negatives)

    print("Built-in filter positive numbers:", builtin_positive)
    print("Custom ft_filter positive numbers:", custom_positive)
    assert builtin_positive == custom_positive, "Positive number filtering failed"

    # Test Case 4: Empty list
    print_test_header("Empty List Filtering")
    empty_list = []

    builtin_empty = list(filter(lambda x: x > 0, empty_list))
    custom_empty = ft_filter.ft_filter(lambda x: x > 0, empty_list)

    print("Built-in filter empty list:", builtin_empty)
    print("Custom ft_filter empty list:", custom_empty)
    assert builtin_empty == custom_empty, "Empty list filtering failed"

    print("\n✅ All filter comparisons and docstring checks passed successfully!")


def main() -> None:
    """
    Main function to run filter comparison tests.

    Handles any potential exceptions during testing.
    """
    try:
        test_filter_comparison()
    except AssertionError as ae:
        print(f"Assertion failed: {ae}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()