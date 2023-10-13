import requests

def get_exchange_rate(currency_code):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&json"
    response = requests.get(url)
    response.raise_for_status()  # Проверка статуса ответа

    data = response.json()
    if data and isinstance(data, list) and len(data) > 0:
        return data[0]["rate"]
    else:
        raise Exception("Помилка отримання курсу валюти")

def convert_currency(amount, currency_code):
    try:
        rate = get_exchange_rate(currency_code)
        converted_amount = amount * rate
        return converted_amount
    except requests.exceptions.RequestException as e:
        return f"Помилка: Немає з'єднання з сервером. Перевірте підключення до Інтернету."
    except (KeyError, IndexError):
        return f"Помилка: Невірний формат відповіді сервера."
    except Exception as e:
        return f"Помилка: {e}"

while True:
    try:
        amount = float(input("Введіть суму: "))
        currency_code = input("Введіть код валюти (EUR, USD, PLN): ").upper()

        if currency_code in ["EUR", "USD", "PLN"]:
            result = convert_currency(amount, currency_code)
            print(f"{amount} {currency_code} = {result:.2f} UAH")
        else:
            print("Непідтримуваний код валюти. Спробуйте ще раз.")
    except ValueError:
        print("Помилка: введіть коректну суму.")
    except Exception as e:
        print(f"Помилка: {e}")

    another_conversion = input("Бажаєте конвертувати іншу валюту (так/ні)? ").lower()
    if another_conversion != "так":
        break
