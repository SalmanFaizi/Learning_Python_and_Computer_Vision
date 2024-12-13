# class A:

#     def area(self,radius):
#         return 3.14 *radius * radius

#     def area(self,l,b):
#         return l* b
    

# obj=A()
# obj.area(10) # technically in python overloading doesn't exist




# class A:

#     def area(self,radius):
#         return 3.14 *radius * radius

#     def area(self,l,b): # this method overrides the previous one 
#         return l* b
    

# obj=A()
# print(obj.area(10,4) )# technically in python overloading doesn't exist




#  THIS CAN BE ACHIVED WITH A BIT OF LOGIC

class A:

    def area(self,l,b=0):
        if b==0:
            return 3.14 * l * l
        else:
            return l * b

    

obj=A()
print(obj.area(10) )# This has been achived by giving a parameter a default value

print(obj.area(10,4)) # even this would work

