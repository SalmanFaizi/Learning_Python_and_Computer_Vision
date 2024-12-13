class Parent:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        
    def show_price(self):
        print("in parent class")
        print(self.price)

class Child(Parent):
    def show_price(self):
        print("In child class")
        print(self.price)


obj=Child("Toyata",1000000)
obj.show_price()