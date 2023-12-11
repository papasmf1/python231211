# List
my_list = [1, 2, 3, 4, 5]
print("List:")
print("Elements:", my_list)
print("Type:", type(my_list))
print("Length:", len(my_list))
print("Access an element:", my_list[0])
print("Iterate through elements:")
for item in my_list:
    print(item)

# Tuple
my_tuple = (1, 2, 3, 4, 5)
print("\nTuple:")
print("Elements:", my_tuple)
print("Type:", type(my_tuple))
print("Length:", len(my_tuple))
print("Access an element:", my_tuple[0])
print("Iterate through elements:")
for item in my_tuple:
    print(item)

# Set
my_set = {1, 2, 3, 4, 5}
print("\nSet:")
print("Elements:", my_set)
print("Type:", type(my_set))
print("Length:", len(my_set))
# Sets are unordered and do not support indexing or slicing
# You can iterate through elements, but the order is not guaranteed
print("Iterate through elements:")
for item in my_set:
    print(item)

# Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nDictionary:")
print("Elements:", my_dict)
print("Type:", type(my_dict))
print("Length:", len(my_dict))
print("Access a value by key:", my_dict['a'])
print("Iterate through keys:")
for key in my_dict:
    print(key, "->", my_dict[key])