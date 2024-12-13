class parent:
    def __init__(self,num):
        print("in paren't  constructor")
        self.__num=100

    def show_num(self):
        print(self.__num)

class child(parent):
    def show(self):
        print("Inside the child class show method")


obj=child(100)
obj.show()
obj.show_num()
