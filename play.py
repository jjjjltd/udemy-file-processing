import pandas
import random
import play0_1
import play0_2

print("\nData Dictionary and Data Frames.\n")
data_dict = {
    "students": ["Johnny", "Freddy", "Rose"],
    "scores": [86, 93, 44],
}

# Create new panda frame
dataframe = pandas.DataFrame(data_dict)
print(dataframe)
dataframe.to_csv("New Data Frame.csv")