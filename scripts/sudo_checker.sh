sudo -l > /tmp/sudo_check.log 2>/dev/null
grep NOPASSWD /tmp/sudo_check.log || echo '[-] No NOPASSWD entries found.'
