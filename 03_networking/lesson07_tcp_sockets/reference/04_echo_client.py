#!/usr/bin/env python3
"""
Lesson 7 - Exercise 3: ECHO CLIENT
==================================
Sends what you type, then prints what the server sends back.
Start 03_echo_server.py first, then:   python3 04_echo_client.py
"""
import socket


def main():
    text = input("Message to echo: ")

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 1) make a phone
    client_sock.connect(("127.0.0.1", 6060))                          # 2) dial
    client_sock.send(text.encode("utf-8"))                            # 3) talk (str -> bytes)

    reply = client_sock.recv(1024)                # 4) listen for the echo (blocks until it arrives)
    print("Server echoed:", reply.decode("utf-8"))   #    bytes -> str

    client_sock.close()                           # 5) hang up


if __name__ == "__main__":
    main()
