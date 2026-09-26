inter={}

with open("interfaces.txt", "r") as file:
    for line in file:
        clean_line = line.strip().split()
        interface = clean_line[0]
        ip = clean_line[2]
        inter[interface]=ip

print(inter)
