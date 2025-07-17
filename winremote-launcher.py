#!/usr/bin/env python3
import subprocess
import sys
import os
import time
from colorama import init, Fore, Style

init(autoreset=True)

# ----- Loading Animation -----
def loading_animation():
    print(Fore.LIGHTBLACK_EX + "[*] Initializing WinRemote Launcher ", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    time.sleep(0.5)
    print(" Done.\n" + Style.RESET_ALL)

# ----- NOSEC Box Logo -----
def show_logo():
    print(f"""{Fore.BLUE}
╔══════════════════════════════╗
║   WINREMOTE LAUNCHER v1      ║
║         by NOSEC 🧠           ║
╚══════════════════════════════╝
""")

# ----- Menu -----
def menu():
    print(Fore.YELLOW + """
[*] Windows Remote Recon Tools
1) SMB Enumeration
2) NetBIOS Enumeration
3) RPC Dumper
4) Null Session Checker
5) Enum Shares
6) Quit
""" + Style.RESET_ALL)

# ----- Run External Script -----
def run_script(script_path):
    if os.path.exists(script_path):
        subprocess.call(["python3", script_path])
    else:
        print(Fore.RED + f"[!] Script not found: {script_path}" + Style.RESET_ALL)

# ----- Main -----
def main():
    loading_animation()
    show_logo()
    while True:
        menu()
        choice = input(Fore.CYAN + "Choose a script to run: " + Style.RESET_ALL).strip()

        if choice == "1":
            run_script("scripts/smb_enum.py")
        elif choice == "2":
            run_script("scripts/netbios_enum.py")
        elif choice == "3":
            run_script("scripts/win_rpcdump_enum.py")
        elif choice == "4":
            run_script("scripts/win_null_session_check.py")
        elif choice == "5":
            run_script("scripts/win_enum_shares.py")    
        elif choice == "6":
            print(Fore.LIGHTBLACK_EX + "[*] Exiting launcher." + Style.RESET_ALL)
            sys.exit(0)
        else:
            print(Fore.RED + "[!] Invalid choice." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
