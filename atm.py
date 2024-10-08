import time
import sys
import random
registered_users = []
def register():
    registration = int(input('How many number of forms are required: '))
    if registration > 0:
        i = 0 
        for i in range(registration):
            i+=1
            print('To open an account with us fill in the form below\n')
            global register_name
            register_name = input('Full-name: ')
            global pin
            pin = input('Create a pin you want to use for your transactions (maximum of 4 numbers): ')
            if len(pin) > 4:
                print('You have exceeded the maximum limit of numbers to create a pin')
            elif len(pin) < 4:
                print('The password you created is less than the required one')
            random_acct = random.randint(1111111111, 9999999999)
            print(f'Dear, {register_name} this is your account number: {random_acct}')
            global registered_details
            registered_details = register_name, pin
            registered_users.append(registered_details)
            if register_name and len(pin) == 4:
                print('You have successfully created an account')
    else:
        print('The number of forms cannot be 0')

register()


def card():
    for atm in registered_users:
        prompt_user = input('\nPlease insert your card ')
        print('Loading...')
        time.sleep(3)
        code()

def code():
    registered_pin = input('Please enter your pin: ')
    for registered_details in registered_users:
        if registered_pin == registered_details[1]:
            home()
        else:
            print('You have entered an invalid pin')
            code()
        return registered_pin

def home():
    select_user = input('''
                Select a transaction option:
                1. Withdrawal
                2. Transfer funds
                3. Check balance
    ''')
    if select_user == '1':
        choose()
        withdraw()
        withdraw_cash()
    if select_user == '2':
        choose()
        transfer()
        successful()
    if select_user == '3':
        choose()
        balance()
    return select_user

def choose():
    account = input('''
                    Select an account type:
                    1. Savings
                    2. Current
            ''')
    if account == "1":
        pass
    if account == "2":
        print("You don't have a current account")
        choose()

def withdraw():
    amount = int(input("Enter the amount you want to withdraw: "))
    if amount < 500:
        print('You cannot withdraw anything less than 500')
        withdraw()
    else:
        receipt()


def receipt():
    ask_user = input('Do you want a receipt of your transaction? (Yes/No) ')
    if ask_user.lower() == 'no':
        transaction()
    elif ask_user.lower() == "yes":
        print("This atm machine can't print receipt")
        transaction()
    else:
        print('You have entered an invalid answer')
        receipt()

def transaction():
    perform = input("Would you like to perform another transaction? (Yes/No) ")
    if perform.lower() == 'no':
        pass
    if perform.lower() == 'yes':
        home()

def withdraw_cash():
    print('Counting your money...')
    time.sleep(4)
    print('\nTake your cash')
    remove()

def transfer():
    bank = input('''
                    Select the bank you want to transfer the money to:
                    1. UBA
                    2. GTBank
                    3. Eco Bank
                    4. Union bank
                    5. First Bank
                ''')
    acct_number = int(input('Enter the account number of the destination account: '))
    if len(str(acct_number)) != 10:
        print('Invalid account number')
        transfer()
    else:
        transfer_amount()
    return bank

def transfer_amount():
    amount = int(input("Enter the amount you want to transfer: "))
    if amount < 500:
        print('You cannot transfer anything less than 500')
        transfer_amount()
    elif amount > 500:
        confirm_transfer()
    return amount

def confirm_transfer():
    confirm = input("Are you sure this is the account you want to send the money to? (Yes/No) ")
    if confirm.lower() == "yes":
        receipt()
    elif confirm.lower() == "no":
        transfer()
    else:
        print('You have entered an invalid answer')
        confirm_transfer()
    return confirm

def successful():
    print('Transfer Successful')
    remove()

def balance():
    print(f'{register_name} you have a total of 1,000,000 in your account.')
    receipt()
    remove()

def remove():
    time.sleep(1)
    print('Remove your card')
    # sys.exit()

card()