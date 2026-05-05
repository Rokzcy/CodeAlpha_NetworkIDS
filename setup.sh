#!/bin/bash
# ============================================================
#  Suricata NIDS Setup Script — CodeAlpha Internship Task 4
#  Author: Gyuzuk Excellence Johnrok
# ============================================================

echo "[*] Updating system..."
sudo apt update && sudo apt upgrade -y

echo "[*] Installing Suricata..."
sudo add-apt-repository ppa:oisf/suricata-stable -y
sudo apt update
sudo apt install suricata suricata-update -y

echo "[*] Updating rules..."
sudo suricata-update

echo "[*] Copying custom rules..."
sudo cp rules/local.rules /etc/suricata/rules/local.rules

echo "[*] Testing configuration..."
sudo suricata -T -c /etc/suricata/suricata.yaml -v

echo "[*] Starting Suricata service..."
sudo systemctl enable suricata
sudo systemctl start suricata

echo ""
echo "[✓] Suricata is running! Monitor alerts with:"
echo "    tail -f /var/log/suricata/fast.log"
