import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
# dataframe like a table

print(type(data['temp']))
# series like a list

print(data.to_dict())

print(data['temp'].to_list())
print(len(data['temp'].to_list()))

avg_temp = sum(data['temp']) / len(data['temp'].to_list())
avg_temp = round(avg_temp, 2)
print(f"average temperature is {avg_temp}.")
# can also use series.mean()

max_temp = data['temp'].max()
print(f"max temperature is {max_temp}.")

# Get data in columns
print(data['condition'])
# same as below, meaning columns are considered as df's attribute
print(data.condition)
# beware, columns names are CASE Sensitive

# Get data in row
print(data.loc[data['day'] == 'Monday', :])

# Get row with highest temp
print(data.loc[data['temp'] == data['temp'].max()])

monday_data = data.loc[data.day == 'Monday']
print(monday_data.condition)

# monday's temperature to Fahrenheit
monday_temp_c = float(monday_data['temp'])
monday_temp_f = monday_temp_c * 1.8 + 32
print(f"Monday temperature in Fahrenheit is {monday_temp_f}.")

# create data from scratch
data_dict = {
    "student": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

student_score_data = pandas.DataFrame(data_dict)
print(student_score_data)
student_score_data.to_csv("student_score_data.csv")