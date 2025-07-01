import os import subprocess import sys

List of all required pip packages

required_packages = [ "cryptography", "colorama" ]

def install(package): subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if name == "main": print("\n[+] Installing required packages...\n") for package in required_packages: try: import(package) print(f"[✔] {package} already installed.") except ImportError: print(f"[!] {package} not found. Installing...") install(package) print("\n[+] All required packages are installed.\n")

