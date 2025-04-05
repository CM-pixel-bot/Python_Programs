import numpy as np

array = np.random.randint(1, 21, size=(3, 3))
print("Original Array:\n", array)

mean_val = np.mean(array)
print("\nMean of the array:", mean_val)

array[array < 10] = 0
print("\nModified Array (elements < 10 replaced with 0):\n", array)

OUTPUT:
Original Array:
[[15  3 19]
 [ 7 10 12]
 [ 1 14  8]]

Mean of the array: 9.88888888888889

Modified Array (elements < 10 replaced with 0):
[[15  0 19]
 [ 0 10 12]
 [ 0 14  0]]
