def temperature_converter():
    print("Temperature Converter")
    temp = float(input("Enter a temperature: "))
    
    print("Select the current unit of temperature:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    
    choice = input("Enter choice (1/2/3): ")
    
    if choice == '1':
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
        print(f"{temp}°C is {fahrenheit}°F and {kelvin}K")
    elif choice == '2':
        celsius = (temp - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{temp}°F is {celsius}°C and {kelvin}K")
    elif choice == '3':
        celsius = temp - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{temp}K is {celsius}°C and {fahrenheit}°F")
    else:
        print("Invalid Input")

temperature_converter()


OUTPUT:
Temperature Converter
Enter a temperature: 54
Select the current unit of temperature:
1. Celsius
2. Fahrenheit
3. Kelvin
Enter choice (1/2/3): 3
54.0K is -219.14999999999998°C and -362.46999999999997°F
