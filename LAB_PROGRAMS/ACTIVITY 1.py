def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Floor Division")
    
    choice = input("Enter choice (1/2/3/4/5/6/7): ")
    
    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error! Division by zero.")
    elif choice == '5':
        if num2 != 0:
            print(f"Result: {num1} % {num2} = {num1 % num2}")
        else:
            print("Error! Modulus by zero.")
    elif choice == '6':
        print(f"Result: {num1} ** {num2} = {num1 ** num2}")
    elif choice == '7':
        if num2 != 0:
            print(f"Result: {num1} // {num2} = {num1 // num2}")
        else:
            print("Error! Floor division by zero.")
    else:
        print("Invalid Input")

calculator()


OUTPUT:
Simple Calculator
Enter first number: 3
Enter second number: 4
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Modulus
6. Exponentiation
7. Floor Division
Enter choice (1/2/3/4/5/6/7): 6
Result: 3.0 ** 4.0 = 81.0
