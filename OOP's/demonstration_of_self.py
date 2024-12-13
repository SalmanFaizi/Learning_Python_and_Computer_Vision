class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age 
        print(id(self))

    def print_person_name_and_age(self):
        name="faizi" # this won't change the name because this has no access to the object 
        self.name="Zunnu" # But this can becuase this has access of the object of the class Person (like Pass by reference) 
        print(f'Your good name is {self.name} and you are {self.age} years old!')
        print(name)
        print(self.name)

person=Person("salman",20)

person.print_person_name_and_age()
print(id(person)) # the id of person object and id of self inside teh __init__ are same hence proved OBJECT HI SELF HAI