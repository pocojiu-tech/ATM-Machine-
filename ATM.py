# ATM Machine Simulation

account_number = int(input("Enter your account number: "))
balance = 10000

if account_number != 9:
    print("Wrong Account Number. Access Denied.")
else:
    while True:
        print("""
Welcome Shashank
What do you want to do today?
Press 1 to know your Balance
Press 2 to Withdraw
Press 3 to Deposit
Press 4 to Exit
""")

        choose = int(input("Choose your response: "))

        if choose == 1:
            print("Your current balance is:", balance)

        elif choose == 2:
            withdraw_amount = int(input("Enter amount to withdraw: "))
            if withdraw_amount > balance:
                print("Insufficient balance.")
            else:
                balance -= withdraw_amount
                print(withdraw_amount, "withdrawn successfully.")
                print("New balance is:", balance)

        elif choose == 3:
            deposit_amount = int(input("Enter amount to deposit: "))
            balance += deposit_amount
            print(deposit_amount, "deposited successfully.")
            print("New balance is:", balance)

        elif choose == 4:
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Try again.")