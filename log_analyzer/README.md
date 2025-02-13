# 🔍 Log File Analyzer

## 📌 Overview
This script scans system logs to **detect failed login attempts** and **identify suspicious IP addresses**.

## 🚀 Features
✅ Detects **failed SSH login attempts**  
✅ Generates a **report of suspicious IPs**  
✅ (Optional) **Automatically blocks attackers**  

## 🔧 How to Use
1️⃣ Place your **log file** (`auth.log`) in the same directory.  
2️⃣ Run the script:
   ```sh
   python log_analyzer.py
3️⃣ View the list of suspicious IPs.

📄 Example Output
🔍 Detected Failed Login Attempts:
🔴 203.0.113.50 - 2 failed attempts
🔴 192.168.1.100 - 2 failed attempts