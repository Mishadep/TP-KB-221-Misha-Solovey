# Функція для додавання двох чисел
def add(x, y):
    return x + y

# Функція для віднімання двох чисел
def subtract(x, y):
    return x - y

# Функція для множення двох чисел
def multiply(x, y):
    return x * y

# Функція для ділення двох чисел
def divide(x, y):
    if y == 0:
        return "Помилка: ділення на нуль"
    return x / y

while True:
    # Виведення опцій для користувача
    print("Оберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вихід")

    # Отримання вибору користувача
    choice = input("Введіть номер операції (1/2/3/4/5): ")

    # Перевірка чи введено правильний номер операції
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        if choice == '1':
            print("Результат:", add(num1, num2))

        elif choice == '2':
            print("Результат:", subtract(num1, num2))

        elif choice == '3':
            print("Результат:", multiply(num1, num2))

        elif choice == '4':
            print("Результат:", divide(num1, num2))
    elif choice == '5':
        print("Дякую за використання калькулятора!")
        break
    else:
        print("Неправильний вибір операції. Будь ласка, виберіть знову.")

        #update