from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    """
    Converts the given amount from one currency to another currency
    using the exchange rate from the forex-python library.
    """
    # create an instance of the CurrencyRates class
    c = CurrencyRates()

    # get the exchange rate from the from_currency to the to_currency
    exchange_rate = c.get_rate(from_currency, to_currency)

    # calculate the converted amount
    converted_amount = amount * exchange_rate

    # return the converted amount rounded to 2 decimal places
    return round(converted_amount, 2)
amount = 100
from_currency = 'USD'
to_currency = 'EUR'

converted_amount = convert_currency(amount, from_currency, to_currency)

print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
