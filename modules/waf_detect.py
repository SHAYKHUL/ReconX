import requests

def run(target):
    print("\n[+] WAF Detection")
    url = f"http://{target}"
    try:
        r = requests.get(url, timeout=5)
        headers = r.headers

        waf_headers = ['X-Sucuri', 'X-Akamai', 'X-CDN', 'Server']

        for h in waf_headers:
            if h in headers:
                print(f"    - WAF Header Detected: {h} -> {headers[h]}")
                return

        print("    - No obvious WAF detected.")
    except Exception as e:
        print(f"    - Error: {str(e)}")
