class GParent:
    def __init__(self,brand,price):
        print("In GParent constructor")
        self.brand=brand
        self.price=price
    def show(self):
        print("In Grand parent class")

class Parent(GParent):

        
    def show_price(self):
        print("in parent class")
        print(self.price)

class Child(Parent):
    def show_price(self):
        print("In child class")
        print(self.price)
        print("goint to take control to parent class")
        super().show_price()


obj=Child("Toyata",1000000)
obj.show_price() # child class method
obj.show() # GParent class method

obj_p=Parent("Hundai",10000)
obj_p.show()
