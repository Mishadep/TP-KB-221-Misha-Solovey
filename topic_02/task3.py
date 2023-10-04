import re

def calculator():
    while True:
        expression = input("Введіть вираз (або 'вийти' для завершення): ")
        
        if expression.lower() == 'вийти':
            print("До побачення!")
            break
        
        # Визначаємо регулярний вираз для вилучення чисел і операцій
        pattern = r'(\d+\.\d+|\d+|\+|\-|\*|\/)'
        tokens = re.findall(pattern, expression)
        
        try:
            if len(tokens) != 3:
                print("Невірний формат виразу")
                continue

            num1, operator, num2 = tokens

            if not num1.isdigit() or not num2.isdigit():
                print("Введені значення не є числами")
                continue

            num1 = float(num1)
            num2 = float(num2)

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Помилка: ділення на нуль")
                    continue
                result = num1 / num2
            else:
                print("Невідома операція")
                continue

            print(f"Результат: {result}")
        except Exception as e:
            print(f"Помилка: {e}")

if __name__ == "__main__":
    calculator()
