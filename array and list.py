exchange_rates = {
    "USD": 1.39,
    "EUR": 1.16,
    "JPY": 151.57,
    "CAD": 1.75,
    "AUD": 1.81
}
pounds = float(input("Enter the number of British pounds: "))
currency = input("Enter the currency to convert into (USD, EUR, JPY, CAD, AUD): ")
if currency in exchange_rates:
    exchange_rate = exchange_rates[currency]
    converted_amount = pounds * exchange_rate
    print(f"Exchange rate: 1 GBP = {exchange_rate} {currency}")
    print(f"{pounds} GBP = {converted_amount} {currency}")
else:
    print("Invalid currency.")