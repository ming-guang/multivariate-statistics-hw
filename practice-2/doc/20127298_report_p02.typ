#import "template.typ": *

#show: project.with(
  title: "Practice 2",
  authors: (
    "Nguyễn Trần Minh Quang - 20127298",
  ),
)

= Progress
#table(
  columns: (25pt, auto, auto),
  inset: 10pt,
  align: horizon,
  [], [*Task*], [*Progress*],
  [1], [Read data from the given Covid-19 cases CSV file], [100%],
  [2], [Visualize data with atleast 3 graphs using matplotlib], [100%],
  [3], [Give some comments, analytic... from the corresponding graphs], [100%]
)
= The program
== Data input
- Covid-19 cases CSV files
- Major samples files
== Data output
- Vietnam's covid cases and death graph
- Covid case by country pie chart
- Men and women in each major category chart
== Usage
1. Navigate to the source folder
2. Create a virtual environment
```sh
$ virtualenv venv
```
3. Activate the virtual environment
```sh
$ source venv/bin/activate
```
4. Install the required dependencies
```sh
# On windows or osx
$ pip install -r requirements.txt
# On linux
$ pip install -r requirements_linux.txt
```
5. Run the program
```sh
$ python main.py
```
#pagebreak()
== Output graph
=== Vietnam's covid cases and death graph
#figure(
  image("images/vietnam_covid_cases_and_deaths.png"),
  caption: [
    Vietnam's covid cases and deaths from Jan 22nd 2020 to May 6th 2021
  ],
)
==== Implementation
1. Read the content from covid cases csv and covid deaths csv using ```python pandas```
2. Filter row with the ```python Country/Region``` column is ```python Vietnam```
3. Concat 2 data frames
4. Plot it
==== Comment
The graph surge around August 2020, January 2021 and April 2021 also indicate the 3 covid "waves" in Vietnam.
#pagebreak()
=== Covid case by country pie chart
#figure(
  image("images/covid_total_cases_by_country.png"),
  caption: [
    25 countries with most covid cases
  ],
)
==== Implementation
1. Read the content from the latest covid data csv using ```python pandas```
2. Filter where the entry is not a country since this data also contains sum of continent and world data
3. Sort by ```python total_cases```
4. Get the top 20
5. Sum the other's country ```python total_cases``` to the ```python Others``` index
6. Concat it with the top 20 data frame
7. Plot it
==== Comment
Most of the cases on the later of the pandemic is mostly reported by the USA and India.
#pagebreak()
=== Men and women in each major category chart
#figure(
  image("images/men_and_women_in_each_major_category.png"),
  caption: [
    Men and womens distributions among top major categories
  ],
)
==== Implementation
1. Read the content from majors csv using ```python pandas```
2. Group by ```python Major_category``` and get the sum of ```python Men``` and ```python Women``` columns
3. Plot it
==== Comment
There is an imbalance in the engineering-related fields which men had way higher ratio then women, also on social science-related field women had way higher ratio then men.
