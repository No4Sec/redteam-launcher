#!/usr/bin/env python3
import os

targets = [
    ".bash_history", "id_rsa", ".env", "config.php",
    "wp-config.php", "credentials", "secrets", "password", "shadow"
]

print("[*] Searching for sensitive files...")

for root, dirs, files in os.walk("/"):
    for file in files:
        for t in targets:
            if t in file.lower():
                print(f"[+] Possible hit: {os.path.join(root, file)}")
