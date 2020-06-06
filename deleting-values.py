from array import *
arr = array('i',[])
n = int(input("enter the length of array"))
for i in range(n):
    x = int(input("enter a no"))
    arr.append(x)
    print(arr)

val=int(input("enter the index to be deleted"))
for e in range(n):
    if e==2:
        pass
    else:
        print(arr[e])
