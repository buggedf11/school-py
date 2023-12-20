def calculate_vat(price):
    vat_rate = 0.2
    vat = price * vat_rate
    return vat

price = float(input("Enter the price of the item: "))
vat = calculate_vat(price)
print(f"The VAT for the item is {vat:.2f}")
