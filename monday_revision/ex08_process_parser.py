with open("processes.txt", "r") as file:
    header = file.readline()
    print(f'{"USER":<12}  {"PID":>6}  {"CPU":>6}  {"MEMORY":>6}  COMMAND')
    highest_cpu = 0

    for line in file:
        clean_line = line.strip().split()
        user = clean_line[0]
        pid = int(clean_line[1])
        cpu = float(clean_line[2])
        memory = float(clean_line[3])
        command = "".join(clean_line[10:])
        if cpu > highest_cpu:
            highest_cpu = cpu
            print(f'{user:<12}  {pid:>6}  {cpu:>6.1f}  {memory:>6.1f}  {command}')
        
