#!/usr/bin/env python3
"""
Lesson 7 - Exercise 3: ECHO SERVER (sends back whatever it gets)
================================================================
Same steps as 01_tcp_server.py, plus ONE new line: send the data back.
Run me first:   python3 03_echo_server.py     (Ctrl+C to stop)
"""
import socket


def main():
    # 1) make the phone   2) give it a number   3) plug it in
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(("", 6060))     # "" = answer on any network card, so another VM can reach it too
    server_sock.listen(1)
    print("Echo server on port 6060 ...")

    while True:                                  # run forever, one client at a time
        conn_sock, addr = server_sock.accept()   # 4) pick up -> new socket for this caller
        data = conn_sock.recv(1024)              # 5) receive (bytes)
        print(addr, "said:", data.decode("utf-8"))
        conn_sock.send(data)                     # 6) ECHO: send the same bytes straight back (no decode needed)
        conn_sock.close()                        # 7) done with this client
    # never reached: the loop runs until Ctrl+C


if __name__ == "__main__":
    main()
