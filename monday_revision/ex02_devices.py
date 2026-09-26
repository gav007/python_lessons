online = 0
offline = 0
with open("devices.txt", "r") as file:
    for line in file:
        clean_line = line.strip().split()
        device = clean_line[0]
        status = clean_line[1]
        if status.lower() == "up":
            online += 1
        else:
            offline += 1

print("Online", online)
print("Offline", offline)
