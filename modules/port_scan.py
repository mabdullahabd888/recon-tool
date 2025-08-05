import socket

def run(domain):
    print(f"\n[+] Port Scan on {domain}")
    ports = [21, 22, 80, 443, 8080]
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((domain, port))
            print(f"[+] Port {port} is OPEN")
            sock.close()
        except:
            pass
