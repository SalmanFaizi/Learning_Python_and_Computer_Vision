class Vehicle:
    def __init__(self,wheels):
        print("Inside parent's constructor ")
        self.wheels=wheels

    def show_wheels(self):
        print("Parent's show wheels method",self.wheels)
    

class Car(Vehicle):

    def __init__(self,wheels,brand,car_no):
        super().__init__(wheels) # super is used to initialize the parent's constructor also    
        print("Inside child's constructor")
        self.wheels=wheels
        self.brand=brand
        self.car_no=car_no

    def show_brand(self): # Example of method overriding 
        print("child's show_brand method",self.brand)


obj=Car(4,"BMW",1234) 
obj.show_brand()
print(obj.brand)
print(obj.wheels)
