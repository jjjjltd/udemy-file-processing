import random

with open("jjj.txt") as infile:
    data = infile.readlines()
    print(random.choice(data))
