import requests

def run(domain):
    print("\n[+] Subdomain Enumeration using crt.sh")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        r = requests.get(url, timeout=10)
        json_data = r.json()
        subdomains = sorted({entry['name_value'] for entry in json_data})
        for sub in subdomains:
            print(f"    - {sub}")
    except Exception as e:
        print(f"    - Error: {str(e)}")
