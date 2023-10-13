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
        self.account_history = []
        self.possible_loan = 2
        self.max_loan_amount = 100000
        self.loan_amount = 0
        super().__init__(name, email, password, address)

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            history = {
                "type": "deposit",
                "amount": amount
            }
            self.account_history.append(history)
            print(
                f'Your deposit successfully!!!. Your current accout balance is {self.__balance}')
        else:
            print(
                "Negetive amount is not allow to deposit!!!. Please provide valid amount")

    # withdraw function
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            history = {
                "type": "withdraw",
                "amount": amount
            }
            self.account_history.append(history)
            print(
                f"{amount} withdraw successfull!!!. Your current balance is {self.__balance}")
        else:
            print("Withdrawal amount exceeded")

    # available balance
    def available_balance(self):
        print(f"Your current balance is {self.__balance}")

    def transition_history(self):
        print(f"============{self.name} my transition history===========")
        print()
        for history in self.account_history:
            print(
                f"History type:{history['type']} and amount is {history['amount']}")
        print()

  # loan function
    def take_loan(self, amount):
        if self.possible_loan > 0:
            if amount > self.max_loan_amount:
                print(
                    f"Sorry to say. You are not able to loan more then {self.max_loan_amount}")
            else:
                self.loan_amount += amount
                self.__balance -= amount
                self.possible_loan -= 1
                history = {
                    "type": "loan",
                    "amount": amount
                }
                self.account_history.append(history)
                print(f"Your loan approved succussfully!!!")
        else:
            print("You already take loan maximum time. Your are not allow to reloan")
            print()

    # transfer account to another user
    def transfer_amount(self, amount, account):
        if self.__balance >= amount:
            self.__balance -= amount
            account.__balance += amount
            history = {
                    "type": "transfer",
                    "amount": amount
                }
            self.account_history.append(history)
            print(f"Your amount {amount} transfer successfull!!!")
        else:
            print(f"Your account has not enough money to transfer!!!")
