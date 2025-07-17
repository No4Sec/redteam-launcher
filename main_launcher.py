#!/usr/bin/env python3
import os
import subprocess
import time
from colorama import init, Fore, Style

init(autoreset=True)

# ----- Loading Effect -----
def loading():
    print(Fore.LIGHTMAGENTA_EX + "[*] Initializing NOSEC Red Team Launcher", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")

# ----- NOSEC Logo -----
def show_main_logo():
    logo = f"""
{Fore.RED}░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░  
{Fore.RED}░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
{Fore.RED}░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░        
{Fore.RED}░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓██████▓▒░░▒▓█▓▒░        
{Fore.RED}░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░        
{Fore.RED}░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
{Fore.RED}░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓██████▓▒░ 

        {Fore.LIGHTBLACK_EX}Red Team Launcher by NOSEC 🐍
"""
    print(logo)

# ----- Main Menu -----
def main_menu():
    print(Fore.YELLOW + """
[MAIN MENU]
1) Privilege Escalation Launcher
2) Recon Launcher
3) WinRemote Launcher
4) Quit
""" + Style.RESET_ALL)

# ----- Main Function -----
def main():
    loading()
    show_main_logo()
    while True:
        main_menu()
        choice = input(Fore.CYAN + "Choose a launcher: " + Style.RESET_ALL).strip()
        if choice == "1":
            subprocess.call(["python3", "launcher.py"])
        elif choice == "2":
            subprocess.call(["python3", "recon_launcher.py"])
        elif choice == "3":
            subprocess.call(["python3", "winremote-launcher.py"])
        elif choice == "4":
            print(Fore.LIGHTBLACK_EX + "[*] Exiting. Stay stealthy." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "[!] Invalid choice." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
