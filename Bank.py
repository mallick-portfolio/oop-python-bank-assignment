from User import User, Account


class Bank:
    isBanrupt = False
    is_loan_feature = True

    def __init__(self, name) -> None:
        self.name = name
        self.__accounts = []
        pass

    # add new account
    def add_account(self, account):
        if isinstance(account, Account):
            self.__accounts.append(account)
            return account
        else:
            print('Your account is not valid. Please provide valid account')

    # check account is available or not
    def check_account(self, email, password):
        for account in self.__accounts:
            if account.email == email and account.password == password:
                return account

    # delete user account
    def delete_account(self, name, email):
        flag = False
        for account in self.__accounts:
            if account.name == name and account.email == email:
                self.__accounts.remove(account)
                flag = True
                break
        if flag:
            print("Account removed successfull!!!")
            return True
        else:
            print("Your information is not correct. Please provide valid information")
            return False

    # see all user account
    def see_all_account(self):
        print()
        print("====== All account in this bank =======")
        if len(self.__accounts):
            for account in self.__accounts:
                print(
                    f"Holder name: {account.name}. Email: {account.email}. Address {account.address}. Account no: {account.account_no}")
        else:
            print("Currently the bank has no account.")

    # available balance in the bank
    def available_bank_balance(self):
        total = 0
        for account in self.__accounts:
            total += account.balance
        return total

    # user total loan from this bank
    def total_loan(self):
        total = 0
        for account in self.__accounts:
            total += account.loan_amount
        return total


sonali_bank = Bank("Sonali Bank")
tamal = Account("Tamal", "tamal@gmail.com", "12345", "dhaka", "saving")
amit = Account("amit", "amit@gmail.com", "12345", "dhaka", "saving")
sonali_bank.add_account(tamal)
sonali_bank.add_account(amit)


# replica system
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


# Can check the total loan amount.                                                       5
# Can on or off the loan feature of the bank.

    else:
        if current_account.is_admin:
            print()
            print("======== Admin Option =======")
            print("Option 1: Create an account: ")
            print("Option 2: Delete an account: ")
            print("Option 3: See all user accounts: ")
            print("Option 4: Check the total available balance of the bank: ")
            print("Option 5: Check the total loan amount: ")
            print("Option 6: Turn (on/off) loan feature: ")
            print("Option 7: Exit: ")
            print("========= ******* ==========")
            print()
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
                sonali_bank.delete_account(holder_name, holder_email)

            elif ch == 3:
                sonali_bank.see_all_account()
            elif ch == 4:
                balance = sonali_bank.available_bank_balance()
                print(f"Current balance in bank is {balance}")
            elif ch == 5:
                loan = sonali_bank.total_loan()
                print(f"Total loan from this bank is {loan}")
            elif ch == 6:
                print()
                print("laodn feature", sonali_bank.is_loan_feature)
                print()
                if sonali_bank.is_loan_feature:
                    change_loan_feature = input(
                        "Are you want to allow loan feature(y/n): ")
                    if change_loan_feature == 'y':
                        sonali_bank.is_loan_feature = True
                    else:
                        sonali_bank.is_loan_feature = False
                else:
                    confirm = input(
                        "Are you sure want to stop loan feature(y/n): ")
                    if confirm == 'y':
                        sonali_bank.is_loan_feature = False
                    else:
                        sonali_bank.is_loan_feature = True
            elif ch == 7:
                pass
