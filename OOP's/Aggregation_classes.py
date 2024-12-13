class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address #initializing the object as a reference variable so that we can use it's avialable method and variables 

    def edit_address(self,new_name,new_city,new_pin,new_state):
        self.name=new_name
        self.address.change_address(new_city,new_pin,new_state) # Aggregation and calling another class for doing operations related to Address
        print("Name & Address changed!!")



class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state

    def change_address(self,new_city,new_pin,new_state):
        self.city=new_city
        self.pincode=new_pin
        self.state=new_state



add=Address("kolkata",700084,"WB")
cust=Customer("salman","Male",add)
print("old name: ",cust.name)
print("old city: ",cust.address.city)

cust.edit_address("Zunnu","purnia",854315,"BH")
print("New name: ",cust.name)
print("new city: ",cust.address.city)

