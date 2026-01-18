print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
operation = input("Select an operation to perform:")

if operation == str(1):
    num1 = input("Enter first number: ")
    num2 = input ("Enter second number: ")
    print("The sum is " + str(int(num1)+ int(num2)))
elif operation == str(2): 
    num1 = input("Enter first number: ")
    num2 = input ("Enter second number: ")
    print("The difference is " + str(int(num1)-int(num2)))
elif operation == str(3):
    num1 = input("Enter first number: ")
    num2 = input ("Enter second number: ")
    print("The product is " + str(int(num1) * int(num2)))
elif operation == str(4):
    num1 = input("Enter first number: ")
    num2 = input ("Enter second number: ")
    print("The quotient is " + str(int(num1) / int (num2)))
else:
    print("Invalid Entry. Please try entering an integer 1-4 again")