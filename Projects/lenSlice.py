#python project demonstrating usage of lists to organize
#sales data for pizza restaurant

#create list of types of pizza toppings to sell
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

#create list to keep track of how much each pizza slice costs
prices = [2, 6, 1, 3, 2, 7, 2]

#use method to count the number of occurences "2" in the price list and store result in "num_two_dollar_slices"
#and print out result
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#find length of toppings list and store in variable "num_pizzas"
num_pizzas = len(toppings)

#Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas
print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

#Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices.
#Each sublist in pizza_and_prices should have one pizza topping and an associated price.
pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]

#print pizzas_and_prices
print(pizza_and_prices)

#Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending)
pizza_and_prices.sort() 

#Store the first element of pizza_and_prices in a variable called cheapest_pizza
cheapest_pizza = pizza_and_prices[0]

#Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza
priciest_pizza = pizza_and_prices[-1]

#It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.
pizza_and_prices.pop()


#add new topping 'peppers' and price '2.5' and make sure it is in the correct area of the sorted list
pizza_and_prices.insert(4, [2.5, 'peppers'])

#Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest
three_cheapest = pizza_and_prices[0:3]

#print three cheapest list
print(three_cheapest)