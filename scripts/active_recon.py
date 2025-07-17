#!/usr/bin/env python3
import subprocess
import os

def nmap_scan(target):
    print(f"\n[*] Starting Nmap scan on {target}...\n")
    cmd = f"nmap -sC -sV -Pn -n -T4 -oN nmap_scan.txt {target}"
    os.system(cmd)

def banner_grabbing(target):
    print(f"\n[*] Running basic banner grabbing on {target}...\n")
    for port in [21, 22, 80, 443, 8080, 3306, 6379]:
        print(f"\n--- Port {port} ---")
        subprocess.call(f"timeout 5 bash -c 'echo -e \"\\n\\n\" | nc -nv {target} {port}'", shell=True)

def service_enum(target):
    print(f"\n[*] Checking for open services using Nmap scripts...\n")
    cmd = f"nmap -p- --script=banner,vuln -T4 -Pn -n -oN service_enum.txt {target}"
    os.system(cmd)

def main():
    target = input("[?] Target IP/Host: ").strip()
    if not target:
        print("[!] Invalid target")
        return
    nmap_scan(target)
    banner_grabbing(target)
    service_enum(target)
    print("\n[+] Recon complete. Output saved in nmap_scan.txt & service_enum.txt")

if __name__ == "__main__":
    main()
