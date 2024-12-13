class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age 

    def print_person_name_and_age(self):
        print(f'Your good name is {self.name} and you are {self.age} years old!')

person=Person("salman",20)

person.print_person_name_and_age()