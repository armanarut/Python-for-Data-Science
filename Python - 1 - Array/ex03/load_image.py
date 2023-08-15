import numpy as np
from PIL import Image


def ft_load(path: str) -> any:
    """Load an image from a path.

    Args:
        path (str): Path to the image.

    Returns:
        np.ndarray: An array of the image.

    Raises:
        AssertionError: If path is not str.
        AssertionError: If path is empty.
        AssertionError: If path does not end with .jpg or .jpeg.
        FileNotFoundError: If path does not exist."""

    try:
        assert type(path) == str, "Path must be a string."
        assert path != "", "Path must not be empty."
        assert path.endswith(".jpg") or path.endswith("jpeg"),\
            "Path must end with .jpg or .jpeg"

        im = Image.open(path)
        arr = np.array(im)
        print("The shape of image is :", arr.shape)

        return im

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return []

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return []
