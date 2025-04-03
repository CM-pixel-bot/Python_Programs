def list_operations():
    my_list = []
    while True:
        print("\nList Operations:")
        print("1. Insert an element")
        print("2. Delete an element")
        print("3. Find an element")
        print("4. Display the list")
        print("5. Sort the list")
        print("6. Reverse the list")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            element = input("Enter the element to insert: ")
            my_list.append(element)
            print(f"Element '{element}' inserted.")
        
        elif choice == 2:
            element = input("Enter the element to delete: ")
            if element in my_list:
                my_list.remove(element)
                print(f"Element '{element}' deleted.")
            else:
                print(f"Element '{element}' not found.")
        
        elif choice == 3:
            element = input("Enter element to find: ")
            if element in my_list:
                print(f"Element '{element}' found.")
            else:
                print(f"Element '{element}' not found.")
        
        elif choice == 4:
            print("Current list:", my_list)
        
        elif choice == 5:
            my_list.sort()
            print("List sorted:", my_list)

        elif choice == 6:
            my_list.reverse()
            print("List reversed:", my_list)
        
        elif choice == 7:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice, please try again.")

list_operations()


OUTPUT:
List Operations:
1. Insert an element
2. Delete an element
3. Find an element
4. Display the list
5. Sort the list
6. Reverse the list
7. Exit
Enter your choice: 4
Current list: []

List Operations:
1. Insert an element
2. Delete an element
3. Find an element
4. Display the list
5. Sort the list
6. Reverse the list
7. Exit
Enter your choice: 5
List sorted: []

List Operations:
1. Insert an element
2. Delete an element
3. Find an element
4. Display the list
5. Sort the list
6. Reverse the list
7. Exit
Enter your choice: 7
Exiting the program.

