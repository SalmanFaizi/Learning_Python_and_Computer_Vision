class GParent:
    def __init__(self,brand,price):
        print("In GParent constructor")
        self.brand=brand
        self.price=price

    def show(self):
        print("In Grand parent class method show")
        print(self.brand , self.price)

class Parent(GParent):

    def show_price(self):
        print("in parent class")
        print(self.price)

class Child(GParent):

    def show_price(self):
        print("In child class")
        print(self.price)
        print("goint to take control to parent class")
        super().show_price()


# both classes have acces to the GParent class

obj=Child("Toyata",1000000) 
obj.show()

obj_p=Parent("Hundai",1000)
obj_p.show()

