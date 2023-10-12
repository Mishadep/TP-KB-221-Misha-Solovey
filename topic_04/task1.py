
def dodavannia(a, b):
    return a + b

def vidnimannia(a, b):
    return a - b

def mnozhennia(a, b):
    return a * b

def dilennia(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Помилка: ділення на нуль")

while True:
    try:
        operand1 = float(input("Введіть перше число: "))
        operator = input("Введіть операцію (+, -, *, /) або 'q' для виходу: ")

        if operator.lower() == 'q':
            break
        elif operator in ('+', '-', '*', '/'):
            operand2 = float(input("Введіть друге число: "))
            if operator == '+':
                result = dodavannia(operand1, operand2)
            elif operator == '-':
                result = vidnimannia(operand1, operand2)
            elif operator == '*':
                result = mnozhennia(operand1, operand2)
            elif operator == '/':
                try:
                    result = dilennia(operand1, operand2)
                except ValueError as e:
                    result = str(e)
            print("Результат:", result)
        else:
            print("Неправильна операція! Спробуйте ще раз.")
    except ValueError as e:
        print(f"Помилка: {e}. Спробуйте ще раз.")
    except ZeroDivisionError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Помилка: {e}")
