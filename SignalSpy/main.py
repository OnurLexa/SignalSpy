import subprocess
import re

def scan_wifi():
    result = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True)
    output = result.stdout

    networks = []
    ssid_pattern = re.compile(r'SSID\s+\d+\s+:\s(.+)')
    signal_pattern = re.compile(r'Signal\s+:\s(\d+)%')

    ssid_matches = ssid_pattern.findall(output)
    signal_matches = signal_pattern.findall(output)

    for ssid, signal in zip(ssid_matches, signal_matches):
        networks.append({"SSID": ssid, "Signal Strength": signal})

    return networks

wifi_networks = scan_wifi()
if wifi_networks:
    print("WiFi ağları ve sinyal güçleri:")
    for network in wifi_networks:
        print(f"SSID: {network['SSID']}, Sinyal Güçü: {network['Signal Strength']}%")
    else:
        print("WiFi ağı bulunamadı.")