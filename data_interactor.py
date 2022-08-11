'''Data analysis and output return'''
import json

from balance import BalanceTransaction
from deposit import DepositTransaction
from withdrawal import WithdrawalTransaction

class Validation:
    ''' This class is for initial validation and returning output to customer_window module'''

    def __init__(self):
        try:
            with open('bank_details.json',mode='r', encoding='utf-8') as file:
                self.data=json.load(file)
        finally:
            file.close()
        self.input_account_number = None
        self.input_password = None
        self.output_value = None
        self.key =None
        self.customer_withdrawal = None
        self.customer_deposit = None

    def customer_find(self,input_values):
        '''Finding and matching customer'''
        try:

            self.input_account_number = input_values[0]
            self.input_password = input_values[1]
            input_flag = 0
            for customer_id in range(len(self.data['people'])):
                if self.input_account_number == self.data['people'][customer_id]['account_number'] and self.input_password == self.data['people'][customer_id]['password']:
                    print(f"Hello {self.data['people'][customer_id]['name']}")
                    input_flag = 1
                    return input_flag
            if input_flag == 0:
                print("Please enter a valid input 000")

        except ValueError:
            print("Please try again and enter valid inputs")



    def interactor(self,transaction_token):
        '''acccepting transaction type,assigning and returning output '''

        self.key = transaction_token

        if transaction_token == 1:
            data = self.data
            input_account_number = self.input_account_number
            customer_balance = BalanceTransaction(data,input_account_number)
            self.output_value = customer_balance.balance_determine()
            self.output_return()

        elif transaction_token == 2:
            data = self.data
            input_account_number = self.input_account_number
            self.customer_withdrawal = WithdrawalTransaction(data,input_account_number)
            self.output_value= self.customer_withdrawal.withdrawal_amount()
            if self.output_value is not None:
                self.json_save()
                self.output_return()

        elif transaction_token == 3:
            data = self.data
            input_account_number = self.input_account_number
            self.customer_deposit = DepositTransaction(data,input_account_number)
            self.output_value = self.customer_deposit.deposit_amount()
            if self.output_value is not None:
                self.json_save()
                self.output_return()


    def output_return(self):
        '''Returning output to the customer_window'''

        output_value = self.output_value
        return output_value

    def json_save(self):
        '''Rewiriting existing json'''

        if self.key == 2:

            return_new_balance = self.customer_withdrawal.withdrawal_returns()

        elif self.key == 3:

            return_new_balance = self.customer_deposit.deposit_returns()


        for customer_id in range(len(self.data['people'])):

            if self.input_account_number == self.data['people'][customer_id]['account_number']  :

                self.data['people'][customer_id]['balance'] = return_new_balance

        with open('bank_details.json',mode='w',encoding='utf-8') as new_json:
            json.dump(self.data,new_json)
