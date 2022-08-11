'''User interaction module which accepts initials values and return desired output'''

from data_interactor import Validation


class Welcome:
    '''Accepting user details from the user and returning desired result for the entered details'''

    def __init__(self):
        print("Hello user")
        self.account_verification()

    def account_verification(self):
        '''Perform initial verfication'''

        monitor = 1
        while monitor == 1:
            monitor += 1
            try:
                input_account_number = int(input("Please enter your account number "))
                password = int(input("Input 4 digit pin code "))

                if len(str(input_account_number)) != 8 and len(str(password)) != 4 :
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
        '''Understanding user transaction and redirecting the info'''

        for repeat in range(10):

            try:
                transaction_token = int(input("Please provide an input, for Balance press 1, for withdrawal press 2, Deposit press 3 ,Exit transaction 4  "))

                if transaction_token == 1:

                    self.customer1.interactor(transaction_token)
                    print(self.customer1.output_return())

                elif transaction_token == 2:

                    self.customer1.interactor(transaction_token)
                    if self.customer1.output_return() is not None:
                        print(self.customer1.output_return())

                elif transaction_token == 3:

                    self.customer1.interactor(transaction_token)
                    if self.customer1.output_return() is not None:
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

        '''Displays the output'''

        display = self.customer1.output_return()
        print(display)

Welcome()
