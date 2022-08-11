'''Deposit calculation module'''

class DepositTransaction:
    '''Deposit calculation module'''

    def __init__(self,data,input_account_number):

        self.data = data
        self.input_account_number = input_account_number
        self.new_balance = None

    def deposit_amount(self):
        '''Accepting deposit amount and calculating new balance'''

        deposit_amount = float(input("Please enter the amount to deposit "))
        for customer_id in range(len(self.data['people'])):

            if self.input_account_number == self.data['people'][customer_id]['account_number']  :

                if deposit_amount > 0:

                    balance =float(self.data['people'][customer_id]['balance'])
                    new_balance = balance + deposit_amount
                    deposit_response = (f"Hi { self.data['people'][customer_id]['name']} you have deposited {deposit_amount} balance is {new_balance}")
                    self.new_balance = new_balance
                    self.deposit_returns()

                    return deposit_response

                else:
                    print("Please enter a positive value")

    def deposit_returns(self):
        '''Returning the new balance'''

        return_new_balance = self.new_balance
        return return_new_balance
        