import getpass
correct_username = 'solomonthang'
correct_pin='384842'
balance=500000
attempts=3
print('\n Welcome to our KBZ ATM system.')
while attempts>0:
    username = input('\n Enter your username...: ')
    pin = getpass.getpass(f'Enter your 6 digits pin...')
    if username == correct_username and pin==correct_pin:
        print(f'\n...Hello {correct_username}.')
        try:
            money=int(input('Enter amount you want: '))
            if money<=balance:
                balance-=money
                print(f'\nSuccess! You have withdrawn {money} Kyats.')
                print(f"Your balance is {balance} Kyats. Thank you for using our system.")
        except ValueError:
            print(f'\n Please input int only!')
        break
    else:
        attempts-=1
        if attempts>0:
            print(f'\nOnly {attempts} times left. Please try again: ')
        else:
            print('\nSorry 3 times incorrect attempts. Attempts are limited for today.')
            
