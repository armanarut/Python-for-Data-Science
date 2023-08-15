import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate BMI from height and weight.

Args:
    height (list[int | float]): List of height in meters.
    weight (list[int | float]): List of weight in kilograms.

Returns:
    list[int | float]: List of BMI values.

Raises:
    AssertionError: If the length of height and weight are not equal.
    AssertionError: If the type of height and weight are not int or float."""

    try:
        assert height != []
        assert len(height) == len(weight)
        assert all(isinstance(h, (int, float)) for h in height),\
            "All height elements must be int or float."
        assert all(isinstance(w, (int, float)) for w in weight),\
            "All weight elements must be int or float."

        x = np.array(weight)
        y = np.array(height)

        bmi_values = (x / y ** 2)

        return bmi_values.tolist()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply limit to BMI values.

Args:
    bmi (list[int | float]): List of BMI values.
    limit (int): Limit value.

Returns:
    list[bool]: List of boolean values.

Raises:
    AssertionError: If the type of bmi is not int or float.
    AssertionError: If the type of limit is not int."""

    try:
        assert bmi != []
        assert all(isinstance(b, (int, float)) for b in bmi),\
            "All bmi elements must be int or float."
        assert type(limit) == int, "Limit must be int."
        bmi_values = (np.array(bmi) > limit)
        return bmi_values.tolist()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return []
