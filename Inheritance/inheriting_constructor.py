class phone:
    def __init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price
        print("inside parent constructor")

class smartphone(phone):
    pass

obj=smartphone("samsung","black",12345)
print(obj.brand)