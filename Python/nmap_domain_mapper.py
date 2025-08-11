#!/usr/bin/env python3
"""
Nmap Domain Port Mapper
Matches nmap scan results with domain/IP mappings to create a port report per domain.
"""

import re
import sys
import argparse
from typing import Dict, List, Tuple, Set

def parse_domains_file(domains_file: str) -> Dict[str, str]:
    """
    Parse domains.txt file to extract domain -> IP mappings.
    Expected format: domain [A] [IP] [provider]
    
    Returns:
        Dict mapping IP addresses to domain names
    """
    ip_to_domain = {}
    
    try:
        with open(domains_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                # Parse format: domain [A] [IP] [provider]
                match = re.match(r'^(.+?)\s+\[A\]\s+\[(.+?)\]', line)
                if match:
                    domain = match.group(1).strip()
                    ip = match.group(2).strip()
                    ip_to_domain[ip] = domain
                    
    except FileNotFoundError:
        print(f"Error: Could not find domains file: {domains_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error parsing domains file: {e}")
        sys.exit(1)
    
    return ip_to_domain

def parse_nmap_file(nmap_file: str) -> Dict[str, List[Tuple[str, str]]]:
    """
    Parse nmap.txt file to extract IP -> open ports mappings.
    
    Returns:
        Dict mapping IP addresses to list of (port, service) tuples
    """
    ip_to_ports = {}
    current_ip = None
    
    try:
        with open(nmap_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                # Look for scan report lines to get IP
                scan_match = re.match(r'^Nmap scan report for (.+)$', line)
                if scan_match:
                    current_ip = scan_match.group(1).strip()
                    ip_to_ports[current_ip] = []
                    continue
                
                # Look for open port lines
                port_match = re.match(r'^(\d+/\w+)\s+open\s+(.+)$', line)
                if port_match and current_ip:
                    port = port_match.group(1)
                    service = port_match.group(2)
                    ip_to_ports[current_ip].append((port, service))
                    
    except FileNotFoundError:
        print(f"Error: Could not find nmap file: {nmap_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error parsing nmap file: {e}")
        sys.exit(1)
    
    return ip_to_ports

def create_domain_port_report(ip_to_domain: Dict[str, str], 
                            ip_to_ports: Dict[str, List[Tuple[str, str]]]) -> List[str]:
    """
    Create a report mapping domains to their open ports.
    
    Returns:
        List of formatted report lines
    """
    report_lines = []
    report_lines.append("=" * 80)
    report_lines.append("DOMAIN PORT SCAN REPORT")
    report_lines.append("=" * 80)
    report_lines.append("")
    
    # Track statistics
    total_domains_scanned = 0
    total_domains_with_ports = 0
    total_open_ports = 0
    
    # Group by domain
    domain_reports = []
    
    for ip, ports in ip_to_ports.items():
        domain = ip_to_domain.get(ip, f"Unknown ({ip})")
        total_domains_scanned += 1
        
        if ports:
            total_domains_with_ports += 1
            total_open_ports += len(ports)
            
            domain_report = []
            domain_report.append(f"Domain: {domain}")
            domain_report.append(f"IP: {ip}")
            domain_report.append("-" * 40)
            
            for port, service in ports:
                domain_report.append(f"  {port:<12} {service}")
            
            domain_report.append("")
            domain_reports.append("\n".join(domain_report))
        else:
            # Show domains with no open ports if desired
            domain_report = []
            domain_report.append(f"Domain: {domain}")
            domain_report.append(f"IP: {ip}")
            domain_report.append("-" * 40)
            domain_report.append("  No open ports found")
            domain_report.append("")
            domain_reports.append("\n".join(domain_report))
    
    # Add summary statistics
    report_lines.append("SUMMARY:")
    report_lines.append(f"  Total IPs scanned: {total_domains_scanned}")
    report_lines.append(f"  IPs with open ports: {total_domains_with_ports}")
    report_lines.append(f"  Total open ports found: {total_open_ports}")
    report_lines.append("")
    report_lines.append("DETAILED RESULTS:")
    report_lines.append("")
    
    # Add all domain reports
    report_lines.extend(domain_reports)
    
    return report_lines

def create_summary_table(ip_to_domain: Dict[str, str], 
                        ip_to_ports: Dict[str, List[Tuple[str, str]]]) -> List[str]:
    """
    Create a compact summary table.
    """
    table_lines = []
    table_lines.append("=" * 80)
    table_lines.append("QUICK REFERENCE TABLE")
    table_lines.append("=" * 80)
    table_lines.append("")
    table_lines.append(f"{'DOMAIN':<45} {'IP':<16} {'OPEN PORTS'}")
    table_lines.append("-" * 80)
    
    for ip, ports in ip_to_ports.items():
        domain = ip_to_domain.get(ip, f"Unknown ({ip})")
        if ports:
            port_list = ", ".join([port.split('/')[0] for port, _ in ports])
        else:
            port_list = "None"
        
        # Truncate domain if too long
        display_domain = domain[:44] if len(domain) <= 44 else domain[:41] + "..."
        table_lines.append(f"{display_domain:<45} {ip:<16} {port_list}")
    
    table_lines.append("")
    return table_lines

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Match nmap scan results with domain mappings to create a port report per domain.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s domains.txt nmap.txt
  %(prog)s -o custom_report.txt domains.txt nmap.txt
  %(prog)s --output=/tmp/report.txt /path/to/domains.txt /path/to/nmap.txt
        """
    )
    
    parser.add_argument('domains_file', 
                       help='Path to domains file (format: domain [A] [IP] [provider])')
    parser.add_argument('nmap_file', 
                       help='Path to nmap scan results file')
    parser.add_argument('-o', '--output', 
                       default='domain_port_report.txt',
                       help='Output file path (default: domain_port_report.txt)')
    
    return parser.parse_args()

def main():
    """Main function to process files and generate report."""
    
    # Parse command line arguments
    args = parse_arguments()
    domains_file = args.domains_file
    nmap_file = args.nmap_file
    output_file = args.output
    
    print("Parsing domain mappings...")
    ip_to_domain = parse_domains_file(domains_file)
    print(f"Found {len(ip_to_domain)} domain mappings")
    
    print("Parsing nmap scan results...")
    ip_to_ports = parse_nmap_file(nmap_file)
    print(f"Found scan results for {len(ip_to_ports)} IPs")
    
    print("Generating report...")
    
    # Create the full report
    report_lines = create_domain_port_report(ip_to_domain, ip_to_ports)
    
    # Add summary table at the beginning
    summary_lines = create_summary_table(ip_to_domain, ip_to_ports)
    
    # Combine summary and detailed report
    final_report = summary_lines + ["\n"] + report_lines
    
    # Write to output file
    try:
        with open(output_file, 'w') as f:
            f.write("\n".join(final_report))
        print(f"Report written to: {output_file}")
        
        # Also display summary to console
        print("\nQuick Summary:")
        print(f"Total IPs scanned: {len(ip_to_ports)}")
        open_port_ips = sum(1 for ports in ip_to_ports.values() if ports)
        print(f"IPs with open ports: {open_port_ips}")
        total_ports = sum(len(ports) for ports in ip_to_ports.values())
        print(f"Total open ports: {total_ports}")
        
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
