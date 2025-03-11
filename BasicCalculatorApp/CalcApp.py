# Basic Calculator App taking input from the user
number1 = int(input("Please Enter Number 1:"))
number2 = int(input("Please Enter Number 2:"))
operation = input("Enter operation(+,/,*,or-):")

if operation == "+":
    result = number1 + number2
elif operation == "/":

    if number2 == 0:
        print("Error: Divisor can't be Zero(0)")
        result = None
    else:
        result = number1 / number2
        
elif operation == "*":
    result = number1 * number2
elif operation == "-":
    result = number1 - number2
else:
    print("Please Enter the correct operation as in the brackets!")

print(result)
