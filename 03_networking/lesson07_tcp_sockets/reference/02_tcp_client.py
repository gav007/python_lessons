#!/usr/bin/env python3
"""
Lesson 7 - Exercise 2: TCP CLIENT (sends a message)
===================================================
Picture: the client is YOU RINGING THE SHOP.
    make a phone -> dial the number -> talk -> hang up

Start 01_tcp_server.py first, then run me:   python3 02_tcp_client.py
"""
import socket


def main():
    message = "Hello from client"
    server_ip = "127.0.0.1"   # must match where the server is
    server_port = 6000        # must match the server's bind() port, or you get "Connection refused"

    # Step 1 - MAKE A PHONE (same two settings as the server: IPv4 + TCP)
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Step 2 - DIAL. connect() does the TCP 3-way handshake (SYN, SYN-ACK, ACK) for you.
    #          The client does NOT bind: the OS gives it a random port (e.g. 54321) automatically.
    client_sock.connect((server_ip, server_port))

    # Step 3 - TALK. str -> bytes with encode(), because sockets only send bytes.
    client_sock.send(message.encode("utf-8"))
    print("Sent:", message)

    # Step 4 - HANG UP
    client_sock.close()


if __name__ == "__main__":
    main()
