import sys
from ft_filter import ft_filter


def validate_arguments(args):
    """
    Validate the input arguments for the filterstring program.

    Args:
        args (list): Command-line arguments to validate.

    Raises:
        AssertionError: If the number or type of arguments is incorrect.
    """
    # Check number of arguments
    if len(args) != 3:
        raise AssertionError("Assertion Error : the arguments are bad")

    # Check if second argument can be converted to an integer
    try:
        int(args[2])
    except ValueError:
        raise AssertionError("Assertion Error : the arguments are bad")

    # Check if first argument is a string and second is an integer
    if not (isinstance(args[1], str) and isinstance(int(args[2]), int)):
        raise AssertionError("Assertion Error : the arguments are bad")


def filter_words(sentence: str, length: int) -> list:
    """
    Filter words from a sentence that are longer than a specified length.

    Args:
        sentence (str): Input sentence to filter words from.
        length (int): Minimum length of words to keep.

    Returns:
        list: List of words longer than the specified length.
    """
    words = sentence.split()
    return list(ft_filter(lambda word: len(word) > length, words))


def main():
    """
    Main function to handle command-line arguments and filter words.
    Validates arguments, filters words, and prints the result.
    """
    try:
        validate_arguments(sys.argv)
        sentence = sys.argv[1]
        length = int(sys.argv[2])
        result = filter_words(sentence, length)
        print(result)
    except AssertionError as ae:
        print(ae)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()