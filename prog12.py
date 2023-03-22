#12. A student will not be allowed to sit in exam if his/her attendence is less than
classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))
attendance_percentage = (classes_attended / classes_held) * 100
if attendance_percentage >= 75:
 print("Attendance Percentage:", attendance_percentage, "%")
 print("The student is allowed to sit in the exam.")
else:
 print("Attendance Percentage:", attendance_percentage, "%")
 print("The student is not allowed to sit in the exam.")