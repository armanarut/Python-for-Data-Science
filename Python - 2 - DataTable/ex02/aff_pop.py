from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


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

    Loads the data and plots the population of a country."""

    data = load("population_total.csv")
    country_name = "Armenia"
    other_country_name = "France"

    if data is not None:
        years = [float(col) for col in data.columns[1:]
                 if float(col) >= 1800 and float(col) <= 2050]
        country_str = data[data["country"] == country_name]
        country_data = country_str[[col for col in data.columns[1:]
                                    if float(col) in years]]
        other_country_str = data[data["country"] == other_country_name]
        other_country_data = other_country_str[[col for col in data.columns[1:]
                                                if float(col) in years]]

        population = [convert_to_int(x) for x in country_data.values[0, 0:]]
        other_population = \
            [convert_to_int(x) for x in other_country_data.values[0, 0:]]

        plt.figure(figsize=(10, 6), dpi=100)
        ax = plt.subplot()
        ax.plot(years, population,
                label=country_name)
        ax.plot(years, other_population,
                label=other_country_name, color="green")
        ax.get_yaxis().set_major_formatter(
                ticker.FuncFormatter(convert_to_1k))
        ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
        ax.yaxis.set_major_locator(ticker.IndexLocator(20000000, 20000000))
        ax.set(xlabel='Year', ylabel='Population',
               title='Population Projections')
        ax.legend(loc='lower right')

        plt.show()


if __name__ == '__main__':
    main()
