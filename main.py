import argparse

def main():
    parser = argparse.ArgumentParser(description="Custom Recon Tool")
    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    parser.add_argument("--whois", action="store_true")
    parser.add_argument("--dns", action="store_true")
    parser.add_argument("--subdomains", action="store_true")
    parser.add_argument("--ports", action="store_true")
    parser.add_argument("--banners", action="store_true")
    parser.add_argument("--tech", action="store_true")
    parser.add_argument("--all", action="store_true")

    args = parser.parse_args()
    domain = args.domain

    # Call modules based on flags
    if args.all or args.whois:
        from modules import whois_lookup
        whois_lookup.run(domain)

    if args.all or args.dns:
        from modules import dns_enum
        dns_enum.run(domain)

    if args.all or args.subdomains:
        from modules import subdomain_enum
        subdomain_enum.run(domain)

    if args.all or args.ports:
        from modules import port_scan
        port_scan.run(domain)

    if args.all or args.banners:
        from modules import banner_grab
        banner_grab.run(domain)

    if args.all or args.tech:
        from modules import tech_detect
        tech_detect.run(domain)

if __name__ == "__main__":
    main()

