# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.



#ACCEPT QUANTITY FROM USER
quantity = int(input("Please Tell Me The Quantity: "))

#CALCULATE ACTUAL PRICE
total_price = quantity * 100

#CHECK IF ACTUAL PRICE IS MORE THAN 1000
if total_price > 1000:

# IF ACTUAL PRICE IS MORE THAN 1000, GIVE 10% DISCOUNT
	user_cost = total_price - (total_price * 0.1)

else:

# IF ACTUAL PRICE IS NOT ,ORE THAN 1000, THEN THE AMOUNT TO BE PAID IS ACTUAL PRICE ONLY.
	user_cost = total_price


#ASK FOR PAYMENT WITH AMOUNT.
print("Kindly Pay Me {} INR.".format(user_cost))