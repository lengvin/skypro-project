import os
import requests
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv('API_KEY')
headers = {
    "apikey": f"{api_key}"
}


def currency_conversion_in_rub(operation):
    currency = operation['operationAmount']['currency']['code']
    amount = operation['operationAmount']['amount']

    if currency == 'RUB':
        return amount
    else:
        url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}'

        response = requests.get(url, headers=headers)
        response_data = response.json()
        result = response_data['result']

        return result
