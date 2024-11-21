import requests
import mechanize
import getpass
import json
import random
import time
from datetime import datetime
from bs4 import BeautifulSoup 
from colorama import Fore, Style
from rich.panel import Panel
from platform import system
import os, platform, binascii, sys, _socket, ssl, certifi, zlib, json, uuid
from os import system as sh
from time import sleep

#os.system("xdg-open https://www.facebook.com/Raj.Thakur.Tricker.Youtuber")
time.sleep(1)
os.system('clear')
logo =("""\x1b[1;36m 




\033[1;33m/$$      /$$ /$$$$$$$     
\033[1;32m| $$$    /$$$| $$__  $$    
\033[1;36m| $$$$  /$$$$| $$  \ $$    
\033[1;36m| $$ $$/$$ $$| $$$$$$$/    
\033[1;33m| $$  $$$| $$| $$__  $$    
\033[1;35m| $$\  $ | $$| $$  \ $$    
\033[1;34m| $$ \/  | $$| $$  | $$ /$$\ 
\033[1;37m|__/     |__/|__/  |__/ |__/


               \033[1;36m$$$$$$$\   $$$$$$\     $$$$$\ 
               \033[1;36m$$  __$$\ $$  __$$\    \__$$ |
               \033[1;34m$$ |  $$ |$$ /  $$ |      $$ |
               \033[1;34m$$$$$$$  |$$$$$$$$ |      $$ |
               \033[1;36m$$  __$$< $$  __$$ |$$\   $$ |
               \033[1;32m$$ |  $$ |$$ |  $$ |$$ |  $$ |
               \033[1;33m$$ |  $$ |$$ |  $$ |\$$$$$$  |
               \033[1;33m\__|  \__|\__|  \__| \______/ 
                                                                     




â•”â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•—
â•‘\033[1;31mN4M3        : MR RAJ THAK9R 
â•‘\033[1;32mRULL3X     : UP FIRE RUL3X
â•‘\033[1;34mBR9ND      : MR D R9J  H3R3
â•‘\033[1;37mGitHub       : https://github.com/Raj-Thakur420
â•‘\033[1;32mWH9TS99P N0. : +994 405322645
â•šâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•




â•”â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•—
â•‘\033[1;34mJalwa'   :Jay Shree Ram_____3:)
â•‘\033[1;37mCommants+Page wall multy ___3:) 
â•šâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•""" )
# Print the logo
print(Fore. CYAN + logo +  Style.RESET_ALL)



# Prompt Password 
def pas():
    print('\u001b[37m' + '\x1b[1;32mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')
    password = input("\033[1;32mð—£ð—”ð—¦ð—¦ð—ªð—¢ð—¥ð——âžœ  ") 
    print('\x1b[1;35mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')
    mmm = requests.get('https://pastebin.com/raw/f2pT27HR').text

    if mmm not in password:
        print('\033[1;33m.âžœð—œð—¡ð—–ð—¢ð—¥ð—¥ð—˜ð—–ð—§ ð—£ð—”ð—¦ð—¦ð—ªð—˜ð—¥ð——!')
        sys.exit()
        
pas()

# Prompt for token file
token_file = input("\033[1;30mâžœð—˜ð—¡ð—§ð—˜ð—¥ ð—§ð—¢ð—žð—˜ð—¡ ð—™ð—œð—Ÿð—˜ ð—£ð—”ð—§ð—› : ")
print('\x1b[1;36mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')

# Read access token IDs from file
with open(token_file, 'r') as f:
    access_tokens = f.read().splitlines()

# Prompt for the number of user IDs
num_user_ids = int(input("\033[1;36m.âžœð—•ð—¦ð——ð—ž ð—žð—œð—§ð—¡ð—œ ð—£ð—¢ð—¦ð—§ ð—£ð—˜ ð—§ð—¢ð—¢ð—Ÿð—¦ ð—Ÿð—šð—”ð—¡ð—”  ð—–ð—›ð—”ð—›ð—œð—§ð—˜ð—¡ ð—›ð—¢ ð—ªð—¢ ð——ð—”ð—Ÿð—œ : "))
print('\x1b[1;33mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')

# Define the user IDs and message files
user_messages = {}
haters_name = {} 

# Prompt for user IDs and message files
for i in range(num_user_ids):
    user_id = input(f"\033[1;34mð—˜ð—¡ð—§ð—˜ð—¥ ð—£0ð—¦ð—§ ð—œð—— ð—¡ð—¨ð— ð—•ð—˜ð—¥ #{i+1} : ")
    print('\x1b[1;32mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')
    hater_name = input(f"\033[1;35m.ð—˜ð—¡ð—§ð—˜ð—¥ ð—›ð—”ð—§ð—§ð—˜ð—¥ð—¦ ð—¡ð—”ð— ð—˜ {user_id} : ")
    print('\x1b[1;35mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')
    haters_name[user_id] = hater_name
    message_file = input(f"\033[1;34mð—˜ð—¡ð—§ð—˜ð—¥ ð— ð—˜ð—”ð—¦ð—¦ð—šð—˜ ð—™ð—œð—Ÿð—˜ ð—¡ð—£ {user_id} : ")
    print('\x1b[1;36mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')
    user_messages[user_id] = message_file




# Prompt for delay time in messages
delay_time = int(input("\033[1;34mð—˜ð—¡ð—§ð—˜ð—¥ ð——ð—˜ð—Ÿð—”ð—¬ /ð—§ð—œð— ð—˜ (in seconds) ð—™ð—¢ð—¥ ð— ð—˜ð—¦ð—¦ð—”ð—šð—˜ð—¦ : "))
print('\x1b[1;33mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')

# Prompt for delay before repeating the process
repeat_delay = int(input("\033[1;36mð—˜ð—¡ð—§ð—˜ð—¥  ð——ð—˜ð—Ÿð—”ð—¬/ð—§ð—œð— ð—˜ (in seconds) ð—•ð—˜ð—™ð—¢ð—¥ð—˜ ð—¥ð—˜ð—£ð—˜ð—”ð—§ð—œð—¡ð—š ð—§ð—›ð—˜  ð—£ð—¥ð—¢ð—–ð—˜ð—¦ð—¦ : "))
print('\x1b[1;34mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')

# Get profile name using an access token
def get_profile_name(access_token):
    url = f'https://graph.facebook.com/v17.0/me?access_token={access_token}'
    response = requests.get(url)
    data = response.json()
    if 'name' in data:
        return data['name']
    return None

# Function to send a message to a user's inbox conversation using an access token
def send_message(access_token, user_id, message):
    url = "https://graph.facebook.com/v15.0/{}/comments".format(user_id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Referer': 'https://www.facebook.com/',
        'Authorization': f'Bearer {access_token}'
    }
    data = {'message': hater_name + ' ' + message}

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'\x1b[1;35mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\n \x1b[1;32m[{current_time}] {Fore.YELLOW}Comment sent successfully to user ID {user_id}: \x1b[1;34m{hater_name + message}\n\x1b[1;35mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')
        return True
    else:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'\x1b[1;33mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\n\x1b[1;32m[{current_time}] \x1b[1;31mError sending comment to user ID {user_id}: \x1b[1;31m{hater_name + message}\n \x1b[1;33mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')
        print(f'\x1b[1;31m[{current_time}] Response content: \x1b[1;31m{response.content.decode()}')
        return False

# Main loop to send messages
while True:
    total_successful_messages = 0
    total_unsuccessful_messages = 0

    # Iterate over the access tokens
    for i, access_token in enumerate(access_tokens):
        try:
            # Login using the access token and get the profile name
            profile_name = get_profile_name(access_token)
            if not profile_name:
                continue

            profile_number = i + 1
            access_token_id = access_token[:4] + '********'

            # Print the profile information
            print(f'\x1b[1;34mProfileâžœ {profile_number} (IDâžœ {access_token_id})âžœ {profile_name}')
            print('\x1b[1;33mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')

            # Iterate over the user IDs and messages
            for user_id, message_file in user_messages.items():
            	
                # Read messages from the message file for the current user ID
                with open(message_file, 'r') as f:
                    messages = f.read().splitlines()

                # Shuffle the messages for the current user
                
                # Get the hater name for the current user ID
                hater_name = haters_name[user_id]


                # Get the messages count for the current user
                messages_count = len(messages)

                # Get the current message index for the user ID
                message_index = i % messages_count

                # Get the message for the current index
                message = messages[message_index]

                if send_message(access_token, user_id, message):
                    total_successful_messages += 1
                else:
                    total_unsuccessful_messages+= 1

                time.sleep(delay_time)  # Delay between each message
            # Print Facebook ID, message, and current date/time after message is sent
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'\x1b[1;32mð—™ð—”ð—–ð—˜ð—•ð—¢ð—¢ð—ž ð—œð—— âžœ: {user_id}')
            print('\x1b[1;36mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')
            print('\x1b[1;32mð’™âžœð—¡ð—˜ð—«ð—§ ð—œð—— ð—¥ð—˜ð—”ð——ð—¬ ð—§ð—¢ ð—¦ð—˜ð—¡ð—— ð—–ð—¢ð— ð— ð—˜ð—¡ð—§')
            print('\x1b[1;33mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')

        except requests.exceptions.RequestException as e:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'\x1b[1;31m[{current_time}] Internet disconnected. Reconnecting in 10 seconds...{Style.RESET_ALL}')
            time.sleep(10)

        except Exception as e:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'\x1b[1;31m[{current_time}] An error occurred:âžœ {str(e)}{Style.RESET_ALL}')
            continue

    print('\x1b[1;32mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')
    print('\x1b[1;34mAll comments sent. Waiting before repeating the process...')
    print('\x1b[1;36mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')
    time.sleep(delay_time)  # Delay before repeating the process
