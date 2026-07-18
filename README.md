# Hotspot TTL Bypass Tool

A cross-platform script designed to bypass carrier hotspot data restrictions and bandwidth throttling by adjusting the local network Time to Live (TTL) values.

## Overview

When sharing internet via a mobile hotspot, the smartphone drops the packet TTL value by 1. Cellular carriers inspect this packet metric to identify tethered computer traffic, routing it away from unlimited 5G data tiers and into restricted daily caps.

This utility configures the local device's default IPv4 and IPv6 TTL value to 65. Upon passing through the mobile gateway, the value changes to 64, mimicking native mobile device traffic.

> [!WARNING]
> **Disclaimer:** Bypassing network restrictions may violate user service agreements with your telecom provider. Use this script responsibly.

## Quick Installation

### Linux

Execute the following one-liner in your terminal to fetch and run the script automatically:

```bash
curl -sL https://raw.githubusercontent.com/vaibhavrocxx-coder/unlim5g/refs/heads/main/unlim5g.sh | sudo bash
```

### Windows

Open Windows PowerShell as an Administrator and execute:

```powershell
irm https://raw.githubusercontent.com/vaibhavrocxx-coder/unlim5g/refs/heads/main/unlim5g.ps1 | iex
```

### Manual Execution (Python)

To run the unified script manually using Python, administrative privileges are required.

You can download the raw Python script directly:
* **Raw Link:** [unlim5g.py](https://raw.githubusercontent.com/vaibhavrocxx-coder/unlim5g/refs/heads/main/unlim5g.py)

Or clone or download the script:

```bash
git clone https://github.com/vaibhavrocxx-coder/unlim5g.git
cd unlim5g
```

Run the script:

* **Linux:** `sudo python3 unlim5g.py`
* **Windows:** Run Command Prompt as Administrator, then execute `python unlim5g.py`

## Network Reset

Disconnect from the mobile hotspot, toggle Airplane Mode on your phone for 10 seconds to clear cached connection policies on the cell tower, and reconnect.