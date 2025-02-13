# 🔥 Firewall Log Parser

## 📌 Overview
This script scans **firewall logs** to detect:
✅ Repeated **blocked IPs**  
✅ **Brute-force attack attempts**  
✅ Generates a **CSV report & visualization**  

## 🚀 Features
✅ Detects **frequently blocked IPs**  
✅ Identifies **brute-force attacks**  
✅ Saves results in **firewall_report.csv**  
✅ (Optional) **Generates a visualization**  
✅ (Optional) **Automatically blocks repeat offenders**  

## 🔧 How to Use
1️⃣ Place your **firewall log file** (`firewall.log`) in the same directory.  
2️⃣ Run the script:
   python firewall_log_parser.py
3️⃣ View blocked IPs & brute-force alerts.

📄 Example Output
🔍 Detected Blocked IPs:
🔴 192.168.1.100 - Blocked 3 times
🔴 203.0.113.50 - Blocked 2 times

🚨 Potential Brute-Force Attacks:
⚠️  192.168.1.100 - Blocked 3 times (Possible brute-force attack!)
