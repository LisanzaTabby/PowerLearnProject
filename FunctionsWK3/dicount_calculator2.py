# Discount_calculator function that prompts a user for Original price and discount_percent and calculates the final_price based on the original price and discount_percent
def calculate_discount():
    price = int(input("Enter Original price of an item: "))
    discount_percent = float(input("Enter discount_percentage for the item(decimal format i.e. 0.2)& Zero if no discount: "))
    if discount_percent == 0:

        return price
    else:

        final_price = price + (price*discount_percent)
        return final_price
    
print(calculate_discount())