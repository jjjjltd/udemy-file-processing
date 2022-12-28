import pandas
import random

def csvtricks():
    csvdata = pandas.read_csv("Weather Data.csv")
    print("\nPrint CSV Data as Table.")
    print(csvdata)
    print("\nPrint Temperature then Day columns only.\n")
    print(f"(\n{csvdata['temp']}, {csvdata['day']}")

    # Convert temperature data to list.
    temp_list = csvdata["temp"].to_list()

    average_temp = sum(temp_list)/len(temp_list)

    print("\nPrint average temperture 1. Using formula, 2 using csv function - and demo of 'max' arithmetic function.\n")
    print(average_temp)
    print(csvdata["temp"].mean())
    print(csvdata["temp"].max())

    print("Print selected rows based on selection criteria.")
    day_choice = random.choice(["Monday", "Tuesday", "Wednesday"])
    print(csvdata[csvdata.day == day_choice])
    print(csvdata[csvdata.temp == csvdata["temp"].min()])

csvtricks()