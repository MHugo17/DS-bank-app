class Transaction:
    #init class with arguments of the transaction
    def __init__(self, *, sender, recipient, subject, amount):
        # determina that sender and recipient must be integer, amount must be a float
        assert type(sender) == int, 'Sender needs to be an integer'
        assert type(recipient) == int, 'Recipient needs to be an integer'
        assert type(amount) == float, 'Amount needs to be a float'
        assert amount > 0, 'Amount needs to be greater than 0'
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.amount = amount

    #extract transaction info
    def info(self):
        return(f'From {self.sender} to {self.recipient}: {self.subject} - {self.amount} €')