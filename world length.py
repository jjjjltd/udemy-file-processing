sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

list1 = sentence.split(" ")

result = {word: len(word) for word in list1}

for word in result:
    print(f"{word}: {result[word]}")
print(result)