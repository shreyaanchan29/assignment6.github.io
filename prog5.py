#. Write a Python program to calculate the sum and average of n integer numbers (input from the user).Input 0 to finish
total = 0
count = 0
num = int(input("Enter an integer (0 to finish): "))
while num != 0:
 total += num
 count += 1
 num = int(input("Enter an integer (0 to finish): "))
if count > 0:
    avg = total / count
else:
    avg = 0