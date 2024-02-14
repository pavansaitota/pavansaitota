def get_student_info():
    student_number = input("Enter student number: ")
    student_name = input("Enter student name: ")
    marks = []
    for i in range(3):
        subject_mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(subject_mark)
    return student_number, student_name, marks

def calculate_average(marks):
    return sum(marks) / len(marks)

student_number, student_name, marks = get_student_info()
average_mark = calculate_average(marks)

print("\nStudent Information:")
print("Number:", student_number)
print("Name:", student_name)
print("Marks:", marks)
print("Average:", average_mark)

if average_mark >= 75:
    print("Result: Distinction")
elif average_mark >= 60:
    print("Result: First class")
elif average_mark >= 50:
    print("Result: Second class")
elif average_mark >= 35:
    print("Result: Third class")
else:
    print("Result: Fail")

