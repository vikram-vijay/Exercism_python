from threading import Lock

class BankAccount:
    def __init__(self):
        self.status = False
        self.balance = 0
        self.thread = Lock()

    def get_balance(self):
        with self.thread:
            if self.status == False:
                    raise ValueError("Account is closed")
            else:
                return self.balance

    def open(self):
        with self.thread:
            if self.status == True:
                raise ValueError ("Account open")
            else:
                self.status = True
                self.balance = 0

    def deposit(self, amount):
        with self.thread:
            if self.status == False:
                raise ValueError("Account is closed")
            else:
                if amount >= 0:
                    self.balance += amount
                else:
                    raise ValueError("Can't deposit given amount")

    def withdraw(self, amount):
        with self.thread:
            if self.status == False:
                raise ValueError("Account is closed")
            else:
                if amount >= 0 and (self.balance - amount) >= 0:
                    self.balance -= amount
                else:
                    raise ValueError("Can't withdraw given amount")

    def close(self):
        with self.thread:
            if self.status == False:
                raise ValueError("Account is closed")
            else:
                self.status = False
