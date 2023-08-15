import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
# import sys
# sys.path.append('..\\ex00')
from load_csv import load


def convert_to_int(number_str):
    """Converts a string to an integer.

    The string can contain a suffix 'k' or 'M' to indicate thousands or
    millions."""
    if type(number_str) == int:
        return number_str
    suffixes = {
        'k': 1000,
        'M': 1000000,
    }
    if number_str[-1] in suffixes:
        return int(float(number_str[:-1]) * suffixes[number_str[-1]])
    else:
        return int(float(number_str))


def convert_to_1k(number, p):
    """Converts a number to a string with a 'k' or 'M' suffix.

    The number is divided by 1000^p, where p is the power of 1000 that
    corresponds to the suffix."""
    if number < 0:
        return "-" + convert_to_1k(-number, p)
    if number >= 1000000:
        return f"{number/1000000:.0f}M"
    elif number >= 1000:
        return f"{number/1000:.0f}k"
    else:
        return f"{number:.0f}"


def main():
    """Main function of the script.

    Loads the data and plots the Gross domestic product and life expectancy."""

    income_name = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    data_life = load("life_expectancy_years.csv")
    data_income = load(income_name)
    year = "1900"

    if data_life is not None and data_income is not None:
        life = data_life[year]
        income = [convert_to_int(x) for x in data_income[year] if x != ""]

        plt.figure(figsize=(8, 6))
        major_ticks = [300, 1000, 10000]

        ax = plt.subplot()
        ax.scatter(income, life, alpha=0.7)

        ax.set_xscale('log')
        ax.get_xaxis().set_major_formatter(
                ticker.FuncFormatter(convert_to_1k))
        ax.xaxis.set_major_locator(ticker.FixedLocator(major_ticks))
        ax.set_xlim(300, 10200)
        ax.set(xlabel='Gross domestic product', ylabel='Life Expectancy',
               title='1900')

        plt.show()


if __name__ == '__main__':
    main()
