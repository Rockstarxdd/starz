# Note - All Credits Goes To Astra - It's Just Advanced Version Of Astra
# © Astra

import os

os.system("pip3 install git+git://github.com/SpEcHiDe/Telethon@72afe59#egg=telethon")
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep

init()

n = Fore.RESET
LE = Fore.LIGHTGREEN_EX
FR = Fore.RED
FW = Fore.WHITE
FC = Fore.CYAN
FY = Fore.YELLOW
colors = [LE, FR, FW, FC, FY]

lg = LE
r = FR
cy = FC
ye = FY
w = FW

try:
    import requests
except ImportError:
    print(f'{FR}[i] Installing Modules - Requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    #             Stylish
    print(f"""
░█████╗░██╗░░░░░░█████╗░██╗███╗░░██╗  
██╔══██╗██║░░░░░██╔══██╗██║████╗░██║  
███████║██║░░░░░███████║██║██╔██╗██║  
██╔══██║██║░░░░░██╔══██║██║██║╚████║  
██║░░██║███████╗██║░░██║██║██║░╚███║  
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝  
░██████╗░█████╗░██████╗░░█████╗░██████╗░██████╗░███████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝██████╔╝█████╗░░
░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔═══╝░██╔══╝░░
██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░██║░░░░░███████╗
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░╚══════╝
{cy}                                           
{cy}          Version : 1.01                   
{cy}                                 By @Rockstar_xdd    
{cy}                                               
 {r}If any one try to Sell you this script
   {lg}Contact me on telegram @Rockstar_xdd
        """)

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(r+'[1] Add Accounts'+n)
    print(cy+'[2] Check Banned 🚫 Accounts'+n)
    print(ye+'[3] Remove Any Account From Script'+n)
    print(w+'[4] Exit'+n)
    a = int(input('\nEnter Any Input (1/2/3/4): '))
    if a == 1:
        new_accs = []
        with open('vars.txt', 'ab') as g:
            number_to_add = int(input(f'\n{lg} [~] Enter number of accounts to add: {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{lg} [~] Enter Phone Number: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{lg} [i] Done Saved All Accounts.')
            clr()
            print(f'\n{lg} [*] Trying To Login From Accounts.\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                c.start(number)
                print(f'{lg}[+] Logged In {c}')
                c.disconnect()
            input(f'\nPress Enter To Exit...')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] Unable To Find Any Accounts, Please Add Some Accounts And Try Again!\n\n© By @Alain_xD')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Enter the code: '))
                        print(f'{lg}[+] {phone} - Not Banned!{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' Is Banned 🚫!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Congo, No Accounts Banned!')
                input('\nPress Enter To Exit...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] I Have Removed All Banned Accounts..\n\n© By @Alain_xD'+n)
                input('\nPress Enter To Exit...')

    elif a == 3:

        accs = []

        f = open('vars.txt', 'rb')

        while True:

            try:

                accs.append(pickle.load(f))

            except EOFError:

                break

        f.close()

        i = 0

        print(f'{lg}[i] Choose Any Account To Remove\n')

        for acc in accs:

            print(f'{lg}[{i}] {acc[0]}{n}')

            i += 1

        index = int(input(f'\n{lg}[+] Enter Your Choice: {n}'))

        phone = str(accs[index][0])

        session_file = phone + '.session'

        if os.name == 'nt':

            os.system(f'del sessions\\{session_file}')

        else:

            os.system(f'rm sessions/{session_file}')

        del accs[index]

        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Account Deleted{n}')
        input(f'\nPress Enter To Exit...')
        f.close()
    
    elif a == 4:
        clr()
        banner()
        exit()
