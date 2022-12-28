import pandas
from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "alphabet.csv")
data = pandas.read_csv(file_path)

dict = data.to_dict()
phonetic_dict = {row.Letter: row.Word for (index, row) in data.iterrows()}

key = input("Enter something you want to see the phonetic alphbet for:  ").upper()

output_list = [phonetic_dict[letter] for letter in key if letter in phonetic_dict] 
print(output_list)  
