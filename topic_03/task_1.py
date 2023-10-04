def dodavannya(x, y):
    return x + y

def vidnimannya(x, y):
    return x - y

def mnozhennya(x, y):
    return x * y

def dilennya(x, y):
    if y == 0:
        return "Помилка: Ділення на нуль"
    return x / y

while True:
    print("Виберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вийти")

    choice = input("Введіть номер операції: ")

    if choice == '5':
        print("Дякую за використання калькулятора. До побачення!")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Неправильний вибір операції. Спробуйте ще раз.")
        continue

    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    if choice == '1':
        print("Результат:", dodavannya(num1, num2))
    elif choice == '2':
        print("Результат:", vidnimannya(num1, num2))
    elif choice == '3':
        print("Результат:", mnozhennya(num1, num2))
    elif choice == '4':
        print("Результат:", dilennya(num1, num2))
