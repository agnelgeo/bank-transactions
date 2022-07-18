
import json
from balance import Balance_transaction
from deposit import Deposit_transaction
from withdrawal import Withdrawal_transaction

class Validation:

    def __init__(self):

        with open('BANK/bankdetails.json') as f:
            self.data=json.load(f)
    
    def customer_find(self,input_values):
        try:

            self.input_account_number = input_values[0]
            self.input_password= input_values[1]
            input_flag = 0 
            for customer_id in range(len(self.data['people'])):
                
                if self.input_account_number == self.data['people'][customer_id]['account_number'] and self.input_password == self.data['people'][customer_id]['password']:
                    print(f"Hello {self.data['people'][customer_id]['name']}")
                    input_flag = 1
                    return input_flag
            if input_flag == 0:
                print("Please enter a valid input 000")
                
        except:
            print("Please try again and enter valid inputs")



    def interactor(self,transaction_token):
        
        self.key = transaction_token
      
        if transaction_token == 1:
            data = self.data
            input_account_number = self.input_account_number
            customer_balance = Balance_transaction(data,input_account_number)
            self.output_value = customer_balance.balance_determine()
            self.output_return()
 
        elif transaction_token == 2:
            data = self.data
            input_account_number = self.input_account_number
            self.customer_withdrawal = Withdrawal_transaction(data,input_account_number)
            self.output_value= self.customer_withdrawal.withdrawal_amount()
            if self.output_value != None:
                self.json_save()
                self.output_return()
            
        elif transaction_token == 3:
            data = self.data
            input_account_number = self.input_account_number
            self.customer_deposit = Deposit_transaction(data,input_account_number)
            self.output_value = self.customer_deposit.deposit_amount()
            if self.output_value != None:
                self.json_save()
                self.output_return()
      
    def output_return(self):

        output_value = self.output_value
        return output_value

    def json_save(self):


        if self.key == 2:

            return_new_balance = self.customer_withdrawal.withdrawal_returns()

        elif self.key == 3:

            return_new_balance = self.customer_deposit.deposit_returns()


        for customer_id in range(len(self.data['people'])):
            
            if self.input_account_number == self.data['people'][customer_id]['account_number']  :

                self.data['people'][customer_id]['balance'] = return_new_balance

                

        with open('BANK/bankdetails.json','w') as new_json:
            json.dump(self.data,new_json)
            




