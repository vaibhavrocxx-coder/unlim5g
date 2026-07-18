import os
import sys
import platform
import subprocess

def is_admin():
    current_os = platform.system()
    if current_os == "Windows":
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except AttributeError:
            return False
    elif current_os == "Linux":
        return os.geteuid() == 0
    return False

def apply_linux():
    conf_file = "/etc/sysctl.d/99-custom-ttl.conf"
    
    print("===============================")
    print("Applying Hotspot TTL Bypass (Linux)...")
    print("===============================")

    try:
        with open(conf_file, "w") as f:
            f.write("net.ipv4.ip_default_ttl=65\n")
            f.write("net.ipv6.conf.all.hop_limit=65\n")
            f.write("net.ipv6.conf.default.hop_limit=65\n")
    except Exception as e:
        print(f"Error writing to {conf_file}: {e}")
        sys.exit(1)

    print("\nApplying sysctl changes...")
    subprocess.run(["sysctl", "--system"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        with open("/proc/sys/net/ipv4/ip_default_ttl", "r") as f:
            ipv4_check = f.read().strip()
        with open("/proc/sys/net/ipv6/conf/all/hop_limit", "r") as f:
            ipv6_check = f.read().strip()
    except FileNotFoundError:
        ipv4_check = "Unknown"
        ipv6_check = "Unknown"

    return ipv4_check, ipv6_check

def apply_windows():
    print("===============================")
    print("Applying Hotspot TTL Bypass (Windows)...")
    print("===============================")

    subprocess.run(["netsh", "int", "ipv4", "set", "glob", "defaultcurhoplimit=65"], stdout=subprocess.DEVNULL)
    subprocess.run(["netsh", "int", "ipv6", "set", "glob", "defaultcurhoplimit=65"], stdout=subprocess.DEVNULL)

    print("\nApplying changes...")
    try:
        ipv4_check = subprocess.check_output(
            ["powershell", "-Command", "(Get-NetIPv4Protocol).DefaultHopLimit"]
        ).decode("utf-8").strip()
        
        ipv6_check = subprocess.check_output(
            ["powershell", "-Command", "(Get-NetIPv6Protocol).DefaultHopLimit"]
        ).decode("utf-8").strip()
    except subprocess.CalledProcessError:
        ipv4_check = "Unknown"
        ipv6_check = "Unknown"

    return ipv4_check, ipv6_check

def main():
    if not is_admin():
        print("Error: Please run this script with sudo (Linux) or as Administrator (Windows).")
        sys.exit(1)

    current_os = platform.system()
    
    if current_os == "Linux":
        ipv4_check, ipv6_check = apply_linux()
    elif current_os == "Windows":
        ipv4_check, ipv6_check = apply_windows()
    else:
        print(f"Unsupported OS: {current_os}. This script supports Windows and Linux.")
        sys.exit(1)

    print("\nVerification:")
    if ipv4_check == "65" and ipv6_check == "65":
        print(f"Success: IPv4 TTL is {ipv4_check} and IPv6 Hop Limit is {ipv6_check}")
    else:
        print(f"Warning: Values may not have applied correctly. (IPv4: {ipv4_check}, IPv6: {ipv6_check})")

    print("\nPlease disconnect and reconnect to your hotspot.")

if __name__ == "__main__":
    main()