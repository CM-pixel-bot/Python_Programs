import numpy as np
#creating a 1D Numpy array
array_1d = nd.array([1, 2, 3, 4, 5, 6])
print("1D Array:")
print(array_1d)

#Reshaping the 1D Array to 2*3 2D array
array_2d = array_1d.reshape(2, 3)
print("\nReshaped to 2D Array(2 * 3):")
print(array_2d)

#Acessing elements using indexing
print("\nElement at position(1, 2):",array_2d[1, 2])

#Modifying an element
array_2d[0, 1] = 10
print("\nModified Array (After changing element at position (0, 1) to 10):")
print(array_2d)

#Calculating the sum of array elements
array_sum = np.sum(array_2d)
print("\nSum of all elements in the array:", array_sum)

OUTPUT:
1D Array:
[1 2 3 4 5 6]

Reshaped to 2D Array(2 * 3):
[[1 2 3]
 [4 5 6]]

Element at position(1, 2): 6

Modified Array (After changing element at position (0, 1) to 10):
[[ 1 10  3]
 [ 4  5  6]]

Sum of all elements in the array: 29
