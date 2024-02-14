def find_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

max_number = find_max(number1, number2)
print("The biggest number is:", max_number)
