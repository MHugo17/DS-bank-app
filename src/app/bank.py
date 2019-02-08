import app
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = []

    #crear cuenta con numero nombre apellido y el orden es egal
    def open_account(self, account):
        assert type(account) == app.Account, 'Account should be an app.Account'
        assert account.number not in self.accounts, 'Account number 1 already taken!'
        self.accounts[account.number] = account
        return account

    #transaction new
    def add_transaction(self, *, sender, recipient, subject, amount):
        assert sender.number in self.accounts, 'Sender has no account yet!'
        assert recipient.number in self.accounts, 'Recipient has no account yet!'
        assert amount > 0, 'Amount needs to be greater than 0'
        assert sender.has_funds_for(amount), 'Account has not enough funds'

        transaction = app.Transaction(sender=sender.number, recipient=recipient.number, subject=subject, amount=amount)

        self.transactions.append(transaction)
        sender.subtract_from_balance(amount)
        recipient.add_to_balance(amount)

        return transaction

    def konto_aus(self, *, year, month):
        selected_transactions = []  #the list of the transaction selected according to filter
        for transaction in self.transactions: #loop over all transactions
            if int(transaction.time[6:7]) == month and int(transaction.time[0:4]) == year: #filter defining month or year of interest
                selected_transactions.append(transaction)

        print('Konto Auszug Month:\n')
        for transaction in selected_transactions: #loop over selected transactions
            print((transaction.info(short=True)))  #orden

        print('\nSweet!')


