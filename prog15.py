#15. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input).Print average and product of all numbers.
numbers = []
while True:
 num = input("Enter an integer (press q to quit): ")
 if num == 'q':
  break
 else:
   num = int(num)
 numbers.append(num)
if len(numbers) > 0:
 avg = sum(numbers) / len(numbers)
 prod = 1
 for num in numbers:
  prod *= num
 print("Average:", avg)
 print("Product:", prod)
else:
 print("No numbers were entered.")