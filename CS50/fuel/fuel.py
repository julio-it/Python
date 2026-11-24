def main():
    user_input = input("Fraction: ")
    percentage = convert(user_input)
    print(gauge(percentage))

def convert(user_input):
    while True:
        try:
            x_str, y_str = user_input.split("/")
            x = int(x_str)
            y = int(y_str)

            if x < 0 or y <= 0 or x > y:
                raise ValueError

            return round((x / y) * 100)
        except (ValueError, ZeroDivisionError):
            user_input = input("Fraction: ")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
