def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Wybierz operacje: ")

    if choice in ('1', '2', '3', '4'):
        number1 = float(input("Podaj pierwsza liczbe: "))
        number2 = float(input("Podaj druga liczbe: "))

        if choice == '1':
            print(number1, "+", number2, "=", add(number1, number2))

        elif choice == '2':
            print(number1, "-", number2, "=", subtract(number1, number2))

        elif choice == '3':
            print(number1, "*", number2, "=", multiply(number1, number2))

        elif choice == '4':
            print(number1, "/", number2, "=", divide(number1, number2))

        else:
            print("Podaj poprawna liczbe")

        ask = input("Czy chcesz cos jeszcze obliczyc? (T/N) ")
        if ask == "N" or "n":
            break
