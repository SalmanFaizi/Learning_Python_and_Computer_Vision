# class learn():
#     def __init__(self,name):
#         self.name=name
#         print(self.name)

# obj=learn("salman")
# print(obj.name) #simple passed name "salman" will be printed

# class learn():
#     def __init__(self,name):
#         self.name=name
#         # print(self.name)


# def test(obj_cpy):
#     print(obj_cpy.name) # "salman" will be printed
#     print(id(obj_cpy)) # both objects has the same attribute and location because it's pass by reference

# obj=learn("salman")
# print(obj.name)
# print(id(obj))

# test(obj)


class learn():
    def __init__(self,name):
        self.name=name
        # print(self.name)


def test(obj_cpy):
    print(obj_cpy.name) # "salman" will be printed
    obj_cpy.name="zunnu"
    print(id(obj_cpy)) # both objects has the same attribute and location because it's pass by reference
    print(obj_cpy.name)
obj=learn("salman")
print(obj.name)
print(id(obj))

test(obj)

print(obj.name) # obj.name will be changed 