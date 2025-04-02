def temperature_converter():
    print("Temperature Converter")
    temp = float(input("Enter a temperature: "))
    
    print("Convert to:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter choice (1/2): ")
    
    if choice == '1':
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}°C is {fahrenheit}°F")
    elif choice == '2':
        celsius = (temp - 32) * 5/9
        print(f"{temp}°F is {celsius}°C")
    else:
        print("Invalid Input")

temperature_converter()

OUTPUT:
Temperature Converter
Enter a temperature: 5
Convert to:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
Enter choice (1/2): 1
5.0°C is 41.0°F

Temperature Converter
Enter a temperature: 6
Convert to:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
Enter choice (1/2): 2
6.0°F is -14.444444444444445°C
