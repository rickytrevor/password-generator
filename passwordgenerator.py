#why don't you re-write this in c++ aka a superior language to c and no bloat compared to python?

'''

from msilib.schema import Error
import random
import os
import platform
from colorama import *

if "windows" in platform.platform().lower():
  os.system("cls")
else:
  os.system("clear")
def start():
    init(autoreset=True)
    print(f"""{Fore.LIGHTBLUE_EX}
                                                __                             __          
           ___  ___ ____ ____    _____  _______/ / ___ ____ ___  ___ _______ _/ /____  ____
          / _ \/ _ `(_-<(_-< |/|/ / _ \/ __/ _  / / _ `/ -_) _ \/ -_) __/ _ `/ __/ _ \/ __/
         / .__/\_,_/___/___/__,__/\___/_/  \_,_/  \_, /\__/_//_/\__/_/  \_,_/\__/\___/_/   
        /_/                                      /___/                                        
                                                      {Fore.CYAN + Style.BRIGHT} Made by https://github.com/lucadado """)
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    symbols = ":;-_?!.,£$%&/()^*ç°§€<>+#@{[}]"
    upper = letters.upper()
    print("\n\n\n")
    try:
        length = int(input(f"        {Fore.LIGHTBLUE_EX}Password Length: {Fore.RESET}"))
    except ValueError:
        print(f"\n        {Fore.LIGHTRED_EX}Please provide a valid number!")
        back()
    symbask = str(input(f"\n        {Fore.LIGHTBLUE_EX}Do you want symbols? (yes/no): {Fore.RESET}"))
    if symbask.lower() == "yes":        
        total = letters + numbers + upper + symbols
        password = "".join(random.sample(total, length))
        print(f"\n        {Fore.LIGHTBLUE_EX}Password: {Fore.LIGHTYELLOW_EX}{password}")
    elif symbask.lower() == "no":
        total = letters + numbers + upper
        password = "".join(random.sample(total, length))
        print(f"\n        {Fore.LIGHTBLUE_EX}Password: {Fore.LIGHTYELLOW_EX}{password}")
    else:
        print(f"\n        {Fore.LIGHTRED_EX}Please provide a valid answer! (Yes/No)")
        back()    
    # RATING
    if len(password) >= 32:
        print(f"\n        {Fore.LIGHTBLUE_EX}Password Strength: {Fore.MAGENTA}Area51")   
    elif len(password) >= 26:
        print(f"\n        {Fore.LIGHTBLUE_EX}Password Strength: {Fore.LIGHTGREEN_EX}Very Strong")
    elif len(password) >= 20:
        print(f"\n        {Fore.LIGHTBLUE_EX}Password Strength: {Fore.LIGHTGREEN_EX}Strong")
    elif len(password) >= 16:
        print(f"\n        {Fore.LIGHTBLUE_EX}Password Strength: {Fore.GREEN}Good")
    elif len(password) >= 10:
        print(f"\n        {Fore.LIGHTBLUE_EX}Password Strength: {Fore.LIGHTGREEN_EX}Great")
    elif len(password) >= 6:
        print(f"\n        {Fore.LIGHTBLUE_EX}Password Strength: {Fore.LIGHTRED_EX}Weak")
    else:
        print(f"\n        {Fore.LIGHTBLUE_EX}Password Strength: {Fore.RED}Very Weak")
    back()
def back():
    print("\n\n")
    input("        Press enter...")
    if "windows" in platform.platform().lower():
        os.system("cls")
    else:
        os.system("clear")
    start()    
start()

———————————No switches?———————————
⠀⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇
⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀
⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀
⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀
⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
—————————————————————————————
'''
