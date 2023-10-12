try:
    number = int("не число")
except ValueError:
    print("Недійсне значення")

try:
    with open("non-existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Неіснуючий файл")

try:
    my_dict = {"name": "John"}
    value = my_dict["age"]
except KeyError:
    print("Значення ключа не існує в словнику")

try:
    my_list = [1, 2, 3]
    item = my_list[5]
except IndexError:
    print("Неіснуючий індекс")

try:
    result = "10" + 5
except TypeError:
    print("Аргумент невірного типу")

try:
    print(undefined_variable)
except NameError:
    print("Неіснюча змінна")

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Програму перервано користувачем")
