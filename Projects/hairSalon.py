#this project will utilize loops and lists to represent the business operations of a hairsalon for one week
#including types of hairstyles, prices, and the total purchases in the past week

#list containing hairstyle offerings
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

#list containing prices of hairstyles corresponding to hairstyles list
prices = [30, 25, 40, 20, 20, 35, 50, 35]

#number of purchases for hairstyles in the last week contained in a list
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#find out what the average price of a cut is
total_price = 0
#loop thru prices list and add each price to total price
for i in last_week:
  total_price += i
#determine average
average_price = total_price / len(prices)
#output average
print('Average Haircut Price: ' + str(average_price))

#use a list comprehension to cut all prices by $5 in discount for all customers
new_prices = [price - 5 for price in prices]
#output new prices
print(new_prices)

#we now want to determine how much revenue was brought in from last week
#set variable called total_revenue and set to 0
total_revenue = 0

#create for loop and add the product of prices of haircuts and number of purchases per haircut type for last week
for i in range(len(hairstyles)):
  total_revenue += (prices[i] * last_week[i])

#output total revenue
print('Total Revenue: ' + str(total_revenue))

#find average daily revenue by dividing total_revenue by 7 and output the results
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

#we want to bring in more customers by advertisting all haircuts under $30
#use list comprehension to create list to output all hairstyles for which the price is less than 30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30]
#output list comprehension results
print(cuts_under_30)