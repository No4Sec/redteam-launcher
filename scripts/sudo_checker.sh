#!/bin/bash
echo "[*] Running sudo -l..."
sudo -l > /tmp/sudo_check.log 2>/dev/null

echo "[*] Analyzing sudo -l output..."

if grep -q "NOPASSWD" /tmp/sudo_check.log; then
    echo "[+] Found NOPASSWD sudo rule:"
    grep "NOPASSWD" /tmp/sudo_check.log
else
    echo "[-] No NOPASSWD rules found."
fi

echo "[*] Full sudo -l output saved to /tmp/sudo_check.log"
