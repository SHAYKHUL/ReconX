import socket

def run(target):
    print("\n[+] DNS Lookup")
    try:
        ip = socket.gethostbyname(target)
        print(f"    - {target} => {ip}")
    except socket.gaierror:
        print("    - Failed to resolve target.")
