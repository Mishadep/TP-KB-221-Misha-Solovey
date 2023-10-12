# calc.py
from operations import Calculator

def main():
    calculator = Calculator()
    
    while True:
        print("Виберіть операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("5. Вихід")
        
        choice = input("Ваш вибір: ")
        
        if choice == '5':
            print("До побачення!")
            break
        
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
            
            if choice == '1':
                print(f"Результат: {calculator.add(num1, num2)}")
            elif choice == '2':
                print(f"Результат: {calculator.subtract(num1, num2)}")
            elif choice == '3':
                print(f"Результат: {calculator.multiply(num1, num2)}")
            elif choice == '4':
                print(f"Результат: {calculator.divide(num1, num2)}")
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
    