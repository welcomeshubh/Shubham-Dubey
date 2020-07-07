# Take two int values from user and print greatest among them.

# Take the First Number.
a = int(input("Enter First Number: "))

#Take the Second Number.
b = int(input("Enter First Number: "))

#Compare Two Numbers
if a == b:
	# Print Result
	print("First Number is equal to Second Number. {} = {}".format(a,b))

elif a > b:
	print("First Number is greater than Second Number. {} > {}".format(a,b))

else:
	print("Second Number is greater than First Number. {} < {}".format(a,b))



# You can also solve this problem by min(a,b) or max(a,b) function.