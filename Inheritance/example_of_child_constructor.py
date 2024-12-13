class parent:
    def __init__(self,num):
        print("in paren't  constructor")
        self.__num=100

    def get_num(self):
        print(self.__num) # this will result in an error because this has never been initilized

class child(parent):
    def __init__(self,var,num):
        self.__var=var
    def get_var(self):
        print("Inside the child class show method",self.__var)


obj=child(100,10)
obj.get_var()
obj.get_num()
