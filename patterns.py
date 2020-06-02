i = 1
while i < 5:
    print("#" , end = "")
    j = 1
    while j <= 4:
        print("#",end = "")
        j += 1
    i += 1
    print()



for i in range(4):
    for j in range(6):
        print("*", end="")

    print()


for i in range(5):
    for j in range(i+1):
        print("#" , end="")

    print()


for i in range(5):
    for j in range(5-i):
        print("*", end="")

    print()



for i in range(4):
    for j in range(4-i):
        print(i+j+1, end="")

    print()

