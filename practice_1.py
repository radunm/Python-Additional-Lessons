# Write a Python program to calculate the area of a rectangle.
height = 10
width = 3
area = height * width


# Write a Python program to calculate the area of a circle
pi = 3.14
r = 3
circle_area = pi * r ** 2


# Ask for the user’s first name and display the output message Hello [First Name].
first_name = input("Please, enter your name: ")
print("Hello, " + first_name + "!")


# Ask the user to enter two numbers. Add them together and display the answer as The total is [answer].
numb_1 = int(input('Enter first number: '))
numb_2 = int(input('Enter second number: '))
total = numb_1 + numb_2
print('The total is ' + str(total))


# Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third.
# Display the answer as The answer is [answer].
numb_1 = int(input('Enter first number: '))
numb_2 = int(input('Enter second number: '))
numb_3 = int(input('Enter third number: '))

result = (numb_1 + numb_2) * numb_3
print('The answer is ' + str(result))


# Ask the user for their name and their age. Add 1 to their age and display the output [Name] next birthday you will be
# [new age].
name = input('Enter your name: ')
age = int(input('Enter your age: '))
print(name + ' next birthday you will be ' + str(age + 1))


# Ask an integer number, check is it odd or even and return answer
numb = int(input('Enter number: '))
if numb % 2 == 0:
    print('even')
else:
    print('odd')


# Ask the user to type in any word and display it in upper case. (See string methods)
word = input("Please, enter any word: ")
print(word.upper())


# Ask for the user’s first name and then ask for their surname and display the output
# message Hello [First Name] [Surname]
first_name = input("Please, enter your first name: ")
surname = input("Please, enter your surname: ")
print('Hello ' + first_name + ' ' + surname)


# Write code that will display the joke “What do you call a bear with no teeth?” and on the next line display the
# answer “A gummy bear!”  Try to create it using only one line of code.
print("What do you call a bear with no teeth?" + "\n" + "A gummy bear!")


# Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices
# they have left and display the answer in a user-friendly format
slice_number = int(input("How many slices of pizza do you started with? "))
eaten = int(input("How many slices of pizza you have eaten? "))

print("Pizza had " + str(slice_number) + " slices. You eat " + str(eaten) + " slices. There are " + str(
slice_number - eaten) + " slices left")


# Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of
# diners and show how much each person must pay.
total_bill = int(input("What was the total price of the bill? "))
diners = int(input("How many diners are there? "))
pay = total_bill / diners
print("Each person have to pay " + str(pay))


# Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in
# that number of days.
days = int(input("Enter any number of days: "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print("In " + str(days) + " days " + str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds.")


# Ask the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller
# number goes into the larger number in a user-friendly format.
first_number = int(input("Enter a number over 100: "))
if first_number > 100:
    second_number = int(input("Enter a number under 10: "))
    if second_number < 10:
        result = first_number // second_number
        print("Second number goes into the first number " + str(result) + " times.")


# Ask the integer number and return the second power of this number.
integer = int(input("Enter any integer: "))
print("The second power of number " + str(integer) + " is " + str(integer ** 2))


# Ask the integer number and power what you would like to get. Return result
integer = int(input("Enter any integer: "))
power = int(input("Enter power: "))
print("Integer " + str(integer) + " to the power of " + str(power) + " will be " + str(integer ** power))


# Ask the user to enter their first name and then display the length of their name.
first_name = input("Please, enter your first name: ")
print("Length of your name " + str(len(first_name)) + " characters")


# Ask the user to enter their first name and then ask them to enter their surname. Join them together with a space
# between and display the name and the length of the whole name.
first_name = input("Please, enter your first name: ")
surname = input("Please, enter your surname: ")
name = first_name + " " + surname
print(name + " and the length of the whole name is " + str(len(name)))


# Ask the user to enter their first name and surname in lower case. Change the case to title case and join them
# together. Display the finished result.
first_name = input("Please, enter your first name in lower case: ").upper()
surname = input("Please, enter your surname in lower case: ").upper()
print(first_name + " " + surname)


# Enter a random string, which includes only digits. Write a function sum_digits which will find a sum of digits in
# this string
digits = input("Please, enter a string of digits: ")


def sum_digits(dig):
    summ = 0
    for i in dig:
        summ += int(i)

    return summ


print(sum_digits(digits))


# Ask the user to enter their favorite color. If they enter “red”, “RED” or “Red” display the message “I like red too”,
# otherwise display the message “I don’t like [color], I prefer red”.
color = input("Please, enter your favorite color: ").lower()
if color == "red":
    print("I like red too")
else:
    print("I don’t like " + color + ", I prefer red")


# Ask the user’s age. If they are 18 or over, display the message “You can vote”, if they are aged 17, display the
# message “You can learn to drive”, if they are 16, display the message “You can buy a lottery ticket”, if they are
# under 16, display the message “You can go Trickor-Treating”.
age = int(input("Please, enter your age: "))
if age >= 18:
    print("You can vote")
if age == 17:
    print("You can learn to drive")
if age == 16:
    print("You can buy a lottery ticket")
if age < 16:
    print("You can go Trickor-Treating")


# Ask the user to enter a number. If it is under 10, display the message “Too low”, if their number is
# between 10 and 20, display “Correct”, otherwise display “Too high”.
number = int(input("Please, enter any number: "))
if number < 10:
    print("Too low")
elif 10 <= number <= 20:
    print("Correct")
else:
    print("Too high")


# Ask the user to enter 1, 2, or 3. If they enter a 1, display the message “Thank you”, if they enter a 2,
# display “Well done”, if they enter a 3, display “Correct”. If they enter anything else, display “Error message”.
number = int(input("Please, enter 1, 2, or 3: "))

if number == 1:
    print("Thank you")
elif number == 2:
    print("Well done")
elif number == 3:
    print("Correct")
else:
    print("Error message")
