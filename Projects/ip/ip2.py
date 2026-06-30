count = 0

for ip in range(0,255):

    if ip % 8 == 0:
        print("Network Address =", ip)
        count += 1
