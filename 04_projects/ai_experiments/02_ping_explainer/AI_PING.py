# Idea is to use subprocess to get ping
# Later model will analysis ping output
# This one will use the AI to analysis the ping results...

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


def model_explain(result):
    starter_prompt = """You are explaining Linux ping output to a beginner networking student.

    Important rules:
        - RTT values are in milliseconds, not seconds.
        - Do not confuse 'time 3043ms' with RTT.
        - Use the rtt min/avg/max/mdev line for latency.
        - If packet loss is 0%, say the connection looks successful.
        - Keep the answer short and clear."""

    response = subprocess.run(["ollama", "run", "qwen3:0.6b", starter_prompt + " " + result],
                              capture_output=True,
                              text=True
                              )

    if response.returncode == 0:
        model_response = response.stdout
        return model_response
    else:
        model_response = response.stderr
        return model_response

def print_models_response(model_response):

    print()
    print("The AI MODEL SAID")
    print()
    print(model_response)


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

    # give ping to model
    model_out = model_explain(ping_out)

    # output model response
    print_models_response(model_out)


if __name__ == "__main__":
    main()

