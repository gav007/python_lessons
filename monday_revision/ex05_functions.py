def parser(line):
    clean_line = line.strip().split()
    device = clean_line[0]
    status = clean_line[1]
    return device, status

devices = {}
broken_lines = 0

with open("messy_devices.txt", "r") as file:
    for line in file:
        try:
            device, status = parser(line)
            devices[device] = status
        except IndexError:
            broken_lines += 1


print("Done Processing")
print("Line issues", broken_lines)
