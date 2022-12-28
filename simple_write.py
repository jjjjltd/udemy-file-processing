import os

os.system('cls')
print(os.getcwd())
os.chdir("./EODay24/")
print(os.getcwd())

with open("jjj.txt", "a") as file:
    file.write("\nThis is a first file write.")

with open("jjj.csv", "w") as csvfile:
    csvfile.write("I want to, see, if this is, coolumn, delimited")    

with open("jjj.csv", "r") as csvfile:
    contents = csvfile.read()
    print(contents)

with open("../jjj back one path.txt", "w") as backpath:
    backpath.write("Writing back one directory path.")
