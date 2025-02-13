import re

# Define the log file path (Example: auth.log for Linux)
LOG_FILE = "auth.log"  # Replace with your log file

# Define a regex pattern to find failed login attempts
failed_login_pattern = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")

def analyze_log(file_path):
    failed_attempts = {}

    with open(file_path, "r") as file:
        for line in file:
            match = failed_login_pattern.search(line)
            if match:
                ip_address = match.group(1)
                if ip_address in failed_attempts:
                    failed_attempts[ip_address] += 1
                else:
                    failed_attempts[ip_address] = 1

    print("\n🔍 Detected Failed Login Attempts:")
    for ip, count in sorted(failed_attempts.items(), key=lambda x: x[1], reverse=True):
        print(f"🔴 {ip} - {count} failed attempts")

if __name__ == "__main__":
    analyze_log(LOG_FILE)
