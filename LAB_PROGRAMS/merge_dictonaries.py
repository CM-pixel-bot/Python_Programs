dict = eval(input("Enter first dictionary: "))
dict2 = eval(input("Enter second dictionary: "))


merged_dict = {**dict1, **dict2}


print("Merged dictionary:", merged_dict)

OUTPUT:
Enter first dictionary: {'a': 1, 'b': 2}
Enter second dictionary: {'c': 3, 'd': 4}
Merged dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
