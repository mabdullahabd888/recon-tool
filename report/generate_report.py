from datetime import datetime

def save_report(domain, content):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"output/{domain}_report_{now}.txt"
    with open(filename, "w") as f:
        f.write(content)
    print(f"[+] Report saved to {filename}")
