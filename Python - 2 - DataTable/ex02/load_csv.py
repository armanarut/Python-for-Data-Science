import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    """Loads a csv file into a pandas DataFrame.

    Args:
        path (str): Path to the csv file.

    Returns:
        DataFrame: Pandas DataFrame with the loaded data.
    """
    try:
        data = pd.read_csv(path)

        print("Loading dataset of dimensions", data.shape)

        return data

    except FileNotFoundError:
        print("File not found")
        return None
