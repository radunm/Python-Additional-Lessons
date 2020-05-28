from random import randint

# Ask the user to enter their name and then display their name three times.
first_name = input("Please, enter your first name: ")
i = 0
while i < 3:
    print(first_name)
    i += 1


# Alter program 1 so that it will ask the user to enter their name and a number and then display their name that
# number of times.
first_name = input("Please, enter your first name: ")
repetition = int(input("How many times to repeat? "))
while repetition != 0:
    print(first_name)
    repetition -= 1


# Ask the user to enter their name and display each letter in their name on a separate line.
first_name = input("Please, enter your first name: ")
for letter in first_name:
    print(letter)


# Change program 3 to also ask for a number. Display their name (one letter at a time on each line) and repeat this for
# the number of times they entered.
first_name = input("Please, enter your first name: ")
repetition = int(input("How many times to repeat? "))
while repetition > 0:
    for i in first_name:
        print(i)
    repetition -= 1


# Ask the user to enter their name and a number. If the number is less than 10, then display their name that number of
# times; otherwise display the message “Too high” three times.
first_name = input("Please, enter your first name: ")
repetition = int(input("Enter number: "))
if repetition < 10:
    while repetition > 0:
        print(first_name)
        repetition -= 1
else:
    repetition = 3
    while repetition > 0:
        print("Too high")
        repetition -= 1


# Set a variable called total to 0. Ask the user to enter five numbers and after each input ask them if they want that
# number included. If they do, then add the number to the total. If they do not want it included, don’t add it to the
# total. After they have entered all five numbers, display the total.
total = 0
for i in range(5):
    number = int(input("Enter any number: "))
    choice = input("Do you want to add this number to the total? y(yes) or n(no) ")
    if choice == "y":
        total += number
    else:
        continue
print(f'The total is {total}')


# Ask which direction the user wants to count (up or down). If they select up, then ask them for the top number and
# then count from 1 to that number. If they select down, ask them to enter a number below 20 and then count down from
# 20 to that number. If they entered something other than up or down, display the message “I don’t understand”.
choice = input("Which direction do you want to count (up or down)? u(up) or d(down) ")
if choice == 'u':
    count = int(input("How far would you like to go? "))
    for i in range(1, count + 1):
        print(i)
elif choice == 'd':
    count = int(input("Enter a number below 20: "))
    for i in range(20, count - 1, -1):
        print(i)
else:
    print("I don’t understand")


# Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the names and after
# each name display “[name] has been invited”. If they enter a number which is 10 or higher, display the message
# “Too many people”.
choice = int(input("How many people would you like to invite to a party? "))
if choice < 10:
    for i in range(choice):
        first_name = input("Please, enter name of your guest: ")
        print(f'{first_name} has been invited')
elif choice >= 10:
    print("Too many people")


# Set the total to 0 to start with. While the total is 50 or less, ask the user to input a number. Add that number
# to the total and print the message “The total is… [total]”. Stop the loop when the total is over 50.
total = 0
while total <= 50:
    number = int(input("Enter any number: "))
    total += number
    print("The total is… " + str(total))


# Ask the user to enter a number. Keep asking until they enter a value over 5 and then display the message “The last
# number you entered was a [number]” and stop the program.
number = 0
while number <= 5:
    number = int(input("Enter any number: "))
    if number > 5:
        print(f'The last number you entered was {number}')


# Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they
# want to add another number. If they enter “y", ask them to enter another number and keep adding numbers until they
# do not answer “y”. Once the loop has stopped, display the total.
answer = "y"
total = int(input("Enter any number: "))
while answer == "y":
    number_1 = int(input("Enter another number: "))
    total += number_1
    answer = input("Do you want to add another number? y or n ")
print(f"The total is {total}")


# Ask for the name of somebody the user wants to invite to a party. After this, display the message “[name] has now
# been invited” and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until they
# no longer want to invite anyone else to the party and then display how many people they have coming to the party.
answer = "y"
total = 0
while answer == "y":
    first_name = input("Please, enter name of your guest: ")
    print(f'{first_name} has now been invited')
    total += 1
    answer = input("Do you want invite somebody else? y or n ")
print(f'You invited {total} people')


# Ask the user to enter a number between 10 and 20. If they enter a value under 10, display the message “Too low” and
# ask them to try again. If they enter a value above 20, display the message “Too high” and ask them to try again.
# Keep repeating this until they enter a value that is between 10 and 20 and then display the message “Thank you”.
number = int(input("Enter any number between 10 and 20: "))
value = True
while value:
    if number < 10:
        number = int(input("Too low, enter any number between 10 and 20: "))
    elif number > 20:
        number = int(input("Too high, enter any number between 10 and 20: "))
    else:
        print("Thank you")
        value = False


# Write a Python program to sum all the items in a list.
my_list = [1, 2, 3, 4, 5]
total = 0
for i in my_list:
    total += i
print(total)


# Write a Python program to multiplies all the items in a list.
my_list = [1, 2, 3, 4, 5]
total = 1
for i in my_list:
    total *= i
print(total)


# Write a Python program to get the largest number from a list.
arr = []
for i in range(10):
    item = randint(0, 50)
    arr.append(item)
print(arr)
max_number = arr[0]
for item in arr:
    if item > max_number:
        max_number = item
print(f'Largest number is {max_number}')

# Write a Python program to get the smallest number from a list
arr = []
for i in range(10):
    item = randint(0, 50)
    arr.append(item)
print(arr)
min_number = arr[0]
for item in arr:
    if item < min_number:
        min_number = item
print(f'Smallest number is {min_number}')


# Write a Python program to remove duplicates from a list.
arr = ["c", "o", "m", "m", "o", "n", "m", "e", "m", "b", "e", "r"]
temp = []
for i in arr:
    if i not in temp:
        temp.append(i)
print(temp)


# Write a Python program to check a list is empty or not.
arr = [2, 7, 15]
if len(arr) == 0:
    print("List is empty")
else:
    print("List is not empty")


# Write a Python function that takes two lists and returns True if they have at least one common member.
list_1 = [7, 5]
list_2 = [1, 2, 7]


def compare(x, y):
    found = False
    for i in x:
        if i in y:
            found = True
    return found


print(compare(list_1, list_2))

# Write a Python program to get unique values from a list.
arr = [7, 5, 7, 8, 15]
result = []
for i in arr:
    if i not in result:
        result.append(i)
print(result)


# Write a Python program to select the odd items of a list.
arr = [7, 5, 7, 8, 15, 10, 11]
result = []
for i in arr:
    if i % 2 != 0:
        result.append(i)
print(result)


# Write a Python program to concatenate elements of a list
arr = [7, 5, 7, 8, 15, 10, 11, "f", 23]
temp = ""
for i in arr:
    temp += str(i)
arr.clear()
arr.append(temp)
print(arr)
