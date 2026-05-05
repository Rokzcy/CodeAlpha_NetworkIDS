# 🛡️ Network Intrusion Detection System (NIDS)
**CodeAlpha Cybersecurity Internship — Task 4**
**Author:** Gyuzuk Excellence Johnrok

---

## Overview
A network-based Intrusion Detection System (NIDS) built using **Suricata** on Ubuntu Linux. The system monitors live network traffic, applies custom and community detection rules, generates alerts for suspicious activity, and parses results for analysis.

---

## Features
- ✅ Suricata IDS configured on a live network interface
- ✅ Emerging Threats open ruleset (thousands of community rules)
- ✅ Custom rules detecting: ping sweeps, port scans, SSH brute force, SQLmap, suspicious DNS
- ✅ EVE JSON structured logging for all alerts
- ✅ Python alert parser with summary statistics
- ✅ Automated setup script for quick deployment

---

## Project Structure


---

## Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_NetworkIDS.git
cd CodeAlpha_NetworkIDS
```

### 2. Run the setup script
```bash
chmod +x setup.sh
./setup.sh
```

### 3. Monitor live alerts
```bash
tail -f /var/log/suricata/fast.log
```

### 4. Parse and summarise alerts
```bash
python3 parse_alerts.py
```

---

## Custom Rules (`rules/local.rules`)
| Rule ID | Detection | Severity |
|---------|-----------|----------|
| 1000001 | ICMP Ping Sweep | Medium |
| 1000002 | Nmap SYN Scan | High |
| 1000003 | SSH Brute Force | High |
| 1000004 | SQLmap User-Agent | High |
| 1000005 | Suspicious DNS (.tk) | Medium |
| 1000006 | Port Scan | High |

---

## Tools Used
- **Suricata** — open-source IDS/IPS engine
- **Emerging Threats Open Rules** — community ruleset
- **Python 3** — alert parsing and analysis
- **iptables** — automated response/blocking

---

## References
- [Suricata Documentation](https://suricata.readthedocs.io)
- [Emerging Threats Rules](https://rules.emergingthreats.net)
- [OWASP Network Security](https://owasp.org)
