#13. Take 10 integers from keyboard using loop and print their average value on the screen.
sum = 0
for i in range(10):
 num = int(input("Enter an integer: "))
 sum += num
average = sum / 10
print("The average of the 10 integers is:", average)