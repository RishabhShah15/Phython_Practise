#1.Define a function called calculate_final_price(price, discount_rate) that returns 
# the final price after applying the discount rate to the given price.
from calculate_price import calculate_final_price
price=float(input("Enter a Price :"))
discount=float(input("Discount Rate (%) :"))
final_price=0.0
calculate_final_price(price,discount) if(discount<=100) else  "not valid discount rate"


