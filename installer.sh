#!/bin/bash

echo "🧠 NOSEC Red Team Launcher Installer"
echo "--------------------------------------"
sleep 1

# Check for sudo
if [ "$EUID" -ne 0 ]; then
  echo "[!] Please run as root (sudo ./install.sh)"
  exit
fi

echo "[*] Updating package list..."
apt update -y

echo "[*] Installing system dependencies..."
apt install -y python3 python3-pip nmap smbclient nbtscan rpcbind rpcsvc-proto whois curl dnsutils

echo "[*] Installing Python requirements..."
pip3 install colorama

echo "[✔] Installation complete."

# Optional run prompt
read -p "Do you want to launch NOSEC now? (y/n): " choice
if [[ "$choice" == "y" || "$choice" == "Y" ]]; then
  python3 main_launcher.py
else
  echo "[-] You can run the launcher later using: python3 main_launcher.py"
fi

