pos = -1
def search(list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1

    return False


list = [1,21,35,43,5]
n = 43

if search(list,n):
    print("number is found", pos+1)
else:
    print("number is not in the list")



