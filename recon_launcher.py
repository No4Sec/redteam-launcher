#!/usr/bin/env python3
import subprocess
import os
import sys
from colorama import init, Fore, Style
import time

init(autoreset=True)

def loading_animation(text="Loading"):
    for _ in range(3):
        for dot in ".  .. ...".split():
            print(f"\r{Fore.LIGHTBLACK_EX}{text}{dot}", end="")
            time.sleep(0.3)
    print("\r", end="")

def show_logo():
    print(f"""{Fore.BLUE}
╔══════════════════════════════╗
║      RECON LAUNCHER v1       ║
║         by NOSEC 🛰️          ║
╚══════════════════════════════╝
""")

def menu():
    print(Fore.YELLOW + """
[RECON MODULES]
1) Active Recon
2) Web Enum
3) WhoIs Lookup
4) Quit
""" + Style.RESET_ALL)

def run_script(script_path):
    if os.path.exists(script_path):
        if script_path.endswith(".sh"):
            subprocess.call(['bash', script_path])
        else:
            subprocess.call(['python3', script_path])
    else:
        print(Fore.RED + f"[!] Script not found: {script_path}")

def main():
    loading_animation("Initializing Recon Module")
    show_logo()
    while True:
        menu()
        choice = input(Fore.CYAN + "Choose a module: " + Style.RESET_ALL).strip()
        if choice == "1":
            run_script("scripts/active_recon.py")
        elif choice == "2":
            run_script("scripts/web_enum.py")
        elif choice == "3":
            run_script("scripts/whois_lookup.py")
        elif choice == "4":
            print(Fore.LIGHTBLACK_EX + "[*] Exiting Recon Launcher." + Style.RESET_ALL)
            sys.exit(0)
        else:
            print(Fore.RED + "[!] Invalid choice." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
