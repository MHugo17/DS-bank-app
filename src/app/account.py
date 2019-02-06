class Account:
    #init class with 4 arguments and balance is optional
    def __init__(self, *, firstname, lastname, number, balance = 0.0):
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.balance = balance
    #account number is an integer
        assert type(number) == int, 'Number needs to be an integer'
        assert type(balance) == float, 'Balance needs to be a float'
    #info return
    def info(self):
        return(f'Number {self. number}: {self.firstname} {self.lastname} - {self.balance} €')

    #check funds
    def has_funds_for(self, founds):
        return self.balance >= founds

    #add founds to balance
    def add_to_balance(self, deposit):
        assert deposit >0, 'Amount needs to be greater than 0'
        self.balance = deposit + self.balance
    #subtract from balance
    def subtract_from_balance(self, subtract):
        assert self.balance >= subtract, 'Account has not enough funds'
        self.balance = self.balance - subtract