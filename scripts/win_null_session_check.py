#!/usr/bin/env python3
import subprocess
import os
from colorama import Fore, Style

def run_null_session_check():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(Fore.YELLOW + "\n[+] NULL Session Check (rpcclient anonymous access)\n" + Style.RESET_ALL)

    target = input(Fore.CYAN + "Enter the target IP or hostname: " + Style.RESET_ALL).strip()

    try:
        print(f"\n[*] Checking anonymous access to {target} via rpcclient...\n")
        subprocess.run(["rpcclient", "-U", "", target], check=False)
    except Exception as e:
        print(Fore.RED + f"[!] Error during NULL session check: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    run_null_session_check()
