data = [{'name': 'John', 'grade': 75},
        {'name': 'Emily', 'grade': 76},
        {'name': 'Michael', 'grade': 88},
        {'name': 'David', 'grade': 21},
        {'name': 'Sophia', 'grade': 89},
        {'name': 'Oleg', 'grade': 90},
        {'name': 'Tate', 'grade': 75},
        {'name': 'Oliver', 'grade': 100}]

# Запитуємо параметри сортування від користувача
parameter = input("Виберіть ключ для сортування (name або grade): ")
reverse_sort = input("Сортувати від більшого до меншого (yes/no)? ").lower()

# Перевірка чи потрібно сортувати у зворотньому порядку
reverse = reverse_sort == 'yes'

# Функція для сортування
def sort_data(data, parameter, reverse):
    if parameter == 'name':
        return sorted(data, key=lambda x: x['name'], reverse=reverse)
    elif parameter == 'grade':
        return sorted(data, key=lambda x: x['grade'], reverse=reverse)
    else:
        print("Неправильний ключ сортування.")
        return data

# Виклик функції для сортування
sorted_data = sort_data(data, parameter, reverse)

# Виведення відсортованих даних
for item in sorted_data:
    print(f"Name: {item['name']}, Grade: {item['grade']}")
