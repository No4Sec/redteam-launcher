#!/usr/bin/env python3
import os

print("[*] SUID checker started...\n")
exploitables = [
    "nmap", "perl", "python", "ruby", "vim", "find", "bash", "env", "less", "more", "man",
    "socat", "tcpdump", "nano", "cp", "mv", "tar"
]

for suid in os.popen("find / -perm -4000 -type f 2>/dev/null").read().splitlines():
    for bin in exploitables:
        if bin in suid:
            print(f"[+] Potential exploitable SUID: {suid}")

print("\n[*] Check these on https://gtfobins.github.io/")
