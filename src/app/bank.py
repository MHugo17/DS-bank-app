import pandas as pd


class Bank:
    def __init__(self, name): #acc and transactions are imported from panda dataframe
        self.name = name
        self.accounts = pd.DataFrame(columns=['id', 'firstname', 'lastname', 'balance'])
        self.transactions = pd.DataFrame(columns=['id', 'sender_id', 'recipient_id', 'amount', 'subject', 'category', 'timestamp'])

    def open_account(self, account_id, firstname, lastname, balance=0.0):
        assert len(self.accounts.loc[self.accounts['id'] == account_id ]) == 0, 'Account number 1 already taken!'

        account = {'id':account_id, 'firstname':firstname, 'lastname':lastname, 'balance':balance}
        self.accounts = self.accounts.append(account, ignore_index=True)

        return self.accounts

    def add_transaction(self, transaction_id, sender_id, recipient_id, subject, amount, category, timestamp):
        assert amount > 0, 'Amount needs to be greater than 0'
        assert len(self.accounts.loc[self.accounts['id'] == sender_id]) > 0, 'Sender has no account yet!'
        assert len(self.accounts.loc[self.accounts['id'] == recipient_id]) > 0, 'Recipient has no account yet!'

        transaction = {'id':transaction_id, 'sender_id':sender_id, 'recipient_id':recipient_id, 'amount':amount, 'subject':subject, 'category':category, 'timestamp':timestamp}
        self.transactions = self.transactions.append(transaction, ignore_index=True)

        return self.transactions

