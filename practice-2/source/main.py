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


def main():
    vietnam_covid_cases_and_deaths_graph()


if __name__ == "__main__":
    main()
