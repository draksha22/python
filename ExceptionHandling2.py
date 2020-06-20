a = int(input("Enter first number"))
b = int(input("Enter second number"))

try:
    print("Resource Open")
    print(a / b)

except Exception as e:
    print("Hey, you can't divide a number by zero",e)

finally:
    print("Resource Closed")

