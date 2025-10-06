class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


pin_code, balance, age = map(int, input().split(", "))

while (command := input()) != "End":
    command = command.split("#")
    task = command[0]
    amount = int(command[1])

    if task == "Send Money":
        given_pin = int(command[2])

        if amount > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if given_pin != pin_code:
            raise PINCodeError("Invalid PIN code")

        if age < 18:
            raise UnderageTransactionError(
                "You must be 18 years or older to perform online transactions")

        print(f"Successfully sent {amount:.2f} money to a friend")
        # update the balance
        balance -= amount
        print(f"There is {balance:.2f} money left in the bank account")

    elif task == "Receive Money":
        if amount < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        money_for_bank_account = amount / 2
        balance += money_for_bank_account
        print(f"{money_for_bank_account:.2f} money went straight into the bank account")
