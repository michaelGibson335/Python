#import random module
import random

#lists containing letters of the alphabet, numbers 0-9 and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
numberLetters = int(input("How many letters would you like in your password?\n")) 
numberSymbols = int(input(f"How many symbols would you like?\n"))
numberNumbers = int(input(f"How many numbers would you like?\n"))

#list to contain appended characters pulled from the loops below
newCharactersList = []

#loop to go through letters list and pull random letters and append to newCharacters List
countLetters = numberLetters
lengthLetters = len(letters) // 2

while countLetters != 0:
    newCharactersList.append(letters[random.randrange(0, lengthLetters)])
    countLetters = countLetters - 1

#loop to go through symbols list and pull random symbols and append to newCharacters List
countSymbols = numberSymbols
lengthSymbols = len(symbols) // 2

while countSymbols != 0:
    newCharactersList.append(symbols[random.randrange(0, lengthSymbols)])
    countSymbols = countSymbols - 1

#loop to go through numbers list and pull random numbers and append to newCharacters List
countNumbers = numberNumbers
lengthNumbers = len(numbers) // 2

while countNumbers != 0:
    newCharactersList.append(numbers[random.randrange(0, lengthNumbers)])
    countNumbers = countNumbers - 1

#new list to contain final password
finalPassword = []

#pull length of newCharacters list
lengthCharList = len(newCharactersList)

#counter for newCharacters list length for loop below
newCharCount = len(newCharactersList)

#loop to randomize character selection and append to finalPassword list
while newCharCount != 0:
    finalPassword.append(newCharactersList[random.randrange(0, lengthCharList)])
    newCharCount -= 1

#output password result by looping through finalPassword list
print('Here is your password: ')
for i in finalPassword:
    print(i, end='')
print()









