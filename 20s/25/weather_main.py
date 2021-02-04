# working with csv using the csv reader
# import csv

# with open('weather_data.csv') as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != 'temp':
#            temperatures.append(int(row[1]))
# print(temperatures)

# working with pandas to work with csv files
# import pandas
# data = pandas.read_csv('weather_data.csv')
# temperatures = data['temp']
# temp_list = temperatures.to_list()

# average = data['temp'].mean()
# max = data['temp'].max()

# get data in columns
# print(data['condition'])
# print(data.condition)

# get data in row
# print(data[data['day']=='Monday'])
# print(data[data.day == 'Monday'])

# get row of data with highest temperature
#print(data[data.temp == data.temp.max()])

# get mondays temperature in F
# monday = data[data.day == 'Monday']
# monday_temp = (int(monday.temp) * (9/5)) + 32
# print(monday_temp)

# create dataframe from scratch
# data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "scores" : [76,56,65]
#}
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)
