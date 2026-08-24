def calculate_final_price(price,discount):
    final_price=price-(price*(discount/100))
    print(f"final price is : {final_price}")

def get_delivery_charge(amount,city):
    print('delivery charge: 50') if(city!='Ahmedabad' and city!='ahmedabad') else print('delivery charge : 0')

def format_price(price, currency='INR'):
    print(f"currency is {currency} : ₹{price}") if(currency=="INR") else print(f"currency is {currency} : ${price}")

def apply_coupon(price, coupon_code=None) :
    if(coupon_code=='ZOMATO10'):
       dis_price =price-(price* 10/100)
       return dis_price
    else:
        return price
     