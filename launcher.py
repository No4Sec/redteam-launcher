#!/usr/bin/env python3
import subprocess
import sys
import os
import time
import itertools
import threading
from colorama import init, Fore, Style

init(autoreset=True)

# ----- Spinner loading -----
def spinner(text="Loading Privilege Escalation Toolkit...", delay=0.1, duration=2.5):
    done = False

    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            print(f'\r[•] {text} {c}', end='', flush=True)
            time.sleep(delay)

    t = threading.Thread(target=animate)
    t.start()
    time.sleep(duration)
    done = True
    t.join()
    print('\r[✔] Privilege Escalation Toolkit Ready.     ')

# ----- NOSEC Box Logo -----
def show_logo():
    print(f"""{Fore.BLUE}
╔══════════════════════════════╗
║  PRIVILEGE ESCALATION v2     ║
║         by NOSEC 🐍          ║
╚══════════════════════════════╝
""")

# ----- Menu -----
def menu():
    print(Fore.YELLOW + """
[*] Red Team Script Launcher
1) Privilege Escalation
2) Credential Hunting
3) Network Discovery
4) Reverse Shell Injector
5) Log Cleaner
6) SUID Checker
7) LinPEAS Launcher
8) Sudo Checker
9) Sensitive File Finder
10) Reverse Shell Collector
11) Quit
""" + Style.RESET_ALL)

# ----- Run selected script -----
def run_script(script_path):
    if os.path.exists(script_path):
        if script_path.endswith(".sh"):
            subprocess.call(['bash', script_path])
        else:
            subprocess.call(['python3', script_path])
    else:
        print(Fore.RED + f"[!] Script not found: {script_path}" + Style.RESET_ALL)

# ----- Main -----
def main():
    spinner()
    show_logo()
    while True:
        menu()
        choice = input(Fore.CYAN + "Choose a script to run: " + Style.RESET_ALL).strip()
        if choice == "1":
            run_script("scripts/priv_esc_linux.py")
        elif choice == "2":
            run_script("scripts/creds_hunter.py")
        elif choice == "3":
            run_script("scripts/network_enum.py")
        elif choice == "4":
            run_script("scripts/reverse_shell.py")
        elif choice == "5":
            run_script("scripts/log_cleaner.py")
        elif choice == "6":
            run_script("scripts/suidchecker.py")
        elif choice == "7":
            run_script("scripts/linpeas_launcher.sh")
        elif choice == "8":
            run_script("scripts/sudo_checker.sh")
        elif choice == "9":
            run_script("scripts/find_sensitive_files.py")
        elif choice == "10":
            run_script("scripts/shells_collector.py")   
        elif choice == "11":     
            print(Fore.LIGHTBLACK_EX + "[*] Exiting. Stay stealthy." + Style.RESET_ALL)
            sys.exit(0)
        else:
            print(Fore.RED + "[!] Invalid choice." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
