# operations.py
from functions import Functions

class Operations:
    @staticmethod
    def get_numbers():
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        return a, b

    @staticmethod
    def log_action(action, data, result, log_file_path):
        with open(log_file_path, "a") as log_file:
            log_entry = f"Action: {action}, Data: {data}, Result: {result}\n"
            log_file.write(log_entry)

    @staticmethod
    def perform_addition(log_file_path):
        a, b = Operations.get_numbers()
        result = Functions.add(a, b)
        Operations.log_action("Addition", f"{a} + {b}", result, log_file_path)
        print("Результат додавання:", result)

    @staticmethod
    def perform_subtraction(log_file_path):
        a, b = Operations.get_numbers()
        result = Functions.subtract(a, b)
        Operations.log_action("Subtraction", f"{a} - {b}", result, log_file_path)
        print("Результат віднімання:", result)

    @staticmethod
    def perform_multiplication(log_file_path):
        a, b = Operations.get_numbers()
        result = Functions.multiply(a, b)
        Operations.log_action("Multiplication", f"{a} * {b}", result, log_file_path)
        print("Результат множення:", result)

    @staticmethod
    def perform_division(log_file_path):
        a, b = Operations.get_numbers()
        result = Functions.divide(a, b)
        Operations.log_action("Division", f"{a} / {b}", result, log_file_path)
        print("Результат ділення:", result)
