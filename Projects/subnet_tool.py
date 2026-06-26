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
    
    if cidr >=8 and cidr <= 16:
        iterations = cidr - 8
        
        for i in BINARY_TABLE[:iterations]:
            subnet_mask += i
        
        subnet = [255, subnet_mask, 0, 0]
        
        return subnet    
        
    elif cidr >=16 and cidr <= 24:
        iterations = cidr - 16
        
        for i in BINARY_TABLE[:iterations]:
            subnet_mask += i
        
        subnet = [255, 255, subnet_mask, 0]
        
        return subnet  
    
    elif cidr >=24 and cidr <= 32:
        iterations = cidr - 24
        
        for i in BINARY_TABLE[:iterations]:
            subnet_mask += i
        
        subnet = [255, 255, 255, subnet_mask]
        
        return subnet  
        
    
def display_input_summary(first, second, third, fourth, cidr, submask):
    print()
    print("Your Data")
    print("----------------------")
    print(f"{first}.{second}.{third}.{fourth} /{cidr}")
    print()
    print(f"{submask}")
    
     
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
    
    #display ip
    display_input_summary(int_first, int_second, int_third, int_fourth, cidr, submask)
    
    

if __name__ == "__main__":
    main()