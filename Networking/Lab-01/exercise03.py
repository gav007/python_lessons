import statistics
import re

ping_time = []

with open("ping.txt", "r", encoding="utf-16") as file:
    #data = file.read()
    #print(data)

    for line in file:
        times = re.search(r"time=(\d+)ms", line)
        if times:
            ping_time.append(int(times.group(1)))
        lost_match = re.search(r"Lost = (\d+)", line)

        if lost_match:
            lost = int(lost_match.group(1))

        received_match = re.search(r"Received = (\d+)", line)
        if received_match:
            received = int(received_match.group(1))


        

slow_ping = 0

for _ in ping_time:
    if _ > 50:
        slow_ping += 1

print("Ping Report")
print("-----------------")
print("Replied:", received)
print("Timeouts:", lost)
print("Average:", statistics.mean(ping_time))
print("Highest:", max(ping_time))
print("Slow Pings", slow_ping)
