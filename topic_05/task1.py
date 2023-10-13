import random


def get_user_choice():
    user_choice = input("Оберіть камінь (к), ножиці (н) або папір (п): ")
    return user_choice


def get_computer_choice():
    choices = ['к', 'н', 'п']
    computer_choice = random.choice(choices)
    return computer_choice


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:  
        return "Нічия!"
    elif (user_choice == 'к' and computer_choice == 'н') or (user_choice == 'н' and computer_choice == 'п') or (user_choice == 'п' and computer_choice == 'к'):
       
        return "Ви перемогли!"
    else:
     
        return "Комп'ютер переміг!"


def main():
    user_choice = get_user_choice()  
    computer_choice = get_computer_choice() 
    print(f"Ви обрали: {user_choice}") 
    print(f"Комп'ютер обрав: {computer_choice}") 
    result = determine_winner(user_choice, computer_choice) 
    print(result) 


if __name__ == "__main__":
    main()  
