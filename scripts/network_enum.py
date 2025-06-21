#!/usr/bin/env python3
import os

print("[*] Running basic network enumeration...")
os.system("ip a")
os.system("netstat -tulnp")
print("[*] Done.")
# Basic network info
