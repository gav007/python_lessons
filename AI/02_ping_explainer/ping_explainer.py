# Idea is to use subprocess to get ping
# Later model will analysis ping output

import subprocess

def get_host():
    host = input("Enter the IP of the host >> ")
    return host

def run_ping(host):
    results = subprocess.run(["ping", "-c", "4", host],
                             capture_output=True,
                             text=True
                             )

    if results.returncode == 0:
        ping_output = results.stdout
        return ping_output
    else:
        ping_output = results.stderr
        return ping_output

def print_ping(ping_results):
    print()
    print("PING RESULTS")
    print()
    print(ping_results)


def main():
    
    # get ip address and save

    host = get_host()

    # run ping with saved results

    ping_out = run_ping(host)

    # print_results

    ping_print = print_ping(ping_out)

if __name__ == "__main__":
    main()

