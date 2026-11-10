import socket

# make the land line
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# dail the server
c.connect(("127.0.0.1", 6000))

# say high
message = "HELLLLOOO"

# encode the message
c.send(message.encode())

# echo
echo = c.recv(1024).decode("utf-8")

# print message
print(echo)

c.close()

