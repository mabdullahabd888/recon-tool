import subprocess

def run(domain):
    print(f"\n[+] Detecting Technologies on {domain}")
    try:
        result = subprocess.run(['whatweb', domain], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"[-] Tech detection failed: {e}")
