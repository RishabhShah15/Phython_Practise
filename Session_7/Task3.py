total_amt=(float(input("Enter Flipkart cart total :")))

if(total_amt>2000):
    print('You get a 10%' +'discount')
elif(total_amt>1000):
    print("You get a 5 %"+"discount")
else:
    print('No discount available.')
