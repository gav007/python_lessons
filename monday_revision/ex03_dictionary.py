devices = {}

with open ("devices.txt", "r") as file:
    for line in file:
        clean_line = line.strip().split()
        key = clean_line[0]
        value = clean_line[1]
        devices[key]=value

with open ("device_report.txt", "w") as file:

    for key, value in devices.items():
        file.write(key + " = " + value + "\n")
