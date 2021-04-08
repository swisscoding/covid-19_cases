#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

import colored
import pandas as pd
import matplotlib.pyplot as plt

print(colored.stylize("\n---- | Plotting COVID-19 cases in specified country | ----\n", colored.fg("red")))

# dataframe
df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")

# smaller more useful dataframe
small_df = df[["location", "new_cases", "total_deaths", "population", "date"]]
small_df_values = small_df.values

# user interaction
country = input("Enter the country: ")

# limitation to one country
mask = small_df_values[:,0] == country
small_df_values_with_mask = small_df_values[mask]

print(f"\nPopulation of {country}: {int(small_df_values_with_mask[-1:,3][0])}")
print(f"Total deaths: {int(small_df_values_with_mask[-1:,2][0])}\n")

# last 14 days and its cases
dates = [ i[8:] for i in small_df_values_with_mask[:,4][-15:-1]]
cases = small_df_values_with_mask[:,1][-15:-1]

fig = plt.figure("Plotting with Pyplot")
plt.scatter(dates, cases)
plt.plot(dates, cases)
plt.title("COVID-19 cases of the last 14 days")
plt.xlabel("Date - 2020")
plt.ylabel("Cases")
plt.show()
