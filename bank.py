class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private variable (encapsulation)

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print(f"{self.name}'s Current Balance: {self.__balance}")



user1 = BankAccount("Tapan", 1000)
user2 = BankAccount("Rahul", 500)


user1.deposit(500)
user1.withdraw(200)
user1.show_balance()

print("------")

user2.withdraw(600)
user2.deposit(300)
user2.show_balance()

