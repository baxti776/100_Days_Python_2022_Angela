# with open("./weather-data.csv") as weather_data:
#     data = (weather_data.readlines())
#     print(data)
# import csv
#
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv("weather-data.csv")
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))
# data_dic = data.to_dict()
# print(data_dic)
# data_list = data["temp"].to_list()
# print(data_list)
# print(data["temp"].mean())
# print(data["temp"].max())
# average_data = 0
# data_len = len(data_list)
# for data in data_list:
#     average_data += data
# print(average_data)
# average_data /= data_len
# print(f"Average temp: {average_data}")
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_fara = (monday.temp * 1.8) + 32
# print(monday_fara)

# Creating a new dataframe
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

park = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Grey = len(park[park["Primary Fur Color"] == "Gray"])
Black = len(park[park["Primary Fur Color"] == "Black"])
Red = len(park[park["Primary Fur Color"] == "Cinnamon"])

# print(park.color)
print(f"Black: {Black}, Grey: {Grey}, Cinnamon: {Red}")
