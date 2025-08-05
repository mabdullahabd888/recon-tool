import whois

def run(domain):
    print(f"\n[+] WHOIS Lookup for {domain}")
    try:
        info = whois.whois(domain)
        for key, value in info.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"[-] WHOIS lookup failed: {e}")
