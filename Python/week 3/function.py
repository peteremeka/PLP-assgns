# FUNCTION TO CALCULATE PRICE DISCOUNT
price = int(input("Enter Price : "))
discount = int(input("Enter Price Discount : "))

discount_percent = discount / 100

def calculate_discount(price, discount_percent):
    if discount_percent >= 0.2:
        discount_price = price * discount_percent
        price_after_dicount = price - discount_price
        return int(price_after_dicount)
    else:
        return int(price)

print(f"{calculate_discount(price, discount_percent)}")