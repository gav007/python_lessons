import subprocess

def list_contents():
    """ Lists contents in the current directory """
    
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
    
    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr
    
def print_directory():
    """ Lists the actual directory """
    
    result = subprocess.run(["pwd"], capture_output=True, text=True)
    
    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr
    
def show_user():
    """ Lists the actual user """
    
    result = subprocess.run(["whoami"], capture_output=True, text=True)
    
    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr
    
def show_network():
    """ Lists the network details """
    
    result = subprocess.run(["ip","addr"], capture_output=True, text=True)
    
    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr
    
def show_network():
    """ Ping a Network """
    
    ip = input("Enter ip address: ")
    
    result = subprocess.run(["ping","-c", "4", ip], capture_output=True, text=True)
    
    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr
    

def main():
    
    print(list_contents())
    print(print_directory())
    print(show_user())
    print(show_network())
    
if __name__ == "__main__":
    main()