#!/usr/bin/env python3
import argparse
from modules import dns_lookup, subdomains, port_scan, waf_detect
from utils.banner import print_banner

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="ReconX - Lightweight Recon Toolkit")
    parser.add_argument("-t", "--target", help="Target domain/IP", required=True)
    parser.add_argument("--dns", help="Perform DNS lookup", action="store_true")
    parser.add_argument("--subs", help="Find subdomains", action="store_true")
    parser.add_argument("--ports", help="Scan top ports", action="store_true")
    parser.add_argument("--waf", help="Detect WAF", action="store_true")
    args = parser.parse_args()

    if args.dns:
        dns_lookup.run(args.target)

    if args.subs:
        subdomains.run(args.target)

    if args.ports:
        port_scan.run(args.target)

    if args.waf:
        waf_detect.run(args.target)

if __name__ == "__main__":
    main()
