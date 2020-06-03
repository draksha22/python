X = int(input("Enter 1st number"))
Y = int(input("Enter 2nd number"))
Z = int(input("Enter 3rd number"))

if X > Y and X > Z:
    print("X is greatest")

elif Y > X and Y > Z:
    print("Y is greatest")

else:
    print("Z is greatest")


a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))
c = int(input("Enter 3rd number"))

print("Greatest number is" , max(a,b,c))