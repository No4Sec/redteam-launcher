#!/usr/bin/env python3
import os

print("[*] Searching for potential credential files...")
os.system("grep -ri 'password' /etc 2>/dev/null | head -n 10")
print("[*] Done.")
