class Balance_transaction:
    def __init__(self,data,input_account_number):
        self.data = data
        self.input_account_number = input_account_number

    def balance_determine(self):

         for customer_id in range(len(self.data['people'])):

            if self.input_account_number == self.data['people'][customer_id]['account_number']  :
                balance_response = (f"Hi { self.data['people'][customer_id]['name']} your balance is { self.data['people'][customer_id]['balance']}") 
                return balance_response
