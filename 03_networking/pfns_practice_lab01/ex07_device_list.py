
devices = [
    ("R1", "10.0.0.1", "up"),
    ("R2", "10.0.0.2", "down"),
    ("SW1", "10.0.0.3", "up"),
    ("SW2", "10.0.0.4", "up"),
    ("SW3", "10.0.0.5", "down"),
    ("AP1", "10.0.1.1", "up"),
    ("AP2", "10.0.1.2", "up"),
    ("AP3", "10.0.1.3", "down"),
    ("FW1", "10.0.2.1", "up"),
    ("FW2", "10.0.2.2", "down"),
    ("SRV1", "10.0.3.10", "up"),
    ("SRV2", "10.0.3.11", "up"),
    ("SRV3", "10.0.3.12", "down"),
    ("PRN1", "10.0.4.20", "up"),
    ("PRN2", "10.0.4.21", "down"),
    ("CAM1", "10.0.5.30", "up"),
    ("CAM2", "10.0.5.31", "up"),
    ("CAM3", "10.0.5.32", "down"),
    ("WLC1", "10.0.6.40", "up"),
    ("WLC2", "10.0.6.41", "down"),
]

online = 0

for device, ip, status in devices:
    if status.lower()=="up":
        online += 1
    print(f"{device} - {ip} - {status}")
print("Online Devices", online)
