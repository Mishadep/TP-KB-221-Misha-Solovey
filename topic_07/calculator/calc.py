import os
from functions import Functions
from operations import Operations

if __name__ == "__main__":
    log_file_name = "calculator_log.txt"
    current_directory = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(current_directory, log_file_name)

    if not os.path.isfile(log_file_path):
        with open(log_file_path, "w") as log_file:
            log_file.write("Calculator Log:\n")

    print("Виберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")

    choice = input("Ваш вибір (1/2/3/4): ")

    if choice == "1":
        Operations.perform_addition(log_file_path)
    elif choice == "2":
        Operations.perform_subtraction(log_file_path)
    elif choice == "3":
        Operations.perform_multiplication(log_file_path)
    elif choice == "4":
        Operations.perform_division(log_file_path)
    else:
        print("Неправильний вибір операції")
