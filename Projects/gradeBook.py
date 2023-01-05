#practice using Lists to reorganize subjects and grades

#last semester gradebook
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#create list called subjects and fill it with classes
#I'm taking
subjects = ['physics', 'calculus', 'poetry', 'history']

#create list called grades and put in scores
grades = [98, 97, 85, 88]

#create 2D list to contain both subjects and grades as gradebook
gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]

#test gradebook output by printing
print(gradebook)

#use append method to add computer science class with score of 100
gradebook.append(['computer science', 100])

#use append method to add visual arts class with score of 93
gradebook.append(['visual arts', 93])

#use index of gradebook to increase visual arts class grade to 98
gradebook[5][1] = 98

#change numberical grade value to Pass/Fail option for poetry class
#use remove() method to remove poetry class grade
gradebook[2].remove(85)

#use append() method to add 'Pass' to poetry class
gradebook[2].append('Pass')

#combine last semester gradebook with current gradebook and store in 'full_gradebook variable'
full_gradebook = last_semester_gradebook + gradebook

#print full_gradebook contents
print(full_gradebook)