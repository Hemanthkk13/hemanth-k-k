class BankAccount:
    def __init__(self,account_number,pin,balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def login(self, entered_pin):
        return entered_pin == self.pin

    def display_balance(self):
        print(f"Account Balance:${self.balance}")

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}.")
            self.display_balance()
        else:
            print("invalid deposit amount.")
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"withdrew${amount}.")
            self.display_balance()
        else:
            print("Invalid withdrawal amount or insufficient funds.")

def main():
    account_number="94957"
    pin="4433"
    user_account = BankAccount(account_number,pin,balance=20000)
    account_number = input("Enter your account number:")
    pin = input("Enter your PIN:")


    if user_account.login(pin):
        print("Login successful.")
        while True:
            print("\nchoose an option:")
            print("1.Deposit Money")
            print("2.Withdraw Money")
            print("3.check your balance")
            print("4.Exit")

            choice = input("Enter your choice(1/2/3/4):")


            if choice == '1':
                amount = float(input("Enter your amount to deposit:$"))
                user_account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter the amount to withdraw:$"))
                user_account.withdraw(amount)
            elif choice == '3':
                user_account.display_balance()
            elif choice == '4':
                print("Thank you for using our DFD bank")
                break
            else:
                print("Invalid choice.please choose a valid option.")
    else:
        print("login failed.Invalid account number or PIN.")


if __name__ == "__main__":
    main()


