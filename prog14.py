# Print multiplication table of 24, 50 and 29 using loop.
numbers = [24, 50, 29]
for num in numbers:
 print("Multiplication table of", num, ":")
 for i in range(1, 11):
  result = num * i
 print(num, "x", i, "=", result)
 print()