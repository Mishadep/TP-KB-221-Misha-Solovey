def find_insert_position(sorted_list, new_element):
    left = 0
    right = len(sorted_list) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if sorted_list[mid] == new_element:
            # Якщо елемент вже є в списку, повертаємо його позицію
            return mid
        elif sorted_list[mid] < new_element:
            # Якщо новий елемент більший за поточний середній елемент,
            # зміщуємо ліву границю пошуку
            left = mid + 1
        else:
            # Якщо новий елемент менший, зміщуємо праву границю
            right = mid - 1
    
    # Після завершення циклу, left показує на позицію, де потрібно вставити новий елемент
    return left

# Приклад використання:
my_list = [1, 3, 5, 7, 9]
new_element = 6
position = find_insert_position(my_list, new_element)
print(f"Позиція для вставки {new_element}: {position}")
