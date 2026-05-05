#!/usr/bin/env python3
"""
parse_alerts.py — Suricata EVE JSON Alert Parser
CodeAlpha Internship Task 4 — Gyuzuk Excellence Johnrok
Reads /var/log/suricata/eve.json and prints a clean alert summary.
"""

import json
import sys
from collections import Counter
from datetime import datetime

LOG_FILE = "/var/log/suricata/eve.json"

def parse_alerts(filepath):
    alerts = []
    try:
        with open(filepath, "r") as f:
            for line in f:
                try:
                    event = json.loads(line.strip())
                    if event.get("event_type") == "alert":
                        alerts.append({
                            "timestamp": event.get("timestamp", ""),
                            "src_ip":    event.get("src_ip", ""),
                            "dest_ip":   event.get("dest_ip", ""),
                            "dest_port": event.get("dest_port", ""),
                            "signature": event["alert"].get("signature", ""),
                            "severity":  event["alert"].get("severity", ""),
                            "category":  event["alert"].get("category", ""),
                        })
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        print(f"[!] Log file not found: {filepath}")
        sys.exit(1)
    return alerts

def print_summary(alerts):
    print("=" * 65)
    print("  SURICATA ALERT SUMMARY")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 65)
    print(f"\n  Total Alerts: {len(alerts)}\n")

    # Top attacking IPs
    src_ips = Counter(a["src_ip"] for a in alerts)
    print("  Top Source IPs:")
    for ip, count in src_ips.most_common(5):
        print(f"    {ip:<20} {count} alert(s)")

    # Top signatures triggered
    sigs = Counter(a["signature"] for a in alerts)
    print("\n  Top Signatures Triggered:")
    for sig, count in sigs.most_common(5):
        print(f"    [{count}] {sig}")

    # Recent 10 alerts
    print("\n  Recent Alerts:")
    print(f"  {'Time':<25} {'Src IP':<18} {'Signature'}")
    print("  " + "-" * 60)
    for a in alerts[-10:]:
        ts = a["timestamp"][:19].replace("T", " ")
        print(f"  {ts:<25} {a['src_ip']:<18} {a['signature'][:35]}")
    print()

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else LOG_FILE
    alerts = parse_alerts(path)
    print_summary(alerts)
