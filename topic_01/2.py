text1 = "Привіт, "
text2 = "світ!"
result = text1 + text2
print(result)

#Розділення рядка на слова:
text = "Це приклад роботи зі словами"
words = text.split()
print(words)

#Заміна тексту
text = "Замініть слово"
new_text = text.replace("слово", "текст")
print(new_text)

#Перетворення на великі літери
text = "Великі літери"
uppercase_text = text.upper()
print(uppercase_text)

#Перетворення на маленькі літери:
text = "МАЛЕНЬКІ ЛІТЕРИ"
lowercase_text = text.lower()
print(lowercase_text)

#Перевірка, чи починається рядок з певного слова:
text = "Починається зі слова"
starts_with_word = text.startswith("Починається")
print(starts_with_word)

#Перевірка, чи закінчується рядок певним словом:
text = "Закінчується словом"
ends_with_word = text.endswith("словом")
print(ends_with_word)

#Пошук підрядка у тексті:
text = "Цей текст містить слово"
substring = "слово"
found = substring in text
print(found)

#Визначення довжини рядка:
text = "Ця стрічка має довжину"
length = len(text)
print(length)

#Вилучення пробілів з початку і кінця рядка:
text = "   З пробілами по обидва боки   "
trimmed_text = text.strip()
print(trimmed_text)

#Повторення рядка:
text = "Повторіть мене. "
repeated_text = text * 3
print(repeated_text)

#Форматування рядка:
name = "Михайло"
age = 18
formatted_text = f"Мене звуть {name} і мені {age} років."
print(formatted_text)

#Видалення символу з рядка:
text = "Видаліть 'цей' символ"
removed_char_text = text.replace("'", "")
print(removed_char_text)

#Перетворення числа в рядок:
number = 42
text = str(number)
print(text)

#Визначення позиції підрядка у тексті:
text = "Це слово знаходиться на позиції"
substring = "слово"
position = text.find(substring)
print(position)

#Перетворення рядка у список символів:
text = "Пробел"
char_list = list(text)
print(char_list)

#Переведення першої літери у велику:
text = "перша літера великою"
capitalized_text = text.capitalize()
print(capitalized_text)

#Розділення рядка на підрядки за роздільником:
text = "Розділіть рядок, використовуючи кому."
substrings = text.split(",")
print(substrings)

#Перевірка, чи складається рядок лише з букв:
text = "Тільки букви"
is_alpha = text.isalpha()
print(is_alpha)

#Перевірка, чи складається рядок лише з цифр:
text = "12345"
is_digit = text.isdigit()
print(is_digit)

#Перевірка, чи складається рядок лише з пробілів:
text = "     "
is_whitespace = text.isspace()
print(is_whitespace)


text = "42 is the answer"
starts_with_digit = text[0].isdigit()
print(starts_with_digit)

text = "Це слово зустрічається двічі в цьому реченні. Слово!"
substring = "слово"
count = text.count(substring)
print(count)

text = "3.14"
is_float = text.replace(".", "", 1).isdigit()
print(is_float)