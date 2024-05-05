t = int(input("Options:-\n 1-Addition\n 2-Substraction\n 3-Multiplication\n 4-Division\n 5-Power\n Enter the option number you choosed - "))
if t == 1:
     a = int(input("Enter the first number: "))
     b = int(input("Enter the second number: "))
     print(a + b, " is the result.")
elif t == 2:
     a = int(input("Enter the first number: "))
     b = int(input("Enter the second number: "))
     print(a - b, "is the result.")
elif t == 3:
     a = int(input("Enter the first number: "))
     b = int(input("Enter the second number: "))
     print(a * b, " is the result.")
elif t == 4:
     a = int(input("Enter the first number: "))
     b = int(input("Enter the second number: "))
     print(a / b, " is the result.")
     # some issue in this part(power) so i'll try to solve that
else:
     a = int(input("Enter the first number: "))
     b = int(input("Enter the second number: "))
     print(a ** b, " is the result.")
