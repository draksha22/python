a = int(input("Enter first number"))
b = int(input("Enter second number"))

try:
    print("Resource Open")
    print(a / b)
    k = int(input("Enter a number"))

except ZeroDivisionError as e:
    print("Hey, you can't divide a no by 0",e)

except Exception as e:
    print("Something went wrong...",e)

except ValueError as e:
    print("Invalid Input!",e)

finally:
    print("Resource Closed")
