# Write a program to print absolute vlaue of a number entered by user. E.g.-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1

#ACCEPT NUMBER FROM USER
num = int(input("Enter number for its absolute value: "))

#CHECK FOR POSITIVE NUMBERS AND NUMBER 0.
if num >= 0:

	print("Absolute value of {}: {}".format(num,num))

#CHECK FOR NEGATIVE NUMBERS.
elif num < 0:

	print("Absolute value of {}: {}".format(num, num*(-1)))

else:

	pass