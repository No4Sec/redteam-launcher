#!/usr/bin/env python3
import os

print("[*] Checking for SUID binaries...")
os.system("find / -perm -4000 -type f 2>/dev/null")

print("\n[*] Checking for world-writable files...")
os.system("find / -writable -type f 2>/dev/null")

print("\n[*] Done.")
