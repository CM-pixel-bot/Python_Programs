def list_operations():
    my_list = []
    while True:
        print("\nList Operations:")
        print("1. Insert an element")
        print("2. Delete an element")
        print("3. Find an element")
        print("4. Display the list")
        print("5. Exit")
        
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
5. Exit
Enter your choice: 1
Enter the element to insert: 4
Element '4' inserted.

List Operations:
1. Insert an element
2. Delete an element
3. Find an element
4. Display the list
5. Exit
Enter your choice: 2
Enter the element to delete: 4
Element '4' deleted.

List Operations:
1. Insert an element
2. Delete an element
3. Find an element
4. Display the list
5. Exit
Enter your choice: 3
Enter element to find: 2
Element '2' not found.

List Operations:
1. Insert an element
2. Delete an element
3. Find an element
4. Display the list
5. Exit
Enter your choice: 4
Current list: []

List Operations:
1. Insert an element
2. Delete an element
3. Find an element
4. Display the list
5. Exit
Enter your choice: 5
Exiting the program.

