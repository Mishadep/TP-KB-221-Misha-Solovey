import math

def quadratic_roots(a, b, c):
    # Розрахунок дискримінанту
    discriminant = b**2 - 4*a*c

    # Перевірка дискримінанту
    if discriminant > 0:
        # Два дійсних корені
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # Один дійсний корінь (корінь кратності 2)
        root = -b / (2*a)
        return root,
    else:
        # Коренів немає в дійсних числах
        return None

# Приклад використання функції
a = 1
b = -3
c = 2
roots = quadratic_roots(a, b, c)
if roots:
    print("Корені квадратного рівняння:", roots)
else:
    print("Корені відсутні в дійсних числах")