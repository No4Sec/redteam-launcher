# 🧠 NOSEC Red Team Launcher

Modular and CTF-ready red team toolkit by NOSEC.  
Includes multiple launchers and plug & play scripts for privilege escalation, reconnaissance, and remote Windows enumeration.

### ⚠️ Usage Scope

- **🛠 Privilege Escalation Launcher**  
  This launcher is for **local use only**.  
  You must **upload it to the target machine** and execute it there for proper functionality.

- **🌐 Recon Launcher** and **🪟 Windows Remote Recon Launcher**  
  These launchers are designed for **remote use**.  
  You can run them directly from your **attack machine** against the target.

---

## 🚀 Features

- 🔥 Modular script launcher system
- 🎯 Local Linux Privilege Escalation Toolkit
- 🌐 Remote Recon Module (Linux & Windows targets)
- 🪟 Windows Remote Recon Toolkit (SMB, NetBIOS, hostname, shares etc.)
- 🖼️ Custom ASCII branding (NOSEC)
- 🎨 Colorized CLI with smooth menus
- 🧩 Easily extendable with new scripts
- 🧠 Fully CTF-Ready

---

## 📁 Structure

nosec-launcher/
├── main_launcher.py
├── launcher.py
├── recon-launcher.py
├── winremote-launcher.py
├── scripts/
│ ├── [ all recon & privesc scripts ]
└── README.md

---

## 🔓 Privilege Escalation Launcher (Working is only local)

1.Privilege Escalation
2.Credential Hunting
3.Network Discovery
4.Reverse Shell Injector
5.Log Cleaner
6.SUID Checker
7.LinPEAS Launcher
8.Sudo Checker
9.Sensitive File Finder
10.Reverse Shell Collector

---

## 🛰️ Recon Launcher


[RECON MODULES]

1.Active Recon
2.Web Enum
3.WhoIs Lookup

---

## 🧠 Windows Remote Recon Launcher

1.SMB Enumeration
2.NetBIOS Enumeration
3.RPC Dumper
4.Null Session Checker
5.Enum Shares

---

## ⚙️ Usage

Run the installer script first to install all required tools and dependencies:

```bash
chmod +x install.sh
sudo ./install.sh
```

Once installed, launch the main menu with:

```bash
python3 main_launcher.py
```

From there, choose between Privilege Escalation, Recon, or Windows Remote modules.




