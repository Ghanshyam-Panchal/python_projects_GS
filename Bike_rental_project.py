# Display available bikes
# Request a bike for rent(100->1qty)
# exit

class bikeShop:
    def __init__(self,stock)
        self.stock=stock
    def displayBike(self):
        print ("Total Bike",self.stock)
    def rentForBike(self,q):

        if q<=0:
            print("Enter the positive value or greater then zero")  
        elif q>self.stock:
            print("Enter the value(less then stock)") 
        else:
            print("Total price",q*100)
            print("Total Bikes",self.stock)

while True:
    obj=bikeShop(100)
    uc=int(input('''
1 Display Stock
2 Rent a bikeShop
3 Exit
'''))

if uc==1:
    obj.displayBike()
elif uc==2:
    n=int(input("Enter the Quantiyt:---"))
    obj,rentForBike(n)
else:
    break


