#import random to generate random number
from random import randrange
#This a simple rock, paper, scissors program, it takes a number input from the user
#and the corresponding input number pulls the variable rock, paper, scissors from the list
#it is stored in, then the "computer" will choose from the rock, paper, scissors list
#and it will output an ascii art of the choice and whether the user wins, loses or ties with
#the computer

#ascii art of rock, paper, scissors and variables storing them 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#list storing rock, paper, scissors ascii art variables
rockPaperScissors = [rock, paper, scissors]

#prompt user to input number corresponding to list storing rock, paper, scissors variables
handNumber = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

#simulate computer choice by generating random number range from 0-2 and pull from list
computerChoice = randrange(3)
computerNumber = rockPaperScissors[computerChoice]

#output your choice
print(rockPaperScissors[handNumber])

#output "computer" choice
print('Computer chose {}'.format(computerNumber))

#conditionals to print tie, win, lose depending on output
if(handNumber == computerChoice):
    print('Tie')
elif(handNumber == 0 and computerChoice == 1):
    print('You Lose!')
elif(handNumber == 0 and computerChoice == 2):
    print('You Win!')
elif(handNumber == 1 and computerChoice == 0):
    print('You Win!')
elif(handNumber == 2 and computerChoice == 1):
    print('You Win!')
elif(handNumber == 2 and computerChoice == 0):
    print('You Lose!')
elif(handNumber == 1 and computerChoice == 2):
    print('You Lose!')


