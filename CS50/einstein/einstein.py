def main():
    mass = int(input("Enter the mass: "))
    energy = calculate(mass)
    print(f"The energy is: {energy}")

def calculate(m):
    c = 300000000
    return m * (c ** 2)

if __name__ == "__main__":
    main()
