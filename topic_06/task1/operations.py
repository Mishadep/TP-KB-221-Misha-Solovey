from functions import add, subtract, multiply, divide

def get_numbers():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    return a, b

def log_action(action, data, result, log_file_path):
    with open(log_file_path, "a") as log_file:
        log_entry = f"Action: {action}, Data: {data}, Result: {result}\n"
        log_file.write(log_entry)

def perform_addition(log_file_path):
    a, b = get_numbers()
    result = add(a, b)
    log_action("Addition", f"{a} + {b}", result, log_file_path)
    print("Результат додавання:", result)

def perform_subtraction(log_file_path):
    a, b = get_numbers()
    result = subtract(a, b)
    log_action("Subtraction", f"{a} - {b}", result, log_file_path)
    print("Результат віднімання:", result)

def perform_multiplication(log_file_path):
    a, b = get_numbers()
    result = multiply(a, b)
    log_action("Multiplication", f"{a} * {b}", result, log_file_path)
    print("Результат множення:", result)

def perform_division(log_file_path):
    a, b = get_numbers()
    result = divide(a, b)
    log_action("Division", f"{a} / {b}", result, log_file_path)
    print("Результат ділення:", result)