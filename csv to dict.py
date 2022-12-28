import csv
from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "alphabet.csv")
with open(file_path, "r") as infile:
    csvdata = csv.reader(infile)
    mydict ={rows[0]:rows[1] for rows in csvdata}

print(mydict)

swap_text = input("Type something you want to see in phonetic alphbet:  ")

# phonetic = [mydict[letter] for letter in swap_text]
print(mydict["A"])
phonetic = [letter.upper() for letter in swap_text]
print(phonetic)