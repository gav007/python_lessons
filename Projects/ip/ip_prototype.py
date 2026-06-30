# INPUT
get_ip = input("Enter your ip: ")
get_cidr = int(input("Enter CIDR number: "))
TABLE = [128,64,32,16,8,4,2,1]
SUBNET = []


# SPLIT
first_oct,second_oct,third_oct,forth_oct = get_ip.split(".")

submask = 0


# GET INTERESTING OCT SUBMASK
if get_cidr >= 8 and get_cidr <=15:
    interesting_oct = int(second_oct)
    iterations = get_cidr - 8

    for index in TABLE[:iterations]:
        submask += index
    block_size = 256 - submask
    SUBNET = [255, submask, 0, 0]
    print("Subnet Mask =", SUBNET)
    print("Block Size =", block_size)

    for net_address in range(0, 255):
        if net_address % block_size == 0:
            print("-"*30)
            print("Network Address:", net_address)
            print("First Host", net_address + 1)
            
            broadcast = net_address + (block_size - 1)
            print("Last Host:", broadcast - 1)
            print("Broadcast Address:", broadcast)
            

elif get_cidr <= 23:
    interesting_oct = int(third_oct)
    iterations = get_cidr - 16

    for index in TABLE[:iterations]:
        submask += index
    block_size = 256 - submask
    SUBNET = [255, 255, submask, 0]
    print("Subnet Mask =", SUBNET)
    print("Block Size =", block_size)
    
    for net_address in range(0, 255):
        if net_address % block_size == 0:
            print("-"*30)
            print("Network Address:", net_address)
            print("First Host", net_address + 1)

            broadcast = net_address + (block_size - 1)
            print("Last Host:", broadcast - 1)
            print("Broadcast Address:", broadcast)
            

elif get_cidr <= 32:
    interesting_oct = int(forth_oct)
    iterations = get_cidr - 24

    for index in TABLE[:iterations]:
        submask += index
    block_size = 256 - submask
    SUBNET = [255, 255, 255, submask]
    print("Subnet Mask =", SUBNET)
    print("Block Size =", block_size)

    for net_address in range(0, 255):
        if net_address % block_size == 0:
            print("-"*30)
            print("Network Address:", net_address)
            print("First Host", net_address + 1)

            broadcast = net_address + (block_size - 1)
            print("Last Host:", broadcast - 1)
            print("Broadcast Address:", broadcast)

else:
    print("Invalid")

print("Interesting Oct", interesting_oct)


count = 0

for ip in range(0,255):

    if ip % 32 == 0:
        #print("Network Address =", ip)
        count += 1

