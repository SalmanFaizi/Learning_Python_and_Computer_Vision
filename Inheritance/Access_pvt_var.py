class Vehicle:
    def __init__(self,wheels,brand,secret_no):
        self.wheels=wheels
        self.brand=brand
        self.__secret_no=secret_no
    

class Car(Vehicle):
    def show_brand(self):
        print(self.brand)
    def access_pvt(self):
        print("pvt var",self.__secret_no) # you can't acces parent's private members
        # but self._Vehicle__secret_no will work

obj=Car(4,"Mahindra",1234) # if child doesn't have a constructor then parent's constructor initilizes the variables
obj.show_brand()
obj.access_pvt()
# print(obj.__secret_no)
# print(obj._Vehicle__secret_no)
