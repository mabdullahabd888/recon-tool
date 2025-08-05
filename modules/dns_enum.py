import dns.resolver

def run(domain):
    print(f"\n[+] DNS Enumeration for {domain}")
    records = ['A', 'MX', 'TXT', 'NS']
    for rtype in records:
        try:
            result = dns.resolver.resolve(domain, rtype)
            for rdata in result:
                print(f"{rtype} Record: {rdata.to_text()}")
        except:
            print(f"[-] {rtype} record not found.")
