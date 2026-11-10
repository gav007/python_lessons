import subprocess
import os
import stat
from pathlib import Path 
import socket
from rich import print

def list_contents():
    """ Lists contents in the current directory """
    
    with os.scandir(".") as entries:
        print()
        print("SUMMARY")
        print("----------------------")
        for entry in entries:
            print("Name:", entry.name)
            if entry.is_file():
                print("Type: File")
            if entry.is_dir():
                print("File Type: Dir")
            if entry.stat().st_size > 1000:
                kb = entry.stat().st_size / 1000
                print("Size KB:", round(kb,2))
            else:
                print("Size Bytes:", entry.stat().st_size)
             
            # get permissions    
            mode = entry.stat().st_mode
            permissions = stat.filemode(mode).strip()
            print()
            print("FILE PERMISSIONS")
            # test owner
            owner = ""
            for i in permissions[1:4]:
                owner += i
            
            if "r" in owner:
                read_O = "READ"
            else:
                read_O = "-"
                
            if "w" in owner:
                read_W = "WRITE"
            else:
                read_W = "-"
                
            if "x" in owner:
                read_X = "EXECUTE"
            else:
                read_X = "-"
            
            print(f"OWNER: {read_O}/{read_W}/{read_X}")
            
            # test groups
            group = ""
            for i in permissions[4:7]:
                group += i
            
            if "r" in group:
                group_R = "READ"
            else:
                group_R = "-"
                         
            if "w" in group:
                group_W = "WRITE"
            else:
                group_W = "-"
                
            if "x" in group:
                group_X = "EXECUTE"
            else:
                group_X = "-"
            
            print(f"GROUP: {group_R}/{group_W}/{group_X}")
            
            # Test others
            other = ""
            for i in permissions[7:]:
                other += i
            
            if "r" in other:
                others_R = "READ"
            else:
                others_R = "-"
            
            if "w" in other:
                others_W = "WRITE"
            else:
                others_W = "-"
            
            if "x" in other:
                others_X = "EXECUTE"
            else:
                others_X = "-"
                
            print(f"OTHERS: {others_R}/{others_W}/{others_X}")
                
            print("----------------------")

    
def print_directory():
    """ Lists the actual directory """
    
    current = Path.cwd()
    print()
    print("[bold cyan]CURRENT PATH[/bold cyan]")
    print("---------------")
    print()
    print("[green] - CURRENT >> [/green]", current)
    print()
    print("[bold cyan]CURRENT FOLDER[/bold cyan]")
    print("---------------")
    print()
    print("[green] - FOLDER NAME >>[/green]", current.name)
    print()
    
    
    
    
def show_user():
    """ Lists the actual user """
    
    user = os.environ.get('USER', "Unknown")
    home = os.environ.get("HOME", "unknown")
    print()
    print("[cyan bold]USER INFO[/cyan bold]")
    print()
    print(f" - Current user = [green]{user}[/green]")
    print(f" - Users home directory = [green]{home}[/green]")
    print()
    
    
    
def show_network():
    """ Lists the network details """
    
    result = subprocess.run(["ip","addr"], capture_output=True, text=True)
    
    if result.returncode == 0:
        lines = result.stdout.split()
        return lines
    else:
        return result.stderr
    
def ping_me():
    """ Ping a Network """
    
    ip = input("Enter ip address: ")
    
    result = subprocess.run(["ping","-c", "4", ip], capture_output=True, text=True)
    
    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr
    

def main():
    
    #list_contents()
    #print_directory()
    #show_user()
    print(show_network())
    
if __name__ == "__main__":
    main()