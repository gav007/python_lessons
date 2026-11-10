#!/usr/bin/env python3
"""
Lesson 7 - Exercise 2: TCP SERVER (receives a message)
======================================================
Picture: the server is a SHOP PHONE.
    make the phone -> give it a number -> plug it in -> wait for a ring -> pick up -> listen -> hang up

Run me FIRST, in terminal 1:   python3 01_tcp_server.py
Then run 02_tcp_client.py in terminal 2.
Stop me with Ctrl+C.
"""
import socket   # Python's built-in networking toolbox


def main():
    server_ip = "127.0.0.1"   # 127.0.0.1 = "this same computer" (loopback). "" would mean ANY network card
    server_port = 6000        # the "phone number" of this program. Pick one above 1024 (below needs root)

    # 1) MAKE THE PHONE
    #    AF_INET     = use IPv4 addresses
    #    SOCK_STREAM = use TCP (a reliable, in-order stream). SOCK_DGRAM would be UDP.
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # (optional but handy) lets you restart the server straight away,
    # instead of getting "Address already in use" for about a minute after stopping it
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2) GIVE IT A NUMBER - an address is ALWAYS a 2-tuple: (ip, port)  <- note the double brackets
    server_sock.bind((server_ip, server_port))

    # 3) PLUG IT IN - tell the OS "I'm ready for calls".
    #    1 = backlog = how many callers may wait in the queue while I'm busy
    server_sock.listen(1)
    print(f"Server listening on {server_ip}:{server_port} ...")

    while True:   # a server runs forever, one caller after another
        # 4) WAIT FOR A RING AND PICK UP
        #    accept() BLOCKS (freezes here) until a client connects.
        #    It returns TWO things:
        #       conn_sock = a BRAND NEW socket just for this one caller (the "line")
        #       addr      = who is calling, as (their_ip, their_port)
        #    server_sock stays free to take the NEXT call.   <- the key idea of Lesson 7
        conn_sock, addr = server_sock.accept()
        print("Client connected from", addr)

        # 5) LISTEN - receive up to 1024 bytes.
        #    The network only carries BYTES, so decode() turns them back into a str.
        data = conn_sock.recv(1024)
        print("Received:", data.decode("utf-8"))

        # extra info the lab asks about
        print("  client address (peer):", conn_sock.getpeername())   # their ip + the RANDOM port their OS picked
        print("  server address (me):  ", conn_sock.getsockname())   # my ip + 6000

        # 6) HANG UP THIS CALL ONLY - talk and close on conn_sock, never on server_sock
        conn_sock.close()


if __name__ == "__main__":
    main()
