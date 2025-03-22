# Calculate_dicount function that takes an original price and calculates the discount on the price if its <=20% else should return the original price
def calculate_discount(price, discount_percent):
    if discount_percent >= 0.2:
        final_price= price + (price*discount_percent)
        return final_price
    else:
        return price
    
print(calculate_discount(30000, 0.2))#20% discount
print(calculate_discount(40000, 0.1))#10% discount is less than 20% returns the original price