from User import User, Account


class Bank:
    isBanrupt = False

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
        for account in self.__accounts:
            if account.email == email and account.password == password:
                return account


sonali_bank = Bank("Sonali Bank")
tamal = Account("Tamal", "tamal@gmail.com", "12345", "dhaka", "saving")
amit = Account("amit", "amit@gmail.com", "12345", "dhaka", "saving")
sonali_bank.add_account(tamal)
sonali_bank.add_account(amit)


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
                if ac is not None and ac.admin_secret == admin_secret:
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
                if ac is not None:
                    current_account = ac
                    print("Your login successfull!!!")
                else:
                    print(
                        "Your email or password or secret is not correct. Please provide valid information")
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


# Can delete any user account                                                              5
# Can see all user accounts list                                                            10
# Can check the total available balance of the bank.                            5
# Can check the total loan amount.                                                       5
# Can on or off the loan feature of the bank.

    else:
        if current_account.is_admin:
            print("======== Admin Option =======")
            print("Option 1: create an account: ")
            print("Option 2: sell all user accounts: ")
            print("Option 3: check the total available balance of the bank: ")
            print("Option 4: check the total loan amount: ")
            print("Option 5: Turn (on/off) loan feature: ")
            print("Option 6: exit: ")
            print("========= ******* ==========")
            ch = int(input("Enter the option: "))
            if ch == 1:
                name = input("Enter account holder name: ")
                email = input("Enter account holder email: ")
                password = input("Enter account holder password: ")
                address = input("Enter account holder address: ")
                account_type = input(
                    "Enter account holder account type(savings/current): ")
                ac = sonali_bank.check_account(email, password)
                if ac is not None:
                    sonali_bank.add_account(ac)
                    print("Account create successfully!!!")
            elif ch == 2:
                holder_name = input("Please enter the holder name: ")
                holder_email = input("Please enter the holder email: ")
                
            elif ch == 3:
                pass
