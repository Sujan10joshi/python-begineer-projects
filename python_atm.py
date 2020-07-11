print("\n     --->> Welcome to Python ATM Service !!! <<---    \n")

restart = ('y','Y')
chances = 3
pin = 1234
total_balance = float(1500.69)

while chances >= 0:
    entered_pin = int(input("Please enter your 4 digit PIN: "))
    if entered_pin == (1234):
        print("You entered your pin correctly.\n")
        while restart not in ('N','n','no','No','NO'):
            print("Press 1 to check your balance. ")
            print("Press 2 to make your withdraw. ")
            print("Press 3 to pay in. ")
            print("Press 4 to return your card. ")
            option = int(input("\nWhat would you like to choose? "))

            if option == 1:
                print(f"Your current balance: {total_balance}\n")
                restart = input("Would you like to go back ('y'/'n')? ")
                if restart in ('N','n'):
                    print('   --Thank You !!!--   ')
                    break
            elif option == 2:
                try:
                    withdraw_money = float(input("How much money you want to withdraw? "))
                    if withdraw_money > total_balance:
                        raise('Withdraw ERROR')
                except:
                        print(f"Unsufficient Amount. Your current balance is: {total_balance}")
                        break
                total_balance -= withdraw_money
                print(f"Now, your current balance is: {total_balance}\n")
                restart = input("Would you like to go back ('y'/'n')? ")
                if restart in ('N','n'):
                    print('   --Thank You !!!--   ')
                    break
            elif option == 3:
                payin_money = float(input("\nHow much money you want to pay in? "))
                print(f"You are depositing {payin_money} to your account.")
                total_balance += payin_money
                print(f"Now, your current balance is: {total_balance}")
                restart = input("\nWould you like to go back ('y'/'n')? ")
                if restart in ('N','n'):
                    print("   --Thank you !!!--   ")
                    break
            elif option == 4:
                print("\nPlease wait until your card is returned")
                print("     ---Thank you for your service--- !!!     ")
                break

    elif pin != ('1234'):
        print("Incorrect PIN")
        chances -= 1
        if chances == 0:
            print("\nxxx-- No More Tries --xxx")
            break

