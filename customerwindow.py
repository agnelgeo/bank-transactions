
from datainteractor import Validation


class Welcome:

    def __init__(self):
        print("Hello user")
        self.account_verification()

    def account_verification(self):
        quit = 1
        while quit == 1:
            quit += 1
            try:
                input_account_number = int(input("Please enter your account number "))
                password = int(input("Input 4 digit pin code "))

                if len(str(input_account_number)) != 8 and len(str(password)) != 4 :
                    if True:
                        print("invalid details")
                        break
                
                else:

                    input_values = [input_account_number,password]
                    self.customer1 = Validation()  
                    key = self.customer1.customer_find(input_values)

                    if key == 1:
                        self.response_mod()
                       
                    
            except ValueError:
            
                print("please enter a valid account number or pin")
                break
        
    
    def response_mod(self):
        for repeat in range(10):
            
            try:

                transaction_token = int(input("Please provide an input, for Balance press 1, for withdrawal press 2, Deposit press 3 ,Exit transaction 4  "))

                if transaction_token == 1:

                    self.customer1.interactor(transaction_token)
                    print(self.customer1.output_return())

                elif transaction_token == 2:

                    self.customer1.interactor(transaction_token)
                    if self.customer1.output_return() != None:
                        print(self.customer1.output_return())

                elif transaction_token == 3:

                    self.customer1.interactor(transaction_token)
                    if self.customer1.output_return() != None:
                        print(self.customer1.output_return())

                elif transaction_token == 4:
                    print("Thank you for banking with us")
                    break
                
                else:
                    print("please enter a valid input from 1, 2 ,3 or 4")

            except ValueError:
                print("Please enter a valid input")

            repeat += 1
        if transaction_token in range (0,3):
            self.display_ouput()


    def display_ouput(self):

        display = self.customer1.output_return()
        print(display)


    
Welcome()
            

   
