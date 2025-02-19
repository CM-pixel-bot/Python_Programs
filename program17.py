#get the user input 
num = int(input("Enter a number:"))
#print the multiplication table
print(f"Multiplication Table of {num}:")
for i in range(1, 11):#loop from1 to 10
    print(f"{num} x {i} = {num * i}")
