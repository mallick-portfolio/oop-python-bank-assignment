import uuid

# TODO 7 no point not complete


class User:
    def __init__(self, name, email, password, address) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.admin_secret = "12345"
        self.is_admin = False

    def check_admin(self, admin_secret):
        if self.admin_secret == admin_secret:
            return True
        else:
            return False


class Account(User):
    def __init__(self, name, email, password, address, account_type) -> None:
        self.account_type = account_type
        self.account_no = uuid.uuid4()
        self.__balance = 0
        self.transaction_history = []
        self.possible_loan = 2
        self.max_loan_amount = 100000
        super().__init__(name, email, password, address)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            history = {
                "type": "deposit",
                "amount": amount
            }
            self.transaction_history.append(history)
            print(
                f'Your deposit successfully!!!. Your current accout balance is {self.balance}')

    # withdraw function
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            history = {
                "type": "withdraw",
                "amount": amount
            }
            self.transaction_history.append(history)
            print(
                f"{amount} withdraw successfull!!!. Your current balance is {self.balance}")
        else:
            print("Withdrawal amount exceeded")

    # available balance
    def available_balance(self):
        print(f"Your current balance is {self.balance}")

  # loan function
    def take_loan(self, amount):
        if amount > self.max_loan_amount:
            print(
                f"Sorry to say. You are not able to loan more then {self.max_loan_amount}")
        else:
            self.balance -= amount
            history = {
                "type": "loan",
                "amount": amount
            }
            self.possible_loan -= 1
            self.transaction_history.append(history)
            print(f"Your loan approved succussfully!!!")
