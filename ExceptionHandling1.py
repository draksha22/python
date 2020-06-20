a = int(input("Enter first number"))
b = int(input("Enter second number"))

try:
    print(a / b)

except Exception:
    print("Hey, you can't divide a no by zero")

print("Bye!")