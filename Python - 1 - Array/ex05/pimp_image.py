from PIL import Image
import numpy as np


def display_image(array) -> None:
    """Display the image received."""
    image = Image.fromarray(array)
    image.show()


def ft_invert(array) -> any:
    """Inverts the color of the image received."""
    inverted_array = array.copy()
    inverted_array = 255 - inverted_array

    display_image(inverted_array)
    return inverted_array


def ft_red(array) -> any:
    """Keep only the red channel of the image received."""
    red_array = array.copy()
    red_array[:, :, 1] = red_array[:, :, 2] = 0

    display_image(red_array)
    return red_array


def ft_green(array) -> any:
    """Keep only the green channel of the image received."""
    green_array = array.copy()
    green_array[:, :, 0] = green_array[:, :, 2] = 0

    display_image(green_array)
    return green_array


def ft_blue(array) -> any:
    """Keep only the blue channel of the image received."""
    blue_array = array.copy()
    blue_array[:, :, 0] = blue_array[:, :, 1] = 0

    display_image(blue_array)
    return blue_array


def ft_grey(array) -> any:
    """Convert the image received to a grey scale."""
    rgb_array = array.copy()
    grey_array = np.sum(rgb_array[:, :, i] / 3 for i in range(3))

    display_image(grey_array)
    return grey_array
