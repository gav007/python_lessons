ip_list = []

with open("random_ips.txt", "r") as file:
    for line in file:
        ip = line.strip()
        ip_list.append(ip)

ip_count = 0

for ip in ip_list:
    ip_count += 1

unique = set(ip_list)

unique_count = 0

for ip in unique:
    unique_count += 1

print("IP's", ip_count)
print("Unique IP's", unique_count)
