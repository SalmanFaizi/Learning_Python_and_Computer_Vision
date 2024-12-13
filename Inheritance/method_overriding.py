class Vehicle:
    def __init__(self,wheels,brand,secret_no):
        print("Inside parent's constructor ")
        self.wheels=wheels
        self.brand=brand
        self.__secret_no=secret_no

    def show_brand(self):
        print("Parent's show brand method",self.brand)
    

class Car(Vehicle):
    # super().show_brand()

    def show_brand(self): # Example of method overriding 
        super().show_brand() # super is used to call parent's class same method
        # obj.show_brand()
        print("child's show_brand method",self.brand)

obj=Car(4,"Mahindra",1234) 
obj.show_brand()
