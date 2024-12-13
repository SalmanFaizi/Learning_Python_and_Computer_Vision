def print_name(name): # this is a function takes arguments
    print(f'Your name is {name}.')


print_name("salman")  # functions usually called like this with it's neccesary arguments


class PrintName():
    def __init__(self,name):
        self.name=name 
    def print_my_name(self):
        print(f'Hey!! Your good name is {self.name}')

obj=PrintName("salman")
obj.print_my_name()