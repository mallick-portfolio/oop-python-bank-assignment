from User import User, Account


class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.__accounts = []
        pass

    def add_account(self, account):
        if isinstance(account, Account):
            self.__accounts.append(account)
            return account
        else:
            print('Your account is not valid. Please provide valid account')

    def check_account(self, email, password):
        print("email", email, password)
        flag = False
        ac = None
        for account in self.__accounts:
            if account.email == email and account.password == password:
                flag = True
                ac = account
                break
        if flag:
            print(ac.account_type)
            return ac
        else:
            print("Your information is not valid!!!")


sonali_bank = Bank("Sonali Bank")
tamal = Account("Tamal", "tamal@gmail.com", "12345", "dhaka", "saving")
sonali_bank.add_account(tamal)
current_account = None
while True:
    if current_account is None:
        option = input("Please Login or Register:(L/R) ")
        if option == "L":
            is_admin = input("Are you want to login as admin(y/n): ")
            if is_admin == "y":
                email = input("Please enter your email: ")
                password = input("Please enter your password: ")
                admin_secret = input("Please enter admin secret: ")
                ac = sonali_bank.check_account(email, password)
                if ac.admin_secret == admin_secret:
                    ac.is_admin = True
                    current_account = ac
                    print("Your are now login as admin")
                else:
                    print(
                        "Your email or password or secret is not correct. Please provide valid information")

            else:
                email = input("Please enter your email: ")
                password = input("Please enter your password: ")
                ac = sonali_bank.check_account(email, password)
                current_account = ac
                print("Your login successfull!!!")
        elif option == "R":
            # name, email, password, address, account_type
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            address = input("Enter your address: ")
            account_type = input("Enter your account type(savings/current): ")
            ac = sonali_bank.check_account(email, password)
            if ac is not None:
                print(
                    "Already user exist with this email. Please try with another email")
            else:
                new_account = Account(
                    name, email, password, address, account_type)
                account = sonali_bank.add_account(new_account)
                current_account = account

    else:
        print(current_account.is_admin)
        break
