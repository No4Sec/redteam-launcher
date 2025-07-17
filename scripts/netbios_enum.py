#!/usr/bin/env python3
import subprocess
import shutil
import sys

def netbios_enum(target_ip):
    print(f"\n[+] Running NetBIOS enumeration on {target_ip}...\n")

    if not shutil.which("nbtscan"):
        print("[!] nbtscan is not installed. Use: sudo apt install nbtscan")
        return

    try:
        result = subprocess.run(["nbtscan", "-v", target_ip], capture_output=True, text=True)
        if result.stdout.strip():
            print(result.stdout)
        else:
            print("[!] No NetBIOS response received.")
        input("\n[Press Enter to return to menu]")
    except Exception as e:
        print(f"[!] Error: {e}")
        input("\n[Press Enter to return to menu]")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        target = input("[?] Enter target IP: ").strip()

    netbios_enum(target)
