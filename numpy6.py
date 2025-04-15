import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
#1
arr1=np.arange(2,11).reshape(3,3)
print(arr1)
#2
reversed_arr = arr[::-1]
print("Original array:", arr)
print("Reversed array:", reversed_arr)
#3
a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([3, 4, 6, 7])

result = np.isin(a1, a2)

print("Array 1:", a1)
print("Array 2:", a2)
print("Presence in Array2:",result)