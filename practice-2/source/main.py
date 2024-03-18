import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


COVID_19_CASES_CSV = "data/covid_19_cases.csv"
COVID_19_DEATHS_CSV = "data/covid_19_deaths.csv"
COVID_LATEST_CSV = "data/owid_covid_latest.csv"


def vietnam_covid_cases_and_deaths_graph():
    # read covid 19 cases and deaths data
    cases = pd.read_csv(COVID_19_CASES_CSV)
    deaths = pd.read_csv(COVID_19_DEATHS_CSV)

    # filtering data from Vietnam only
    vietnam_cases = cases.copy().loc[cases["Country/Region"] == "Vietnam"]
    vietnam_cases.drop(vietnam_cases.iloc[:, 0:5], inplace=True, axis=1)

    vietnam_deaths = deaths.copy().loc[deaths["Country/Region"] == "Vietnam"]
    vietnam_deaths.drop(vietnam_deaths.iloc[:, 0:5], inplace=True, axis=1)

    # merge cases and deaths data to a single DataFrame
    data = pd.concat([vietnam_cases, vietnam_deaths], axis=0)
    # give them a label
    data.index = ["Cases", "Deaths"]

    # plot it
    # need to transpose since plt default x-axis to be each row
    data.T.plot(kind="line")
    # show the legend
    plt.legend(loc="upper right")
    # save and show the plot
    plt.savefig("results/vietnam_covid_cases_and_deaths.png")
    plt.show()


def covid_total_cases_by_country_piechart():
    # number of country to shown in the chart
    size = 25

    # read latest covid data
    data = pd.read_csv(COVID_LATEST_CSV)
    data["continent"] = data["continent"].fillna("")
    data = data.loc[data["continent"] != ""]
    # we only need location and total cases
    data = data[["location", "total_cases"]]
    data.set_index("location")
    data["total_cases"] = pd.to_numeric(data["total_cases"]).fillna(0)
    # sort top 50 countries
    sorted_data = data.copy().sort_values(by="total_cases", ascending=False)
    data = sorted_data.head(size).copy()
    # calculate other's total cases
    others = sorted_data.tail(sorted_data.size - 50)["total_cases"].sum()
    data.loc[data.size] = ["Others", others]
    # plot the data
    data.plot.pie(y="total_cases", labels=data["location"], legend=False)
    # save and show the plot
    plt.savefig("results/covid_total_cases_by_country.png")
    plt.show()


def main():
    vietnam_covid_cases_and_deaths_graph()
    covid_total_cases_by_country_piechart()


if __name__ == "__main__":
    main()
