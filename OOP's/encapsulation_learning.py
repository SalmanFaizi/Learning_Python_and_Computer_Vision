class employee():
    def __init__(self):
        self.__employee_id=None
        self.employee_name=None
        self.__password=None

        self.menu()
    def menu(self):
        emp_input=input("""
                 Enter 0 to register
                 Enter 1 to login 
                 Enter 2 to logout
                 Enter 3 to resign
                 Enter 4 to submit your task
                 Enter 5 to give suggestion or feedback or compaints """)
        
        if emp_input=="1":
            self.login()

        if emp_input=="0":
            self.register()
    
    def register(self):
        print("Please enter your name,id and password")
        self.name=input("Enter name: ")
        self.__employee_id=int(input("Enter employee id: "))
        self.__password=input("Enter password: ")
        print("registration succesfull!")
        self.menu()

    def login(self):
        print("Enter your credentials to login")
        self.entered_id=int(input("Enter your emp id: "))
        self.entered_pass=input("Enter your password: ")
        if self.entered_id==self.__employee_id and self.entered_pass==self.__password:
            print("login successful!")
        self.menu()

# obj=employee()
# print(obj.name)
