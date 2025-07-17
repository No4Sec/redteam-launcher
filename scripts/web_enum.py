#!/usr/bin/env python3
import subprocess
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def run_command(description, cmd):
    print(f"{Fore.YELLOW}[+] {description}{Style.RESET_ALL}")
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}[-] Failed to run: {cmd}{Style.RESET_ALL}")

def main():
    target = input(f"{Fore.CYAN}Enter target domain or IP (e.g. http://example.com): {Style.RESET_ALL}").strip()
    if not target:
        print(f"{Fore.RED}[-] No target provided. Exiting.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.LIGHTBLUE_EX}[*] Starting web enumeration on {target}{Style.RESET_ALL}\n")

    run_command("Running WhatWeb (fingerprint CMS, server etc)...", f"whatweb {target}")
    run_command("Running Dirb (brute force directories)...", f"dirb {target}")
    run_command("Running Gobuster (faster directory busting)...", f"gobuster dir -u {target} -w /usr/share/wordlists/dirb/common.txt")
    run_command("Running Nikto (vuln scanner)...", f"nikto -h {target}")

    print(f"\n{Fore.GREEN}[+] Web enumeration completed.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
