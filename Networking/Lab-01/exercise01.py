import re

line = "2: eth0: <BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state UP"

match = re.search(r"mtu\s+(\d+)", line)

if match:
    print(match.group(1))

