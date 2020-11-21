x = int(input("Unesi varijablu x: "))
y = int(input("Unesi varijablu y: "))
operation = input("Odaberi operaciju (+, -, *, /): ")
if operation == "+":
    print(x+y)
elif operation == "-":
    print(x-y)
elif operation == "*":
    print(x*y)
elif operation == "/":
    print(x/y)
else:
    print("Kriva operacija")
