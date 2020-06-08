from numpy import *

arr = array([
    [1,2,3,4,5,6],
    [5,4,3,6,2,1]
])

arr1 = arr.flatten()
print(arr1)

arr2 = arr1.reshape(3,4)
print(arr2)

arr3 = arr2.flatten()
print(arr3)

arr4 = arr3.reshape(2,2,3)
print(arr4)