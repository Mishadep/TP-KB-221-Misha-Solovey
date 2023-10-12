def calculator(operator, num1, num2):
    match operator:
        case '+':
            result = num1 + num2
            print(f'{num1} + {num2} = {result}')
        case '-':
            result = num1 - num2
            print(f'{num1} - {num2} = {result}')
        case '*':
            result = num1 * num2
            print(f'{num1} * {num2} = {result}')
        case '/':
            if num2 != 0:
                result = num1 / num2
                print(f'{num1} / {num2} = {result}')
            else:
                print("Ділення на нуль недопустиме.")
        case _:
            print("Невідома операція")

# Зчитуємо вхідні дані від користувача
operator = input("Введіть операцію (+, -, *, /): ")
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

# Викликаємо функцію калькулятора
calculator(operator, num1, num2)