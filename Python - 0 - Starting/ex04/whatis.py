import sys


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


try:
    n = len(sys.argv)
    assert n <= 2, "more than one argument is provided"

    if n == 2:
        number = sys.argv[1]
        assert is_integer(number), "argument is not an integer"

        number = int(number)
        if number % 2 == 0:
            print("I'm Even")
        else:
            print("I'm Odd")

except AssertionError as e:
    print("AssertionError: ", e)
