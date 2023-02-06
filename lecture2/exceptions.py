import sys

try:
    x = int(input("X: "))
    y = int(input("Y: "))
except ValueError:
    print("Invalid input.")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} is {result}")