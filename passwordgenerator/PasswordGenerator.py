#Basic password generator using Python
import random
import string


print("Welcome to the Password Generator!")
lettersNum = int(input("How many letters would you like in your password?\n"))
symbolsNum = int(input("How many symbols would you like in your password?\n"))
numbersNum = int(input("How many numbers would you like in your password?\n"))

letters = string.ascii_letters

symbols = string.punctuation

numbers = string.digits

selection_list = []

for i in range(0,lettersNum):
    selection_list += random.choice(letters)

for i in range(0,symbolsNum):
    selection_list += random.choice(symbols)

for i in range(0,numbersNum):
    selection_list += random.choice(numbers)

random.shuffle(selection_list)

s = ''.join(selection_list)

print(s)

