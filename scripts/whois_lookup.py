#!/usr/bin/env python3
import subprocess
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    domain = input(f"{Fore.CYAN}Enter domain (e.g. example.com): {Style.RESET_ALL}").strip()
    if not domain:
        print(f"{Fore.RED}[-] No domain provided. Exiting.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.LIGHTBLUE_EX}[*] Performing WHOIS lookup on {domain}...{Style.RESET_ALL}")
    
    try:
        subprocess.run(["whois", domain], check=True)
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}[-] WHOIS query failed.{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}[-] 'whois' command not found. Install it with: sudo apt install whois{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
