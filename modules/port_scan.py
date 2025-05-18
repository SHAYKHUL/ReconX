import socket

top_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]

def run(target):
    print("\n[+] Port Scan (Top Ports)")
    for port in top_ports:
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((target, port))
            print(f"    - Port {port}: OPEN")
            s.close()
        except:
            pass
