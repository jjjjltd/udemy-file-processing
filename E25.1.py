import pandas
import csv

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


furlist = data["Primary Fur Color"].to_list()
sights = data["Above Ground Sighter Measurement"].to_list()


# print(furlist)

black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(black_squirrel_count)
print(gray_squirrel_count)
print(red_squirrel_count)

data_dict = {
    "Fur Colour": ["Gray", "Black", "Red"],
    "Count": [gray_squirrel_count, black_squirrel_count, red_squirrel_count],
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("Squirrel Count.csv")

# print(furlist)
# print(sights)

# # dataframe = pandas.dataFrame(furlist, sights)
# dataframe2 = pandas.DataFrame(csvdata["Primary Fur Color"])

# gray_squirrel_count = len(csvdata["Primary Fur Color"] == "Gray")
# red_squirrel_count = len(csvdata["Primary Fur Color"] == "Red")
# sinful_squirrel_count = len(csvdata["Primary Fur Color"] == "Cinnamon")



# print(dataframe2)
# print(dataframe2.count())
# print(f"Grays:  {gray_squirrel_count}")