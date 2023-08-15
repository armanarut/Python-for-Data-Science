import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D array from start to end.

Args:
    family (list): A 2D array.
    start (int): Start index.
    end (int): End index.

Returns:
    list: A 2D array sliced from start to end.

Raises:
    AssertionError: If family is empty.
    AssertionError: If family elements are not list.
    AssertionError: If family elements are not of the same length.
    AssertionError: If start is not int.
    AssertionError: If end is not int."""

    try:
        assert family != [], "Family must not be empty."
        assert all(isinstance(f, list) for f in family),\
            "All family elements must be list."
        assert all(len(f) == len(family[0]) for f in family),\
            "All family elements must be list of the same length."
        assert type(start) == int, "Start must be int."
        assert type(end) == int, "End must be int."

        arr = np.array(family)
        print("My shape is :", arr.shape)

        arr = arr[start:end]
        print("My new shape is :", arr.shape)

        return arr.tolist()

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return []
