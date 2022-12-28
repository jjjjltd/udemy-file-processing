import csv
"""  CSV Module demos """

def readlines():
    """ The principle should be clear, but this is skipping lines - not sure why... """ 
    with open("Weather Data.csv") as csvfiles:
        for line in csvfiles:
            contents = csvfiles.readline()
            print(contents)
    temperature = []

def column_parse():
    """  This takes a column from a csv and builds a list based on it.  """
    temperature = []
    with open("Weather Data.csv") as csvfiles:
        row_data = csv.reader(csvfiles)
        for row in row_data:
            if row[0] != "day":
                temperature.append(int(row[1]))

    print(f"{temperature}")

print("Start play0_1")

readlines()
column_parse()

print("End play0_1\n\n")