# A school has following rules for grading system:
marks = float(input("Enter your marks: "))
if marks < 25:
 grade = 'F'
elif marks >= 25 and marks < 45:
 grade = 'E'
elif marks >= 45 and marks < 50:
 grade = 'D'
elif marks >= 50 and marks < 60:
 grade = 'C'
elif marks >= 60 and marks < 80:
 grade = 'B'
else:
 grade = 'A'
print("Your grade is:", grade)
