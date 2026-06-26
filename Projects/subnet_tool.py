def get_ip():
    ip = input("Enter IP please >> ")

    return ip

def get_CIDR():
    cidr = int(input("Enter CIDR value >> "))

    return cidr

def split_ip(raw_ip):
    first_oct, second_oct, third_oct, fourth_oct = raw_ip.split(".")

    return first_oct, second_oct, third_oct, fourth_oct

def convert_oct(first, second, third, fourth):
    first = int(first)
    second = int(second)
    third = int(third)
    fourth = int(fourth)
    
    return first, second, third, fourth

def get_mask(cidr):
    
    BINARY_TABLE = [128, 64, 32, 16, 8, 4, 2, 1]
    subnet = []
    subnet_mask = 0
    
    if cidr >=8 and cidr <= 15:
        iterations = cidr - 8
        
        for i in BINARY_TABLE[:iterations]:
            subnet_mask += i
        
        subnet = [255, subnet_mask, 0, 0]
        
        return subnet    
        
    elif cidr >= 16 and cidr <= 23:
        iterations = cidr - 16
        
        for i in BINARY_TABLE[:iterations]:
            subnet_mask += i
        
        subnet = [255, 255, subnet_mask, 0]
        
        return subnet  
    
    elif cidr >= 24 and cidr <= 30:
        iterations = cidr - 24
        
        for i in BINARY_TABLE[:iterations]:
            subnet_mask += i
        
        subnet = [255, 255, 255, subnet_mask]
        
        return subnet  

def get_block_info(cidr, submask_list):
    if cidr >= 8 and cidr <= 15:
        interesting_oct = 2
        interesting_mask_value = submask_list[1]
        block_size = 256 - interesting_mask_value  
        
    elif cidr >= 16 and cidr <= 23:
        interesting_oct = 3
        interesting_mask_value = submask_list[2]   
        block_size = 256 - interesting_mask_value  
        
    elif cidr >= 24 and cidr <= 30:
        interesting_oct = 4
        interesting_mask_value = submask_list[3]   
        block_size = 256 - interesting_mask_value  
               
    else:
        print("Not defined at the moment")
        interesting_oct = None
        interesting_mask_value = None
        block_size = 0
    
    return interesting_oct, interesting_mask_value, block_size
        
    
        
       
def format_subnet_mask(submask_list):
    
    string_list = []
    
    for num in submask_list:
        string_list.append(str(num))
        
    submask = ".".join(string_list)
    
    return submask

def display_input_summary(first, second, third, fourth, cidr, submask, interesting_oct, interesting_mask_value, block_size):
    print()
    print("Your Data")
    print("--------------------------------------")
    print(f"IP: {first}.{second}.{third}.{fourth} /{cidr}")
    print()
    print(f"Subnet Mask: {submask}")
    print()
    print(f"Interesting Oct {interesting_oct}")
    print()
    print(f"Interesting Mask Value: {interesting_mask_value}")
    print()
    print(f"Block Size: {block_size}")
    print()
    
    
def get_network_start(block_size):
    network_addresses = []

    if block_size == 0:
        network_addresses.append(0)
    else:
        for ip in range(0, 256, block_size):
            network_addresses.append(ip)

    return network_addresses

def display_network_addresses(first, second, third, network_starts, interesting_oct, block_size):
    print("--------------------------------")
    print("Network Addresses")
    print("--------------------------------")

    if interesting_oct == 4:
        for net_address in network_starts:
            broadcast_num = net_address + block_size -1
            last_num = broadcast_num - 1
            
            ip = f"{first}.{second}.{third}.{net_address}"
            first_ip = f"{first}.{second}.{third}.{net_address + 1}"
            last_ip = f"{first}.{second}.{third}.{last_num}"
            broadcast = f"{first}.{second}.{third}.{broadcast_num}"
            
            print("Network:", ip)
            print(" - First IP:", first_ip)
            print(" - Last IP:", last_ip)
            print(" - Broadcast:", broadcast)
            print()

    elif interesting_oct == 3:
        for net_address in network_starts:
            ip = f"{first}.{second}.{net_address}.0"
            print("-", ip)

    elif interesting_oct == 2:
        for net_address in network_starts:
            ip = f"{first}.{net_address}.0.0"
            print("-", ip)
        
    
    
    
     
def main():
    
    # get the ip
    ip = get_ip()
    
    # get cidr
    cidr = get_CIDR()
    
    # get octs
    first, second, third, fourth = split_ip(ip)
    
    # convert oct
    int_first, int_second, int_third, int_fourth = convert_oct(first, second, third, fourth)
    
    # get subnet mask
    submask = get_mask(cidr)
    
    # format the mask
    mask = format_subnet_mask(submask)
    
    # test
    interesting_oct, interesting_mask_value, block_size = get_block_info(cidr, submask)    
    
    # display ip
    display_input_summary(int_first, int_second, int_third, int_fourth, cidr, mask, interesting_oct, interesting_mask_value,block_size)
    
    # print the network starts
    network_starts = get_network_start(block_size)
    
    # print net addresses
    display_network_addresses(int_first, int_second, int_third, network_starts, interesting_oct, block_size)
    

if __name__ == "__main__":
    main()