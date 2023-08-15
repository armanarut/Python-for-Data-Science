import sys


def main():
    """Program takes a string as an argument and encodes it into Morse Code.

The Morse Code should only contain space and alphanumeric characters.

The program will raise an AssertionError if the arguments is different from 2,
or if the type of argument is wrong."""

    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ",
                    "B": "-... ",
                    "C": "-.-. ",
                    "D": "-.. ",
                    "E": ". ",
                    "F": "..-. ",
                    "G": "--. ",
                    "H": ".... ",
                    "I": ".. ",
                    "J": ".--- ",
                    "K": "-.- ",
                    "L": ".-.. ",
                    "M": "-- ",
                    "N": "-. ",
                    "O": "--- ",
                    "P": ".--. ",
                    "Q": "--.- ",
                    "R": ".-. ",
                    "S": "... ",
                    "T": "- ",
                    "U": "..- ",
                    "V": "...- ",
                    "W": ".-- ",
                    "X": "-..- ",
                    "Y": "-.-- ",
                    "Z": "--.. ",
                    "0": "----- ",
                    "1": ".---- ",
                    "2": "..--- ",
                    "3": "...-- ",
                    "4": "....- ",
                    "5": "..... ",
                    "6": "-.... ",
                    "7": "--... ",
                    "8": "---.. ",
                    "9": "----. "
                    }

    try:
        n = len(sys.argv)
        assert n == 2, "the arguments are bad"
        S = sys.argv[1]
        assert all((c.isalnum() or S.isspace()) for c in S),\
            "the arguments are bad"
        S = S.upper()
        newlist = []
        for letter in S:
            newlist.append(NESTED_MORSE[letter])
        print("".join(newlist))

    except AssertionError as e:
        print("AssertionError: ", e)


if __name__ == "__main__":
    main()
