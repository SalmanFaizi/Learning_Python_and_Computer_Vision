class phone:
    def __init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price
        print("inside parent constructor")

    def show_brand(self):
        print("inside parent's show_brand method")

        print(self.brand)

class smartphone(phone):
    def show_brand(self):
        print("inside child's show method ")

smartphone("samsung","black",12345).show_brand()