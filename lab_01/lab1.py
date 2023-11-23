students_list = [
    {"name": "Bob", "phone": "0631234567", "age": 20, "email": "bob@gmail.com"},
    {"name": "Emma", "phone": "0631234567", "age": 22, "email": "emma@gmail.com"},
    {"name": "Jon", "phone": "0631234567", "age": 21, "email": "jon@gmail.com"},
    {"name": "Zak", "phone": "0631234567", "age": 19, "email": "zak@gmail.com"}
]


def print_all_list():
    # Сортування
    sorted_students = sorted(students_list, key=lambda x: x["name"])  
    for student in sorted_students:
        str_for_print = f"Ім'я студента {student['name']}, Вік {student['age']}, Телефон {student['phone']}, Електронна пошта {student['email']}"
        print(str_for_print)
    print()


def add_new_element():
    # Додавання студентів
    name = input("Будь ласка, введіть ім'я студента: ")
    age = int(input("Будь ласка, введіть вік студента: "))
    phone = input("Будь ласка, введіть номер телефону студента: ")
    email = input("Будь ласка, введіть електронну пошту студента: ")
    new_student = {"name": name, "phone": phone, "age": age, "email": email}
    
    students_list.append(new_student)
    students_list.sort(key=lambda x: x["name"])  
    print("Новий елемент був доданий")
    print_all_list()


def delete_element():
    # Видалення студента 
    name = input("Будь ласка, введіть ім'я для видалення: ")
    delete_position = -1
    for student in students_list:
        if name == student["name"]:
            delete_position = students_list.index(student)
            break
    if delete_position == -1:
        print("Елемент не був знайдений")
    else:
        del students_list[delete_position]
        print("Елемент був видалений")
        print_all_list()


def update_element():
    # Оновлення існуючого студента
    name = input("Будь ласка, введіть ім'я для оновлення: ")
    for index, student in enumerate(students_list):
        if name == student["name"]:
            new_name = input("Введіть нове ім'я: ")
            new_age = int(input("Введіть новий вік: "))
            new_phone = input("Введіть новий телефон: ")
            new_email = input("Введіть нову електронну пошту: ")
            new_element = {"name": new_name, "age": new_age, "phone": new_phone, "email": new_email}

            del students_list[index]
            insert_position = 0
            for pos, elem in enumerate(students_list):
                if new_name > elem["name"]:
                    insert_position = pos + 1
                else:
                    break
            students_list.insert(insert_position, new_element)
            print("Елемент був оновлений")
            print_all_list()
            break
    else:
        print("Студент не знайдений")


def main():
    while True:
        # Дії для виконання
        choice = input("Будь ласка, вкажіть дію [C create, U update, D delete, P print, X exit]: ")
        if choice.upper() == "C":
            print("Буде створено новий елемент:")
            add_new_element()
        elif choice.upper() == "U":
            print("Буде оновлено існуючий елемент")
            update_element()
        elif choice.upper() == "D":
            print("Буде видалено елемент")
            delete_element()
        elif choice.upper() == "P":
            print("Список буде надруковано")
            print_all_list()
        elif choice.upper() == "X":
            print("Вихід")
            break
        else:
            print("Неправильний вибір")


main()
