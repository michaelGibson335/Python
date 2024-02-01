#print welcome message
print('Welcome to the tip calculator!')
#ask for the total bill
bill = float(input('What was the total bill? $'))
#ask for the amount of tip 
tip = int(input('How much tip would you like to give? 10, 12, or 15? '))
#ask for how many people to split the bill with
people = int(input('How many people to split the bill? '))
#determine bill with tip
tipAsPercent = tip / 100
tipTotalAmount = bill * tipAsPercent
totalBill = bill + tipTotalAmount
#determine bill per person
billPerPerson = totalBill / people
#round bill to 2 decimal places
finalAmount = round(billPerPerson, 2)
#print amount each person should pay
print('Each person should pay: ${}'.format(finalAmount))
