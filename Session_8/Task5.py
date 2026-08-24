#5.Build a simple shopping cart total calculator: Given a list of item prices from a Flipkart cart,
#  use a loop to sum the prices. If an item price is 0 (out of stock), skip it.
#  Stop adding items if the running total crosses ₹2000 using break, and print the final total.
# <br><br><em><strong>Constraint:</strong> Use both break and continue in your solution.</em>

item_price=[0,500,1000,1500,2000,2500]
sum=0
for  i in item_price:
        if i == 0:
            print("Out of stock")
            continue
        sum=sum+i
        if(sum>2000):  
                break
print(f"final total {sum}")
       