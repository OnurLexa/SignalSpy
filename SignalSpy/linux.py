import subprocess
import re

def scan_wifi_linux():
    result = subprocess.run(["iwlist", "wlan0", "scan"], capture_output=True, text=True)
    output = result.stdout

    networks = []
    ssid_pattern = re.compile(r'ESSID:"(.+?)"')
    signal_pattern = re.compile(r'Signal level=(-\d+)')

    ssid_matches = ssid_pattern.findall(output)
    signal_matches = signal_pattern.findall(output)

    for ssid, signal in zip(ssid_matches, signal_matches):
        networks.append({"SSID": ssid, "Signal Strength": signal})

    return networks

wifi_networks = scan_wifi_linux()
if wifi_networks:
    print("WiFi Ağları ve Sinyal Güçleri:")
    for network in wifi_networks:
        print(f"SSID: {network['SSID']} - Sinyal Gücü: {network['Signal Strength']} dBm")
else:
    print("WiFi ağları bulunamadı.")
