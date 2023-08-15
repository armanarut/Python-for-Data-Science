import sys
from ft_filter import ft_filter


def main():
    """Filter a string for words longer than N characters.

The string can be provided as an argument or as user input.

The program will print the words longer than N characters.

The program will raise an AssertionError if the arguments is different from 2,
or if the type of any argument is wrong."""

    try:
        n = len(sys.argv)
        assert n == 3, "the arguments are bad"
        S = sys.argv[1]

        assert type(S) is str, "the arguments are bad"
        N = sys.argv[2]

        assert (lambda value: value.isdigit())(N), "the arguments are bad"
        N = int(N)

        print(list(ft_filter(lambda word: len(word) > N, S.split())))

    except AssertionError as e:
        print("AssertionError: ", e)


if __name__ == "__main__":
    main()
