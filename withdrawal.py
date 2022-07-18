

class Withdrawal_transaction:
    def __init__(self,data,input_account_number):
        self.data = data
        self.input_account_number = input_account_number
        
        

    def withdrawal_amount(self):

        withdrawal_amount = float(input("Please enter amount to withdraw "))

        for customer_id in range(len(self.data['people'])):

            if self.input_account_number == self.data['people'][customer_id]['account_number']  :
                
                balance =float(self.data['people'][customer_id]['balance'])

                if balance >= withdrawal_amount:
                    new_balance = balance - withdrawal_amount
                    withdrawal_response = (f"Hi { self.data['people'][customer_id]['name']} you have withdrawn {withdrawal_amount} balance is {new_balance}") 
                    self.new_balance = new_balance
                    self.withdrawal_returns()
                   

                    return withdrawal_response

                else:

                    print("Insufficent balance")
    
                    break

    def withdrawal_returns(self):
            return_new_balance = self.new_balance
            return return_new_balance


