operation = int(input("Options:-\n1-Addition\n2-Substraction\n3-Multiplication\n4-Division\n5-Power\nEnter the option number you choosed - "))
if operation == 1: # Adds two numbers
     a = int(input("Enter the first number: "))
     b = int(input("Enter the second number: "))
     print(a + b, " is the result.")
elif operation == 2: # Subtracts two numbers
     a = int(input("Enter the first number: "))
     b = int(input("Enter the second number: "))
     print(a - b, "is the result.")
elif operation == 3: # Multiplies two numbers
     a = int(input("Enter the first number: "))
     b = int(input("Enter the second number: "))
     print(a * b, " is the result.")
elif operation == 4: # Divides two number
     a = int(input("Enter the first number: "))
     b = int(input("Enter the second number: "))
     print(a / b, " is the result.")
else: # Gives power(square) of a number
     a = int(input("Enter the first number: "))
     print(a * a, " is the result.")
