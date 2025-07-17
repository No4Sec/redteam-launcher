#!/usr/bin/env python3
import subprocess
import os
from colorama import Fore, Style

def run_rpcdump_enum():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(Fore.YELLOW + "\n[+] RPC Dump Enumeration (Impacket)\n" + Style.RESET_ALL)

    target = input(Fore.CYAN + "Enter the target IP or hostname: " + Style.RESET_ALL).strip()

    try:
        print(f"\n[*] Running rpcdump.py against {target}...\n")
        subprocess.run(["rpcdump.py", f"{target}"], check=False)
    except FileNotFoundError:
        print(Fore.RED + "[!] rpcdump.py not found. Make sure Impacket is installed and in PATH." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[!] Error during RPC enum: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    run_rpcdump_enum()
