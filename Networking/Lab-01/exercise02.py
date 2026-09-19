import statistics
import re

ping_time = []

with open("ping.txt", "r", encoding="utf-16") as file:
    #print(file.read())

    for line in file:
        match = re.search(r"time=(\d+)ms", line)
        if match:
            ping_time.append(int(match.group(1)))

# print(ping_time)
length = len(ping_time)
print("Ping Stats")
print("Number of pings", length)
print("Average:", statistics.mean(ping_time), "ms")
print("Median:", statistics.median(ping_time), "ms")
print("Highest:", max(ping_time), "ms")
print("Lowest:", min(ping_time), "ms")        