"""
Program to convert a string to Morse code.
"""

import sys


def convert_to_morse(input_str: str) -> str:
    """
    Convert an input string to Morse code.

    Args:
        input_str (str): The string to be converted.

    Returns:
        str: The Morse code representation of the input string.

    Raises:
        AssertionError: If the input string contains invalid characters.
    """
    morse_code_dict = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }

    input_str = input_str.upper()
    morse_code = []

    for char in input_str:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            raise AssertionError("the arguments are bad")

    return ' '.join(morse_code)


def main() -> None:
    """
    Main function to handle input arguments and convert them to Morse code.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        input_str = sys.argv[1]

        if not all(char.isalnum() or char == ' ' for char in input_str):
            raise AssertionError("the arguments are bad")

        encoded_message = convert_to_morse(input_str)
        print(encoded_message)

    except AssertionError as error:
        print(f"AssertionError: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
