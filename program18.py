Program 1:
n = int(input("Enter the numbers:"))
for i in range(1, n+1):
	print(" " * (n - i) + "*" * (2 * i - 1))

Program 2:
n = int(input("Enter the numbers:"))
for i in range(n -1,0, -1):
	print(" " * (n - i) + "*" * (2 * i - 1))
  
