class GParent:
    def __init__(self,brand,price):
        print("In GParent constructor")
        self.brand=brand
        self.price=price
    def show(self):
        print("In Grand parent class")

class Parent():
    def __init__(self,brand,price):
        print("In Parent constructor")
        self.brand=brand
        self.price=price

    def show(self):
        print("in parent class")
        print(self.price)

# class Child(Parent,GParent):
#     def show_price(self):
#         print("In child class")
#         print(self.price)
        

class Child(GParent,Parent): #Order of inheritance matters here
    def show_price(self):
        print("In child class")
        print(self.price)


obj=Child("Toyata",1000000)
obj.show()  # the order of inheritance will decide which classes method to call (MRO(Method resolution order))
obj.show_price()
