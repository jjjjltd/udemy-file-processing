# numbers = [1, 2, 3]

# # new_list = [n + 1 for n in numbers]
# new_list = [n+1 for n in numbers]
# print(new_list)

name = "Angela"

letters = [letter for letter in name]
print(letters)

doubled = [n*2 for n in range(1, 50) if n % 2 == 0]
print(doubled)

name_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

cap_long_names = [name.upper() for name in name_list if len(name) >= 5]
print(cap_long_names)

squared = [n**2 for n in range(1, 50) if n % 3 == 0]
print(squared)