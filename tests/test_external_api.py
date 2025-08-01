from unittest.mock import patch
from src import external_api
from dotenv import load_dotenv
import os


@patch('requests.get')
def test_currency_conversion_in_rub(mock_get, api_answer, api_input):
    api_key = os.getenv('API_KEY')
    headers = {
        "apikey": f"{api_key}"
    }
    mock_get.return_value.json.return_value = api_answer
    assert external_api.currency_conversion_in_rub(api_input)
    mock_get.assert_called_once_with(f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37', headers=headers)
