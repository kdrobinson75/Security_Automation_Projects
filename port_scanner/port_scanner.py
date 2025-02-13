import socket

def scan_port(target_host, target_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((target_host, target_port))
        if result == 0:
            print(f"[+] Port {target_port} is open")
        else:
            print(f"[-] Port {target_port} is closed")

if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    ports = [21, 22, 23, 25, 80, 443, 3389]  # Common ports
    for port in ports:
        scan_port(target, port)
