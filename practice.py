balance = 2000
pin = 1234

user_pin = int(input("Please enter your PIN: "))

if user_pin == pin:
    print(f"Your current balance is ${balance}")

    choice = input("Would you like to withdraw (W) or deposit (D) money? ").upper()

    if choice == 'W':
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"Withdrawal successful. Your updated balance is ${balance}")
        else:
            print("Insufficient funds.")

    elif choice == 'D':
        deposit_amount = float(input("Enter the amount to deposit: "))
        balance += deposit_amount
        print(f"Deposit successful. Your updated balance is ${balance}")

    else:
        print("Invalid choice.")

else:
    print("Incorrect PIN. Access denied.")
