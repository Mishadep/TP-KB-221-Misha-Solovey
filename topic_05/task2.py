import requests

def get_exchange_rate(currency_code):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&json"
    response = requests.get(url)
    data = response.json()
    if data:
        return data[0]["rate"]
    else:
        raise Exception("Помилка отримання курсу валюти")

def convert_currency(amount, currency_code):
    try:
        rate = get_exchange_rate(currency_code)
        converted_amount = amount * rate
        return converted_amount
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