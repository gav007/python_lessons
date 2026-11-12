import socket

# create the phone line
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Give the phone a number
s.bind(("", 6000))

# plug it in
s.listen(1)

while True:
    # message
    print("Waiting for the caller....")

    # Wait pick up new socket
    conn, addr = s.accept()

    # Adding the caller
    print("Call from >>", addr)
    
    while True:
        
        # listen for the bytes
        data = conn.recv(1024) 

            # if data false
        if not data:
            break

        # client said ==> bytes ==> str
        print("Client said ==>", data.decode())
            
        # reply with echo
        conn.send(data)

        # close the connection
    conn.close()