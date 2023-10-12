from User import User, Account


class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.__accounts = []
        pass

    def add_account(self, account):
        if isinstance(account, Account):
            self.__accounts.append(account)
        else:
            print('Your account is not valid. Please provide valid account')


    