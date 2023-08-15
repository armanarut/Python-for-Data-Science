from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Main function of the script.

    Loads the data and plots the life expectancy of a country.
    """

    data = load("life_expectancy_years.csv")
    country_name = "Armenia"

    if data is not None:
        country_data = data[data["country"] == country_name]

        years = data.columns[1:].astype(float)
        life_expectancy = country_data.values[0, 1:].astype(float)

        # Plotting the data
        plt.plot(years, life_expectancy)
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.title(f"{country_name} Life expectancy Projections")
        plt.show()


if __name__ == "__main__":
    main()
