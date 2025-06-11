# Red Team Launcher Toolkit

🚨 For educational & authorized penetration testing purposes only.

This toolkit includes:

- Linux privilege escalation helpers
- LinPEAS launcher wrapper
- SUID & sudo privilege checks
- Network and credential discovery tools
- Reverse shell payload helper
- Basic log cleaner

## Usage

```bash
python3 launcher.py
```

## Submodules

For linPEAS integration:

```bash
git submodule add https://github.com/peass-ng/PEASS-ng.git linpeas
```

Then link to:
```bash
linpeas/linPEAS/linpeas.sh
```

## Disclaimer

Use at your own risk. Do **not** deploy on systems without explicit permission.
