import socket

def run(domain):
    print(f"\n[+] Banner Grabbing on {domain}")
    for port in [80, 443]:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((domain, port))
            sock.send(b"HEAD / HTTP/1.1\r\nHost: " + domain.encode() + b"\r\n\r\n")
            banner = sock.recv(1024)
            print(f"Port {port} Banner:\n{banner.decode(errors='ignore')}")
            sock.close()
        except:
            continue
