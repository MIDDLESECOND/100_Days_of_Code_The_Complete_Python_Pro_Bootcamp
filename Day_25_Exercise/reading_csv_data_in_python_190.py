with open("weather_data.csv", mode = "r") as file:
    data = file.readlines()

print(data)

# inherent csv package to work with csv
import csv

with open("weather_data.csv", mode = "r") as file:
    data = csv.reader(file)
    temperature = []
    for row in data:
        if row[1] != 'temp':
            day_temperature = row[1]
            temperature.append(int(day_temperature))

print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data['temp'])