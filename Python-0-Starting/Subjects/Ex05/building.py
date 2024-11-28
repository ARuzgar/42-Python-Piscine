"""
A Python script that counts the number of uppercase letters, lowercase letters, punctuation marks, spaces, and digits in a given text.

Usage:
    python building.py [text]

Arguments:
    text (str, optional): The text to analyze. If not provided, the user will be prompted to enter the text.

Raises:
    AssertionError: If more than one argument is provided.
"""

import sys

def count_characters(text):
    """
    Count the number of uppercase letters, lowercase letters, punctuation marks, spaces, and digits in the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        None. The results are printed to the console.
    """
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    punct_count = sum(1 for char in text if char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    digit_count = sum(1 for char in text if char.isdigit())
    space_count = sum(1 for char in text if char.isspace())
    total_count = len(text)

    print(f"The text contains {total_count} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punct_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")

def main():
    """
    The main entry point of the script.

    Checks if the script was called with more than one argument, and raises an AssertionError if that's the case.
    If no argument was provided, it prompts the user to enter the text to be analyzed.
    If an argument was provided, it uses that as the input text.
    Finally, it calls the count_characters function with the input text.
    """
    assert len(sys.argv) <= 2, "AssertionError"

    if len(sys.argv) == 1:
        text = input("What is the text to count?\n") + "\r"
    elif len(sys.argv) >= 2:
        raise AssertionError("Too many arguments")
    else:
        text = sys.argv[1]

    count_characters(text)

if __name__ == "__main__":
    main()