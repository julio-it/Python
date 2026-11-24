def main():
    expression = input("Expression: ").strip()
    x, y, z = expression.split()

    n1 = float(x)
    n2 = float(z)

    if y == "+":
        print(n1 + n2)
    elif y == "-":
        print(n1 - n2)
    elif y == "*":
        print(n1 * n2)
    elif y == "/":
        if n2 == 0:
            print("Error: Division by zero")
        else:
            print(n1 / n2)
main()
