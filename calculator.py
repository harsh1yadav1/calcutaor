a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

op = input("Enter operation (+, -, *, /): ")

print("\n--- Result ---")

if op == "+":
    print(f"{a} + {b} = {a + b}")

elif op == "-":
    print(f"{a} - {b} = {a - b}")

elif op == "*":
    print(f"{a} * {b} = {a * b}")

elif op == "/":
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Division by zero is not allowed ❌")

else:
    print("Invalid operation ❌")