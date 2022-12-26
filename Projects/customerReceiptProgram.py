#This program is about a simple furniture
#inventory, utilizing variables

#store loveseat description
lovely_loveseat_description = '''
Lovely Loveseat. Tufted polyester
blend on wood. 32 inches high x 40
inches wide x 30 inches deep. Red or
white.
'''

#set price for loveseat
lovely_loveseat_price = 254.00

#store stylish settee description
stylish_settee_description = '''
Stylish Settee. Faux leather on
birch. 29.50 inches high x 54.75
inches wde x 28 inches deep. Black.
'''

#stylish settee price
stylish_settee_price = 180.50

#luxurious lamp description
luxurious_lamp_description = '''
Luxurious Lamp. Glass and iron. 36
inches tall. Brown with cream shade.
'''

#price for luxurious lamp
luxurious_lamp_price = 52.15

#store sales tax
sales_tax = .088

#keep tally of customer purchases
customer_one_total = 0

#keep list of descriptions of things customer is purchasing
customer_one_itemization = ''

#customer one has decided they're going to purchase lovely loveseat
#increment price for customer one total
customer_one_total += lovely_loveseat_price

#add lovely loveseat description to customer one itemization
customer_one_itemization += lovely_loveseat_description

#customer also bought luxurious lamp
#add to customer one total
customer_one_total += luxurious_lamp_price

#update itemization with luxurious lamp
customer_one_itemization += luxurious_lamp_description

#customer is ready to check out, calculate sales tax
customer_one_tax = customer_one_total * sales_tax

#add sales tax to customer's total cost
customer_one_total += customer_one_tax

#print receipt for customer
print('Customer One Items:')

#print itemization
print(customer_one_itemization)

#print customer one total so far
print('Customer One Total:')
print(customer_one_total)