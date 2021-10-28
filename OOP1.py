class BankAccount():
    def __init__(self, account_number, account_name, balance = 0):
        self._account_number = account_number
        self._account_name = account_name
        self.set_balance = balance

    def get_account_number(self):
        return self._account_number

    def get_account_name(self):
        return self._account_name

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance >= 0:
            self._balance += balance
        else: print('Số dư phải là số nguyên')

    def display(self):
        print("Số acc của bạn là:", self.get_account_number())
        print("Tên tài khoản của bạn là", self.get_account_name())
        print("Số dư tài khoản hiện có là:", self.get_balance())


    def withdraw(self, amount):
        if amount > 0 and amount < self.get_balance():
            self._balance -= amount
        else: print("amount ko thỏa mãn ")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else: print("amount phải lớn hơn 0 ")

dung = BankAccount("8888","Vũ Thảo Dung")
dung.display()
dung.deposit(20)
dung.display()
dung.withdraw(30)
dung.display()

