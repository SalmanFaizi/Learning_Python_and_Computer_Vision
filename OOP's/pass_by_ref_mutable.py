# def change(l1):
#     l1.append(5)
#     print(l1)
#     print(id(l1))


# l=[1,2,3,4]
# print(id(l)) # this will have only 1,2,3,4
# print(l)
# change(l)
# print(l)# this will get changed

# This get's changed because list is a mutable object. to prevent this you should pass a copy of the original list


# PREVENT OVERRITING

def change(l1):
    l1.append(5)
    print(l1)
    print(id(l1))


l=[1,2,3,4]
print(id(l)) # this will have only 1,2,3,4
print(l)
change(l[:])
print(l)# this will get changed

# This get's changed because list is a mutable object. to prevent this you should pass a copy of the original list