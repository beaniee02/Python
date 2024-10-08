import random
import sys
import time

customers = []
def register():
    global users
    users = int(input('How many users do we want to register? '))
    if users > 0:
        i = 0
        for i in range(users):
            i += 1
            print('Fill in the form below to create an account')
            full_name = input('Enter your surname and first name>>> ').strip()
            address = input('Enter your residential address>>> ')
            phone = phonenum()
            email = input('Enter your email address>>> ')
            random_acct = random.randint(1111111111, 9999999999)
            print(f'Dear, {full_name} this is your account number: {random_acct}')
            print('You have successfully created an account')
            global pin
            pin = pincode()
            global account
            account = random_acct, pin
            customers.append(account)
            time.sleep(3)
            ask_customer = input('''
                                        \nDo you want to perform USSD Banking?
                                            1. Yes
                                            2. No
                                ''')
            if ask_customer == '1':
                dial()
                starter()
            else:
                sys.exit()
    else:
        print('You have to register at least one user')

def phonenum():
    phone = input('Enter your phone number: ')
    if len(phone) != 11:
        print(f"Invalid phone number")
        phonenum()        
    return phone

def pincode():
    Pin = int(input('Create a pin of 4 digits which you will be using for your transaction>>> '))
    if len(str(Pin)) != 4:
        print('You need to enter a maximum of 4 digits to create a pin')
        pincode()
    return Pin

def dial():
    press = input('Dial *919# to start your USSD Banking>>> ')
    if press != '*919#':
        print('You have entered an invalid USSD number')
        dial()
    return press

def starter():
    info = input('''
                        Wecome to USSD Banking. Please note that a N6.98
                    network charge will be applied to your bank account for
                            banking services on this channel.
                                1. Proceed
                                2. Cancel
                ''')
    if info == '1':
        home()
    if info == '2':
        sys.exit()
    return info

def home():
    prompt = input('''
                1. Buy Airtime
                2. Buy Data
                3. Transfers
                4. Pay Bills
                5. Check Balance
                6. Click Credit
                7. Enquiries
                8. Account Opening
                9. Link NIN
                0. Next
        ''')
    if prompt == '1':
        pinprompt()
        airtime()
    if prompt == '2':
        pinprompt()
        data()
    if prompt == '3':
        pinprompt()
    if prompt == '4':
        pinprompt()
    if prompt == '5':
        pinprompt()
    return prompt

def pinprompt():
    pin_prompt = int(input('''
                                Please enter your PIN
                                    0. Back
                        '''))
    for account in customers:
        if pin_prompt == account[1]:
            pass
        else:
            print('Invalid PIN')
            sys.exit()
    if pin_prompt == '0':
        home()
    return pin_prompt


def airtime():
    prompt = input('''
                        1. Airtime-Self
                        2. Airtime-Others
                    ''')
    if prompt == '1':
        airtime_amount()
    if prompt == '2':
        destination()
        airtime_amount()
    return prompt

def airtime_amount():
    prompt = input('''
                        Please enter amount (50 - 10000)
                        00. Back
                        0. Main
                    ''')
    if prompt == '00':
        airtime()
    elif prompt == '0':
        home()
    elif int(prompt) < 50 or int(prompt) > 10000:
        wrongamount()
    else:
        processed()
    return prompt

def wrongamount():
    wrongamountPrompt = int(input('''
                                    You have entered the wrong amount. Please enter values
                                                from 50 to 10000
                            '''))
    if wrongamountPrompt < 50 or wrongamountPrompt > 10000:
        wrongamount()
    else:
        processed()
    return wrongamountPrompt

def data():
    prompt = input('''
                        1. Data-Self
                        2. Data-Others
                    ''')
    if prompt == '1':
        data_amount()
    if prompt == '2':
        destination()
        data_amount()
    return prompt

def data_amount():
    prompt = input('''
                        Please select
                            1. 1GB(Night5Days) N100
                            2. 150MB(1day) N100
                            3. 2.9GB(30days) N1000
                            4. N10000 Oneoff(50GB) N10000
                            5. 50GB(30days) N10000
                                    6. Next
                                    00. Back
                                    0. Main
                ''')
    if prompt == '1':
        processed()
    if prompt == '2':
        processed()
    if prompt == '3':
        processed()
    if prompt == '4':
        processed()
    if prompt == '5':
        processed()
    if prompt == '6':
        Data_Next()
    if prompt == '00':
        pinprompt()
        data()
    if prompt == '0':
        home()
    return prompt

def Data_Next():
    next = input('''
                        1. GloMega100000 oneoff(1TB) N100000
                        2. 5GB(30Days) N1100
                        3. 4.1GB(30Days) N1500
                        4. 7GB(7Days) N1500
                        5. N15000 Oneoff(93GB) N15000
                                00. Back
                                0. Main
                ''')
    if next == 1:
        processed()
    if next == '2':
        processed()
    if next == '3':
        processed()
    if next == '4':
        processed()
    if next == '5':
        processed()
    if next == '00':
        pinprompt()
        data()
    if next == '0':
        home()
    return next

def destination():
    destination_num = input('''
                                    Please enter destination phone line
                                            00. Back
                                            0. Main
                                ''')
    if destination_num == '00':
        data()
    elif destination_num == '0':
        home()
    else:
        pass


def processed():
    print('Transaction is being processed.')


register()