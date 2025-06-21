#!/usr/bin/env python3
import os

print("[*] Attempting to clear bash history and logs...")
os.system("history -c")
os.system("rm -f ~/.bash_history")
print("[*] Done.")
# Bash history and syslog clearer
