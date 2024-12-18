import math

# Lists: Ordered, mutable collections
my_list = [1, 2, 3, "four"]
my_list.append(5)
print(my_list)

# Tuples: Ordered, immutable sequences
my_tuple = (1, 2, 3)

# Dictionaries: key vlaue pairs
person = {"name": "Alice", "age": 25}
print(person["name"])
print(person["age"])

# Set: Unordered collection of unique elements
my_set = {1, 2, 3, 2, 2, 1, 4}
print(my_set)


# Basic error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Bananas! Cannot divide by Zero!")


print(math.sqrt(198723746475653456789876543456784746756746564782))

dictionnary_harmeet = {
    "key1": ['X', 20],
    "key2": ['X', 40],
    "key3": ['Harmeet', 40],
    "key4": ['Harmeet', 60]
}

print(dictionnary_harmeet["key1"])

{['X',20],['X',40],['Harmeet',40],['Harmeet',60]}

