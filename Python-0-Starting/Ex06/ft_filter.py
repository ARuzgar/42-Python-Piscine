import sys


def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return [x for x in iterable if bool(x)]
    return [x for x in iterable if function(x)]


def main() -> None:
    """
    Main function to demonstrate the ft_filter implementation.
    Provides example usage of the custom filter function with different scenarios.
    """
    try:
        # Example 1: Filter with a lambda function
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        even_numbers = ft_filter(lambda x: x % 2 == 0, numbers)
        print("Even numbers:", even_numbers)

        # Example 2: Filter with None
        mixed_list = [0, 1, False, True, '', 'hello', None, 42]
        truthy_values = ft_filter(None, mixed_list)
        print("Truthy values:", truthy_values)

        # Example 3: Filter with a custom function
        def is_positive(x):
            return x > 0

        positive_numbers = ft_filter(is_positive, [-1, 0, 1, 2, -3, 4])
        print("Positive numbers:", positive_numbers)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()