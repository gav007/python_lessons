#!/usr/bin/env python3
"""
Lesson 7 - Exercise 5: a chat server that STOPS on Ctrl+C (even on Windows)
==========================================================================
The problem: on Windows, while Python waits inside accept(), Ctrl+C can't get through.
              The server looks "locked" until a new client calls.

The 3-line trick:
    1. server_sock.settimeout(1)          -> accept() gives up after 1 second instead of waiting forever
    2. try: ... accept() ...               -> try to pick up
    3. except socket.timeout: continue     -> nobody called? loop round and wait again

So every second Python comes up for air, and that's when Ctrl+C gets through.
Same server as your chat server otherwise.

Run me:    python 05_ctrl_c_server.py      then press Ctrl+C - it stops within a second.
Client:    your second_client.py works with it (port 6000).
"""
import socket


def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(("", 6000))
    server_sock.listen(1)

    server_sock.settimeout(1)                          # TRICK 1: wait at most 1 second for a caller

    print("Chat server on port 6000 - Ctrl+C to stop")
    try:
        while True:                                    # OUTER loop: wait for the next caller
            try:
                conn, addr = server_sock.accept()      # TRICK 2: try to pick up...
            except socket.timeout:
                continue                               # TRICK 3: ...nobody rang, go round again

            conn.settimeout(None)                      # this caller's line waits normally again
            print("Call from", addr)

            while True:                                # INNER loop: this one conversation
                data = conn.recv(1024)
                if not data:                           # empty bytes = the client hung up
                    break
                print("Client said ==>", data.decode())
                conn.send(data)                        # echo it back

            conn.close()
            print("Caller hung up. Waiting for the next one...")

    except KeyboardInterrupt:                          # this is what Ctrl+C raises
        print("\nCtrl+C - closing the server. Bye!")
    finally:
        server_sock.close()                            # always hand port 6000 back


if __name__ == "__main__":
    main()
