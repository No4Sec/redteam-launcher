#!/usr/bin/env python3
import subprocess
import sys

def smb_enum(target_ip):
    print(f"\n[+] Running SMB enumeration on {target_ip}...\n")

    try:
        # List shares
        subprocess.run(["smbclient", "-L", f"//{target_ip}/", "-N"], check=True)
        
        # Try connecting to common shares anonymously
        common_shares = ["IPC$", "ADMIN$", "C$", "Users", "Public"]
        for share in common_shares:
            print(f"\n[*] Trying to access //{target_ip}/{share} anonymously...\n")
            subprocess.run(["smbclient", f"//{target_ip}/{share}", "-N", "-c", "ls"], check=False)
    except Exception as e:
        print(f"[!] Error during SMB enum: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        target = input("[?] Enter target IP: ").strip()

    smb_enum(target)
