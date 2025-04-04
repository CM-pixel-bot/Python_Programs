
dict1 = eval(input("Enter first dictionary: "))
dict2 = eval(input("Enter second dictionary: "))


merged = dict1.copy()
for key, value in dict2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value


print("Merged dictionary:", merged)

OUTPUT:
Enter first dictionary: {'a': 10, 'b': 20}
Enter second dictionary: {'b': 5, 'c': 30}
Merged dictionary: {'a': 10, 'b': 25, 'c': 30}

