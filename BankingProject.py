# Author: Ishan Dias
# Use print statement at line 37 for testing.
import random


def main():
    print("~~~~~~~~~~~~~~~~~~")
    print("Welcome to AIB", "\n"
          + "Allied Irish Bank")
    print("~~~~~~~~~~~~~~~~~~")
    name_list, account_number_list, account_balance_list = read_file()
    option = 0
    while option != 6:  # While the user doesn't enter 6th option the banking_menu list continues

        banking_menu = ["1. Open Account", "2. Close Account", "3. Withdraw Money",
                        "4. Deposit Money", "5. Report for Management", "6. Quit"]

        for option in banking_menu:
            print(option)
        user_input = False
        while not user_input:
            try:
                option = int(input("Please enter an option:"))
                if option > 0:
                    user_input = True
                else:
                    print("Please enter a number greater than 0 \n")
                    for option in banking_menu:
                        print(option)
            except:
                print("Please enter a number between 1 to 6\n")
                for option in banking_menu:
                    print(option)

        # This print statement is for testing purposes only
        # This shows the lists with names, account numbers and account balance
        print(name_list + account_number_list + account_balance_list)

        if option == 1:
            name_list, account_number_list, account_balance_list = \
                open_account(name_list, account_number_list, account_balance_list)

        elif option == 2:
            name_list, account_number_list, account_balance_list = \
                close_account(name_list, account_number_list, account_balance_list)

        elif option == 3:
            name_list, account_number_list, account_balance_list = \
                withdraw_money(name_list, account_number_list, account_balance_list)

        elif option == 4:
            name_list, account_number_list, account_balance_list = \
                deposit_money(name_list, account_number_list, account_balance_list)

        elif option == 5:
            report_for_management(name_list, account_number_list, account_balance_list)

        elif option == 6:
            quit_program(name_list, account_number_list, account_balance_list)


# Function for the file
def read_file():
    name_list = []
    account_number_list = []
    account_balance_list = []

    file = open("bank.txt", "r")  # Opening the bank.txt file
    lines = file.readlines()  # file reads the lines
    for line in lines:
        information = line.split()  # splits the individual lines in the bank.txt file
        account_number_list.append(information[0])  # All account numbers are at index 0
        account_balance_list.append(float(information[1]))  # All account balance is at index 1
        name_list.append(information[2])  # All account names are at index 2
    return name_list, account_number_list, account_balance_list

# Function for opening an account
def open_account(name_list, account_number_list, account_balance_list):
    name = input("Please enter your name:")
    print("Your name:", name)
    name_list.append(name)
    found = True
    while found == True:
        number = str(random.randint(1, 1000000))
        found = number in account_number_list
    print("your account number:", number)
    account_number_list.append(number)
    # Once a new account is created the clients balance is 0.0
    account_balance_list.append(0.0)
    print("Your account has been created " + name + "\n")
    return name_list, account_number_list, account_balance_list


# Function for closing an account
def close_account(name_list, account_number_list, account_balance_list):
    account_number = input("Enter your account number:")
    index = 0
    found = False
    for i in account_number_list:
        if i == account_number:
            found = True
            break
        index = index + 1
    if found:
        print("Your account has been closed " + name_list[index] + "\n"
              + "Thank you for banking with AIB! \n")
        # deletes the 3 lists from their index position.
        del account_number_list[index]
        del account_balance_list[index]
        del name_list[index]
    else:
        print("Sorry this account number doesn't exist in our system. \n")
    return name_list, account_number_list, account_balance_list


# Function for Withdrawing money from an account
def withdraw_money(name_list, account_number_list, account_balance_list):
    account_number = input("Enter your account number:")
    index = 0
    found = False
    for i in account_number_list:
        if i == account_number:
            found = True
            break
        index = index + 1
    if found:
        issue = True
        while issue:
            try:
                withdraw_amount = float(input("Enter the amount you want to withdraw:"))
                # The Amount is the new amount the customer has withdrawn.
                if withdraw_amount < 0:
                    print("Sorry your amount must be positive and not negative. \n")
                    break
                amount = account_balance_list[index] - withdraw_amount
                # if the amount is greater than or equal to 0 it will take the amount away from the balance list.
                if amount >= 0:
                    account_balance_list[index] = account_balance_list[index] - withdraw_amount
                    print("Your transaction has been successful", name_list[index])
                    print("Therefore an amount of ", "€",
                          format(withdraw_amount, ".2f"),
                          " is removed from your account number: ", account_number, sep="")
                    print("Your current balance ", "€", format(account_balance_list[index], ".2f"), sep="")
                    print("")

                else:
                    print("Unfortunately you don't have a sufficient amount in your account", name_list[index])
                    print("Your current balance is ", "€", format(account_balance_list[index], ".2f"), sep="")
                    print("")
                    break
            finally:
                return name_list, account_number_list, account_balance_list
    else:
        print("Sorry this account number doesn't exist in our system \n")
    return name_list, account_number_list, account_balance_list


# Function for depositing an amount to an account
def deposit_money(name_list, account_number_list, account_balance_list):
    account_number = input("Enter your account number:")
    index = 0
    found = False
    for i in account_number_list:
        if i == account_number:
            found = True
            break
        index = index + 1
    if found:
        issue = True
        while issue:
            try:
                deposit_amount = float(input("Enter the amount you want to deposit:"))
                # The Amount is the new amount the customer has deposited
                if deposit_amount <= 0:
                    print("Sorry your amount must be positive and not negative. \n")
                    break
                amount = account_balance_list[index] + deposit_amount
                # if the amount is greater or = 0 it will take the amount away from the balance list.
                if amount >= 0:
                    account_balance_list[index] = account_balance_list[index] + deposit_amount
                    print("Your transaction has been successful", name_list[index])
                    print("Therefore an amount of ", "€",
                          format(deposit_amount, ".2f"), " is added to your account number: ", account_number, sep="")
                    print("Your current balance is ", "€", format(account_balance_list[index], ".2f"), sep="")
                    print("")
                    break
                else:
                    print("Sorry can you enter a positive number", name_list[index])
                    print("Your balance after your current transaction is ", "€",
                          format(account_balance_list[index], ".2f"), sep="")
                    print("")
                    break

            finally:
                return name_list, account_number_list, account_balance_list
    else:
        print("Sorry this account number doesn't exist in our system \n")
        return name_list, account_number_list, account_balance_list


# Function to display a report for all the accounts details
def report_for_management(name_list, account_number_list, account_balance_list):
    for i in range(len(account_number_list)):
        print("Client " + name_list[i] + " whose account number is " + account_number_list[i] +
              " has " + "€" + str(account_balance_list[i]))
        total = sum(account_balance_list)
    print("Total amount of deposit in the bank is " + "€" + format(total, ".2f"))
    largest_deposit = max(account_balance_list)
    i = account_balance_list.index(largest_deposit)
    print("Client " + name_list[i] + " " + "has largest amount of deposit in the bank which is "
          + "€" + str(largest_deposit) + "\n")


# Function for quiting the program
def quit_program(name_list, account_number_list, account_balance_list):
    print("Thank you for coming to AIB" + "\n" + "Have a great day!")
    quit_file = open("bank.txt", "w")
    for i in range(len(account_number_list)):
        save_file = account_number_list[i] + " " + str(account_balance_list[i]) + " " + name_list[i] + "\n"
        quit_file.write(save_file)
    quit_file.close()


main()
