# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

# NUMBER OF CLASSES HELD
number_of_classes = int(input("Enter the number of classes held: "))

#NUMBER OF CLASSES ATTENDED
attended_classes = int(input("Enter the number of classes attended: "))

#CHECK ATTENDANCE PERCENTAGE
percentage = (attended_classes * 100) / number_of_classes

#PRINT THE PERCENTAGE OF CLASSES ATTENDED
print("Percentage of class attended: ",percentage)

#ALLOW TO SIT FOR EXAM IF PEERCENTAGE IS MORE THAN OR EQUAL TO 75
if percentage >= 75:

	print("Student is allowed to sit for exam.")

#IF NOT, DON'T ALLOW
else:

	print("Student is not allowed to sit for exam.")