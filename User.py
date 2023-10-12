import uuid


class User:
    # his/her name, email, address and account
    def __init__(self, name, email, password, address, account_type) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.account_type = account_type
        self.account_no = uuid.uuid4()
        self.balance = 0
        pass


tamal = User("tamal", 'tamal@gmail.com', 'dhaka', "saving")
print(tamal.account_no)
