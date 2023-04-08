class Account:
    def __init__(self, cust_id):
        self.cust_id = cust_id


class CheckingAccount(Account):
    def __init__(self, cust_id, deposit_amount):
        super().__init__(cust_id)
        self.amount = deposit_amount
        self.withdraw_whole = 0
        self.withdraw_part = 0

        # returns a string, formatted up to 2 decimal places
        self.numstr = "{:.2f}".format(deposit_amount)

        # splits the whole number and decimal part of the amount
        self.amount_whole, self.amount_part = map(int, self.numstr.split("."))

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        # splits the whole number and decimal part of the amount to withdraw
        self.withdraw_whole, self.withdraw_part = map(int, "{:.2f}".format(withdraw_amount).split("."))

        # if the amount in the account is greater than the requested amount,
        # then it is allowed to withdraw that amount
        if self.amount >= float(withdraw_amount):
            self.amount_whole -= self.withdraw_whole

            # if the decimal part of the requested amount is greater than the
            # decimal part of the amount in the account, then 1 dollar is taken out
            # and then calculates the remaining decimal value
            if self.withdraw_part > self.amount_part:
                self.amount_part = self.withdraw_part - self.amount_part
                self.amount_whole -= 1
                self.amount_part = 100 - self.amount_part
            else:
                self.amount_part -= self.withdraw_part

            # combines the whole number and decimal value as one but as a float
            self.amount = round(float(f"{self.amount_whole}.{self.amount_part:02d}"), 2)
        else:
            print("Error! Cannot withdraw larger than what you have.")

    def display_amount(self):
        print(self.amount)

    def get_amount(self):
        return self.amount


class SavingsAccount(Account):
    def __init__(self, cust_id, deposit_amount):
        super().__init__(cust_id)
        self.amount = deposit_amount
        self.interest_rate = 0.02  # 2% interest rate
        self.withdraw_whole = 0
        self.withdraw_part = 0

        # returns a string, formatted up to 2 decimal places
        self.numstr = "{:.2f}".format(deposit_amount)

        # splits the whole number and decimal part of the amount
        self.amount_whole, self.amount_part = map(int, self.numstr.split("."))

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        # splits the whole number and decimal part of the amount to withdraw
        self.withdraw_whole, self.withdraw_part = map(int, "{:.2f}".format(withdraw_amount).split("."))

        # if the amount in the account is greater than the requested amount,
        # then it is allowed to withdraw that amount
        if self.amount >= float(withdraw_amount):
            self.amount_whole -= self.withdraw_whole

            # if the decimal part of the requested amount is greater than the
            # decimal part of the amount in the account, then 1 dollar is taken out
            # and then calculates the remaining decimal value
            if self.withdraw_part > self.amount_part:
                self.amount_part = self.withdraw_part - self.amount_part
                self.amount_whole -= 1
                self.amount_part = 100 - self.amount_part
            else:
                self.amount_part -= self.withdraw_part

            # combines the whole number and decimal value as one but as a float
            self.amount = round(float(f"{self.amount_whole}.{self.amount_part:02d}"), 2)
        else:
            print("Error! Cannot withdraw larger than what you have.")

    def display_amount(self):
        print(self.amount)

    def get_amount(self):
        return self.amount

    def add_interest(self):
        # calculate interest and add to account balance
        interest = self.amount * self.interest_rate
        self.amount += interest


class BusinessAccount(Account):
    def __init__(self, cust_id, deposit_amount):
        super().__init__(cust_id)
        self.amount = deposit_amount
        self.withdraw_whole = 0
        self.withdraw_part = 0

        # returns a string, formatted up to 2 decimal places
        self.numstr = "{:.2f}".format(deposit_amount)

        # splits the whole number and decimal part of the amount
        self.amount_whole, self.amount_part = map(int, self.numstr.split("."))

        # initialize the credit limit
        self.credit_limit = 10000

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        # splits the whole number and decimal part of the amount to withdraw
        self.withdraw_whole, self.withdraw_part = map(int, "{:.2f}".format(withdraw_amount).split("."))

        # if the amount in the account plus the credit limit is greater than the requested amount,
        # then it is allowed to withdraw that amount
        if self.amount + self.credit_limit >= float(withdraw_amount):
            # if the requested amount is greater than the amount in the account, deduct the remaining
            # amount from the credit limit
            if self.amount < float(withdraw_amount):
                remaining_amount = float(withdraw_amount) - self.amount
                self.credit_limit -= remaining_amount
            self.amount_whole -= self.withdraw_whole

            # if the decimal part of the requested amount is greater than the
            # decimal part of the amount in the account, then 1 dollar is taken out
            # and then calculates the remaining decimal value
            if self.withdraw_part > self.amount_part:
                self.amount_part = self.withdraw_part - self.amount_part
                self.amount_whole -= 1
                self.amount_part = 100 - self.amount_part
            else:
                self.amount_part -= self.withdraw_part

            # combines the whole number and decimal value as one but as a float
            self.amount = round(float(f"{self.amount_whole}.{self.amount_part:02d}"), 2)
        else:
            print("Error! Cannot withdraw larger than what you have plus credit limit.")

    def display_amount(self):
        print(self.amount)

    def get_amount(self):
        return self.amount

    def set_credit_limit(self, new_limit):
        self.credit_limit = new_limit

    def get_credit_limit(self):
        return self.credit_limit


if __name__ == '__main__':
    isSessionOn = True
    isCustomer = False

    def initialise_objects():
        global sally_checking, paolo_business, paolo_savings, master_list

        sally_checking = CheckingAccount(1, 2567.50)
        paolo_savings = SavingsAccount(2, 12890.01)
        paolo_business = BusinessAccount(2, 14500.40)

        master_list = [[sally_checking, 1, 1], [paolo_savings, 2, 2], [paolo_business, 2, 3]]

        return None

    initialise_objects()

    while isSessionOn is True:
        print("Welcome to 24-hour ATM service.")
        print("Insert your card.")

        # Card reading the customer info representation
        customerID = int(input("Enter your customer id number: "))
        print("\n")

        cust_accounts = []
        for i in master_list:
            if i[1] == customerID:
                cust_accounts.append(i[2])
                isCustomer = True

        if isCustomer is True:
            isAccountSelected = False

            while isAccountSelected is False:
                print("Enter 1 for checking account")
                print("Enter 2 for savings account")
                print("Enter 3 for business account")
                account_type = int(input("Enter which account to use: "))

                if account_type in cust_accounts:
                    for x in master_list:
                        if account_type == x[2]:
                            objectName = x[0]

                    isAccountSelected = True
                    isAccountSessionOn = True

                    while isAccountSessionOn is True:
                        print("\nHow may I help you?")
                        print("Press 1 for balance view.")
                        print("Press 2 for withdrawals")
                        print("Press 3 to exit.")

                        action_value = int(input("Please enter your choice: "))

                        if action_value == 1:
                            objectName.display_amount()
                            print("\n")

                        if action_value == 2:
                            amnt_to_withdraw = float(input("Enter the amount to withdraw: "))
                            temp_str = str(amnt_to_withdraw)

                            adjusted_amount = "%.2f" % amnt_to_withdraw
                            # print "adjusted_amount:", adjusted_amount
                            objectName.withdraw(adjusted_amount)

                            print("current balance is", objectName.get_amount())
                            print("\n")

                        if action_value == 3:
                            isAccountSessionOn = False
                            print("Thank for using the 24-hour ATM service.")
                            print("Have a pleasant day.")
                            print("\n\n")
                            print("##########################################")
                else:
                    print("Error. You don't have that account.")
                    print("Please try again.\n")

        else:
            print("Cannot find your record.")
            print("Please get your card.")
            print("Exiting this session...")
