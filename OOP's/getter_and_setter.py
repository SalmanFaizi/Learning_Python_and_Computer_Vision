class Atm():
    def __init__(self):
        self.__pin=""
        self.__amount=0
        self.number=9502250076
        self.__user_key="salman"

        self.show_menu()

    def show_menu(self):
        User_input=input("""
                Press 1 for creating pin. 
                Press 2 for reseting pin.
                Press 3 for withdrawl. 
                Press 4 for deposit. 
                Press 5 for checking the balance. 
                Press 6 for exit.
                Please enter your choice...
        """)
        if User_input=="1":
            self.create_pin()



        if User_input=="2":
            self.reset_pin()

        
        if User_input=="3":
            self.withdraw()

        if User_input=="4":
            self.deposit()


        if User_input=="5":
            self.check_balance()


        if User_input=="6":
            text=self.exit_call_sal()
            print(text)

    def create_pin(self):
        self.entered_number=int(input("Enter your phone number"))
        self.secret_key=input("Enter secret key to change pin.")
        if self.entered_number==self.number and self.secret_key==self.__user_key:
            self.new_pin=input("Enter new pin")
            self.__pin=self.new_pin
            print("Pin set succesfully!!")
            self.show_menu()
        else:
            print("Please check your secret key or number and try again ...or press 1 to go main menu")
            self.input_user=input("Enter your choice")
            if self.input_user=="1":
                self.show_menu()
            else:
                self.create_pin()


    def reset_pin(self):
    
        self.new_secret_key=input("Enter your secret key..")
        if self.new_secret_key==self.__user_key:
            self.new_pin=input("Set your new pin please")
            self.__pin=self.new_pin
            print("Pin set succesfully!!")
            self.show_menu()

        else:
            print("Wrong secret key entered, please try again by pressing 5 !! or press 2 to create your new pin")
            self.input_user=input("Press 1 to go to main menu or 2 to create your pin.")
            if self.input_user=="1":
                self.show_menu()
            elif self.input_user=="2":
                self.create_pin()
            elif self.input_user=="5":
                self.reset_pin()
            else:
                print("Oops!! Try again...")

    def withdraw(self):
        self.entered_pin=input("Enter your pin..")
        if self.entered_pin==self.__pin:
            self.want_amount=int(input("Enter the amount to withdraw..."))
            if self.__pin and self.want_amount<self.__amount :
                self.__amount=self.__amount-self.want_amount
                print("Withdraw succesfull!!")
                self.show_menu()
            else:
                print("Insufficient funds,Enter the amount less than avialable balance , would you like to go to main menu or try again")
                input_user=input("Press 1 to return to main menu...or 2 to try again")
                if input_user=="1":
                    self.show_menu()
                elif input_user=="2":
                    self.withdraw()
                else:
                    print("try again later....!!")
                

        else:
            print("Wrong pin entered")
            input_user=input("Press 1 to return to main menu...or 2 to try again")
            if input_user=="1":
                self.show_menu()
            elif input_user=="2":
                self.withdraw()
            else:
                print("try again later....!!")
        
    
    def deposit(self):
        self.entered_pin=input("Enter your pin..")
        if self.entered_pin==self.__pin:
            self.deposit_amount=int(input("Enter the amount to deposit..."))
            if self.__pin and self.deposit_amount>0:
                self.__amount=self.__amount+self.deposit_amount
                print("Deposit succesfull!!")
                self.show_menu()

        else:
            print("Wrong pin entered or deposit amount must be greater than zero")
            input_user=input("Press 1 to return to main menu...or 2 to try again")
            if input_user=="1":
                self.show_menu()
            elif input_user=="2":
                self.deposit()
            else:
                print("try again later....!!")



    def check_balance(self):
        self.entered_pin=input("Enter your pin please")
        if self.entered_pin==self.__pin:
            print("Your account balance is: ",self.__amount)
            self.show_menu()

        else:
            print("Please check your pin and try again...")
            self.input_user=input("Enter 1 to go to main menu or 2 to try again..")
            if self.input_user=="1":
                self.show_menu()
            elif self.input_user=="2":
                self.check_balance()
            else:
                print("Oops!! Try again later..")

        
    def exit_call_sal(self):
        text="Thank you!! Visit Again."
        return text

    def get_pin(self):
        return self.__pin

    def set_pin(self,new_pin):
        self.__pin=new_pin
        print("pin changed!")



