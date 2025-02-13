import re
import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the firewall log file (Replace with actual log file)
LOG_FILE = "firewall.log"

# Regex pattern to find blocked IP addresses
blocked_ip_pattern = re.compile(r"Blocked connection from (\d+\.\d+\.\d+\.\d+)")

def analyze_firewall_logs(file_path):
    blocked_ips = {}

    # Read the log file
    try:
        with open(file_path, "r") as file:
            for line in file:
                match = blocked_ip_pattern.search(line)
                if match:
                    ip_address = match.group(1)
                    if ip_address in blocked_ips:
                        blocked_ips[ip_address] += 1
                    else:
                        blocked_ips[ip_address] = 1
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return

    print("\n🔍 Detected Blocked IPs:")
    for ip, count in sorted(blocked_ips.items(), key=lambda x: x[1], reverse=True):
        print(f"🔴 {ip} - Blocked {count} times")

    BRUTE_FORCE_THRESHOLD = 3  # Adjust this value

    print("\n🚨 Potential Brute-Force Attacks:")
    for ip, count in blocked_ips.items():
        if count >= BRUTE_FORCE_THRESHOLD:
            print(f"⚠️  {ip} - Blocked {count} times (Possible brute-force attack!)")

    # Block suspicious IPs
    for ip, count in blocked_ips.items():
        if count >= BRUTE_FORCE_THRESHOLD:
            print(f"🚨 Blocking IP: {ip}")
            os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")  # Linux
            print(f"✅ IP Blocked: {ip}")

    # Create a DataFrame for blocked IPs
    df = pd.DataFrame(list(blocked_ips.items()), columns=["IP Address", "Block Count"])

    # Create a bar chart for blocked IPs
    df.plot(kind="bar", x="IP Address", y="Block Count", color="red", legend=False)
    plt.title("Blocked IPs from Firewall Logs")
    plt.xlabel("IP Address")
    plt.ylabel("Block Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("firewall_visual.png")  # Save visualization
    plt.show()

    # Save results to a CSV file
    df.to_csv("firewall_report.csv", index=False)
    print("\n📄 Report saved to firewall_report.csv")

if __name__ == "__main__":
    analyze_firewall_logs(LOG_FILE)