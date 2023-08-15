import sys


def main():
    """
    Count the number of characters in a string and print the result.

    The string can be provided as an argument or as user input.

    The program will print the number of upper and lower case letters,
    punctuation marks, spaces and digits in the string.
    """
    try:
        n = len(sys.argv)
        assert n <= 2, "more than one argument is provided"

        if n == 1:    # promt user for input
            str = input("What is the text to count?\n")
        else:           # use argument
            str = sys.argv[1]

        print("The text contains", len(str), "characters:")
        print(sum(1 for c in str if c.isupper()), "upper letters")
        print(sum(1 for c in str if c.islower()), "lower letters")
        print(sum(1 for c in str if not c.isalnum() and not c.isspace()),
              "punctuation marks")
        print(sum(1 for c in str if c.isspace() or c == '\n'), "spaces")
        print(sum(1 for c in str if c.isdigit()), "digits")
    except AssertionError as e:
        print("AssertionError: ", e)
    except Exception as e:
        print("Exception: ", e)


if __name__ == "__main__":
    main()
