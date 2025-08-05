import requests

def run(domain):
    print(f"\n[+] Subdomain Enumeration for {domain}")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        subs = set()
        for entry in data:
            names = entry.get("name_value", "").split("\n")
            for name in names:
                if domain in name:
                    subs.add(name.strip())
        for sub in sorted(subs):
            print(f"  - {sub}")
    except Exception as e:
        print(f"[-] Subdomain check failed: {e}")
