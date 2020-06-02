# Create a tuple containing the names of five countries and display the whole tuple.
# Ask the user to enter one of the countries that have been shown to them and then display
# the index number (i.e. position in the list) of that item in the tuple.
countries = ("Belgium", "Cuba", "Israel", "Morocco", "Zambia")


def country(x):
    print(x)
    choice = input("Please, type any country: ")
    return f'Index country {choice} is {x.index(choice)}'


print(country(countries))


# Add to the previous program to ask the user to enter a number and display the country in that position.
countries = ("Belgium", "Cuba", "Israel", "Morocco", "Zambia")


def country(x):
    print(x)
    choice = int(input("Please, type country number: "))
    return f'Country name is {countries[choice - 1]}'


print(country(countries))

# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
key = {0: 10, 1: 20}


def add_key(x):
    print(x)
    x[2] = 30
    return x


print(add_key(key))

# Write a Python program to iterate over dictionaries using for loops.
key = {0: 10, 1: 20, 2: 30}


def iterate(x):
    for i in x:
        print(x[i])


iterate(key)


# Write a Python script to merge two Python dictionaries.
key = {0: 10, 1: 20, 2: 30}
key_1 = {0: 100, 1: 90, 2: 80}


def merge_dictionaries(x, y):
    result = {}
    index = 0
    for i in x:
        result[index] = x[i]
        index += 1
    for i in y:
        result[index] = y[i]
        index += 1
    return result


print(merge_dictionaries(key, key_1))

# Write a Python program to remove duplicates from the Dictionary.
dictionary = {0: 100, 1: 90, 2: 80, 3: 100, 4: 90, 5: 70}


def remove(x):
    print(x)
    result = {}
    for key, value in x.items():
        if value not in result.values():
            result[key] = value
    return result


print(remove(dictionary))

# Write a Python program to remove spaces from dictionary keys.
dictionary = {"first numb": 100, "second numb": 90, "third numb": 80, "fourth numb": 100, "fifth numb": 90, "sixth numb": 70}


def remove_spaces(numbers):
    numbers = {key.replace(' ', ''): values for key, values in numbers.items()}
    return numbers


print(remove_spaces(dictionary))

# Write a Python program to get the maximum and minimum value in a dictionary.
dictionary = {0: 100, 1: 90, 2: 80, 3: 101, 4: 90, 5: 20}


def max_min(numbers):
    maximum = max(numbers.values())
    minimum = min(numbers.values())
    return maximum, minimum


print(max_min(dictionary))


# Write a Python program to check a dictionary is empty or not.
dictionary = {0: 100, 1: 90, 2: 80, 3: 101, 4: 90, 5: 20}


def check_empty(numbers):
    if len(numbers) == 0:
        return "dictionary empty"
    else:
        return "dictionary not empty"


print(check_empty(dictionary))


# Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}


def add_dictionary(x, y):
    result = {}
    for key in x:
        if key in y:
            add_value = x[key] + y[key]
        else:
            add_value = x[key]
        result[key] = add_value
    for key in y:
        if key not in result:
            result[key] = y[key]
    return result


print(add_dictionary(d1, d2))

# Write a Python program to print a dictionary line by line.
dictionary = {0: 100, 1: 90, 2: 80, 3: 101, 4: 90, 5: 20}


def print_dictionary(d):
    result = list(d.items())
    for item in result:
        print(item)


print_dictionary(dictionary)
