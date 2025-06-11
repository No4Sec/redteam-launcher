#!/usr/bin/env python3
import subprocess
import sys
import os

def menu():
    print("""
[*] Red Team Script Launcher
1) Privilege Escalation
2) Credential Hunting
3) Network Discovery
4) Reverse Shell Injector
5) Log Cleaner
6) SUID Checker
7) LinPEAS Launcher
8) Sudo Checker
9) Quit
    """)

def run_script(script_path):
    if os.path.exists(script_path):
        if script_path.endswith(".sh"):
            subprocess.call(['bash', script_path])
        else:
            subprocess.call(['python3', script_path])
    else:
        print(f"[!] Script not found: {script_path}")

def main():
    while True:
        menu()
        choice = input("Choose a script to run: ").strip()
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
            print("[*] Exiting.")
            sys.exit(0)
        else:
            print("[!] Invalid choice.")

if __name__ == "__main__":
    main()
