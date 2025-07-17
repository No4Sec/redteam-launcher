#!/usr/bin/env python3
import os
import re

paths = ["/root/.bash_history", "/home", "/.bash_history"]

print("[*] Searching for reverse shell commands in histories...")

shells = [
    "nc ", "bash -i", "python -c", "php -r", "socat",
    "0<&196;exec 196<>/dev/tcp", "mkfifo", "curl", "wget"
]

def check_history(path):
    try:
        with open(path, "r") as f:
            for line in f:
                if any(s in line for s in shells):
                    print(f"[+] {path}: {line.strip()}")
    except:
        pass

for base in paths:
    if os.path.isdir(base):
        for user in os.listdir(base):
            check_history(os.path.join(base, user, ".bash_history"))
    else:
        check_history(base)
