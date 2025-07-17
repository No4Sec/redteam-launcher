#!/usr/bin/env python3
import subprocess
import os
from colorama import Fore, Style

def run_enum_shares():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(Fore.YELLOW + "\n[+] Enumerating SMB Shares (enum4linux-ng)\n" + Style.RESET_ALL)

    target = input(Fore.CYAN + "Enter the target IP or hostname: " + Style.RESET_ALL).strip()

    try:
        print(f"\n[*] Running enum4linux-ng against {target}...\n")
        subprocess.run(["enum4linux-ng", f"{target}"], check=False)
    except FileNotFoundError:
        print(Fore.RED + "[!] enum4linux-ng not found. Install it from https://github.com/cddmp/enum4linux-ng" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[!] Error during SMB share enumeration: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    run_enum_shares()
