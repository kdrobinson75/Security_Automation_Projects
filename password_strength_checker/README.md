# 🔐 Password Strength Checker

## 📌 Overview
This script analyzes passwords for:
✅ Strength validation (length, uppercase, lowercase, numbers, special characters)  
✅ Detection of **common weak passwords**  
✅ (Optional) Checking against **Have I Been Pwned API** for leaked credentials  

## 🚀 Features
✅ Detects **weak passwords**  
✅ Alerts users of **common passwords**  
✅ Validates **password complexity**  
✅ (Optional) Uses **HIBP API** to check for **breached passwords**  

## 🔧 How to Use
1️⃣ Run the script:
   ```sh
   python password_checker.py

2️⃣ Enter a password to check.
3️⃣ View strength rating & data breach warning (if applicable).

📄 Example Output
Enter a password to check: 123456
❌ Weak: Common password detected. Choose a unique password.
❌ WARNING: This password has been found in 23,000,000+ data breaches!