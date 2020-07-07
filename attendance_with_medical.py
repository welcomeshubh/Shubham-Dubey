# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.
# Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

# NUMBER OF CLASSES HELD
number_of_classes = int(input("Enter the number of classes held: "))

#NUMBER OF CLASSES ATTENDED
attended_classes = int(input("Enter the number of classes attended: "))

#CHECK FOR MEDICAL CONDITIONS.
medical = input("Any MEDICAL CONDITIONS: ['Y','N']: ")

#CHECK ATTENDANCE PERCENTAGE
percentage = (attended_classes * 100) / number_of_classes

#PRINT THE PERCENTAGE OF CLASSES ATTENDED AND ANY MEDICAL CONDITION
print("Percentage of class attended: ",percentage)

print("Medical Condition: "+medical)

#ALLOW TO SIT FOR EXAM IF PEERCENTAGE IS MORE THAN OR EQUAL TO 75
if percentage >= 75 or medical == "Y".lower():

	print("Student is allowed to sit for exam.")

#IF NOT, DON'T ALLOW
else:

	print("Student is not allowed to sit for exam.")
