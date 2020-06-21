pos = -1
def binary(list,n):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (u + l) // 2
        if n == list[mid]:
            globals()['pos'] = mid
            return True
        else:
            if n < list[mid]:
                u = mid - 1
            else:
                l = mid + 1

    return False

list = [1,2,31,42,102,521,662,871,2009,4521]
n = 4587

if binary(list,n):
    print("no is found at",pos)

else:
    print("no is not found")