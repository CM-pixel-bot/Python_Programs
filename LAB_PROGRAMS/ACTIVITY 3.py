def find_largest():
    print("Find the largest of five numbers")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    num4 = float(input("Enter fourth number: "))
    num5 = float(input("Enter fifth number: "))

    largest = max(num1, num2, num3, num4, num5)

    print(f"The largest number is: {largest}")

find_largest()

OUTPUT:
Find the largest of five numbers
Enter first number: 3
Enter second number: 4
Enter third number: 5
Enter fourth number: 6
Enter fifth number: 7
The largest number is: 7.0
