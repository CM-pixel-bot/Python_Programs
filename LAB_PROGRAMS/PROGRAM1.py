def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Select operation:")
    print("1. Add")
    print("2. Divide")
    
    choice = input("Enter choice (1/2): ")  # Fixed the missing closing quote here
    
    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid Input")

calculator()


OUTPUT:
Simple Calculator
Enter first number: 6
Enter second number: 7
Select operation:
1. Add
2. Divide
Enter choice (1/2): 2
Result: 6.0 / 7.0 = 0.8571428571428571


Simple Calculator
Enter first number: 5
Enter second number: 6
Select operation:
1. Add
2. Divide
Enter choice (1/2): 1
Result: 5.0 + 6.0 = 11.0
