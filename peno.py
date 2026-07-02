#!/usr/bin/env python3
import subprocess

def disclaimer():
    print("="*70)
    print("   Peno - All-in-One Pentest Toolkit")
    print("   DISCLAIMER: Use this tool for LEGAL purposes only.")
    print("   Developer is NOT responsible for illegal use.")
    print("="*70)

# Tool wrappers
def run_theharvester():
    domain = input("Enter domain: ")
    subprocess.run(["theHarvester", "-d", domain, "-l", "100", "-b", "bing"])

def run_nmap():
    target = input("Enter target IP/Domain: ")
    subprocess.run(["nmap", "-A", target])

def run_nikto():
    target = input("Enter target URL: ")
    subprocess.run(["nikto", "-h", target])

def run_sqlmap():
    target = input("Enter target URL: ")
    subprocess.run(["sqlmap", "-u", target, "--batch"])

def run_netcat():
    host = input("Enter host: ")
    port = input("Enter port: ")
    subprocess.run(["nc", host, port])

def run_dradis():
    print("[*] Launching Dradis API client...")
    # Example: replace with your Dradis API call
    subprocess.run(["curl", "-X", "GET", "http://localhost:3000/api/projects"])

# Menu
def main():
    disclaimer()
    tools = {
        "1": run_theharvester,
        "2": run_nmap,
        "3": run_nikto,
        "4": run_sqlmap,
        "5": run_netcat,
        "6": run_dradis
    }

    while True:
        print("\nAvailable Pentest Services:")
        print("1. theHarvester")
        print("2. Nmap (Aggressive Scan)")
        print("3. Nikto (Web Vulnerability Scanner)")
        print("4. SQLmap (SQL Injection Tester)")
        print("5. Netcat (Network Utility)")
        print("6. Dradis (API)")
        choice = input("Enter tool number (or 'q' to quit): ")

        if choice == "q":
            print("Exiting Peno...")
            break
        elif choice in tools:
            tools[choice]()
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
