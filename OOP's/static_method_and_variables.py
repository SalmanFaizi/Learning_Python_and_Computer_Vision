class GreetClass:
    # @staticvariable
    __counter=0
    def __init__(self,name):
        self.name=name
        self.greet()
        GreetClass.__counter=GreetClass.__counter+1

    def greet(self):
        print("Good morning",self.name)
        # print(GreetClass.__counter)
    @staticmethod
    def get_counter():
        return GreetClass.__counter
    @staticmethod
    def set_counter(new_count):
        if type(new_count)==int:
            GreetClass.__counter=new_count
        else:
            print("Type Not Alllowed!")
            


