# city="New York" # is a global variable can be accessed anywhere withing the program
# def change():
#     print(city) # can access the global variable

#     print("In change function")

# change()



# city="New York" # is a global variable can be accessed anywhere withing the program
# def change():
#     print(city) # can access the global variable
#     city="California" # but can't change the main variable

#     print("In change function the city is ",city)

# change()
# print(city)



# city="New York" # is a global variable can be accessed anywhere withing the program
# def change():
#     global city # changed the scope now we can change values
#     print(city) # can access the global variable
#     city="California" # but can't change the main variable

#     print("In change function the city is ",city)

# change()
# print(city)




city="New York" # is a global variable can be accessed anywhere withing the program
def change():

    city="California" # but can't change the main variable this will be city accessible to function change only (local scope)
    print(city) # can access the global variable

    print("In change function the city is ",city)

change()
print(city)
