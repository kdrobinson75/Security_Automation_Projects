import re
import hashlib
import requests

HIBP_API_URL = "https://api.pwnedpasswords.com/range/"

# List of commonly used weak passwords
COMMON_PASSWORDS = ["password", "123456", "qwerty", "admin", "letmein", "welcome"]

def check_password_strength(password):
    if len(password) < 8:
        return "❌ Weak: Password too short (must be 8+ characters)"

    if password in COMMON_PASSWORDS:
        return "❌ Weak: Common password detected. Choose a unique password."

    if not re.search(r"[A-Z]", password):
        return "❌ Weak: No uppercase letter (A-Z) included"

    if not re.search(r"[a-z]", password):
        return "❌ Weak: No lowercase letter (a-z) included"

    if not re.search(r"\d", password):
        return "❌ Weak: No number (0-9) included"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "❌ Weak: No special character (!@#$%^&* etc.) included"

    return "✅ Strong Password!"


def check_password_breach(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    first5, remainder = sha1_password[:5], sha1_password[5:]

    response = requests.get(HIBP_API_URL + first5)

    if response.status_code == 200:
        hashes = response.text.splitlines()
        for hash_line in hashes:
            hash_suffix, count = hash_line.split(":")
            if hash_suffix == remainder:
                return f"❌ WARNING: This password has been found in {count} data breaches!"
    return "✅ This password has NOT been found in known breaches."

if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    print(check_password_strength(user_password))
    print(check_password_breach(user_password))