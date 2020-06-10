def count(list):
    even = 0
    odd = 0

    for i in list:
        if i%2 == 0:
            even += 1

        else:
            odd +=1

    return even,odd

list = [12,54,25,43,76,55,91,13,64,32]

even,odd = count(list)

print("even: {} and odd: {}".format(even,odd))