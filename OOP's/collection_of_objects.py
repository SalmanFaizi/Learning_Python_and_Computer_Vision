class GreetClass:
    def __init__(self,name):
        self.name=name

    def greet(self):
        print("Good morning",self.name)

G1=GreetClass("Salman")
G2=GreetClass("Faizi")
G3=GreetClass("ayub")

L_G=[G1,G2,G3]

for Greet_obj in L_G:
    Greet_obj.greet()

