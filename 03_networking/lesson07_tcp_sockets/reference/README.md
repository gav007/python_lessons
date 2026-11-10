# Lesson 7 - TCP Sockets

## The picture
- **Server** = a shop phone: make it, give it a number, plug it in, wait, pick up.
- **Client** = you ringing the shop: make a phone, dial, talk, hang up.
- When the server picks up (`accept()`), it gets a **new socket just for that caller**.
  The listening socket stays free for the next one. Two sockets on the server, one on the client.

## Server - 6 steps
| # | Code | Why |
|---|------|-----|
| 1 | `s = socket.socket(AF_INET, SOCK_STREAM)` | IPv4 + TCP |
| 2 | `s.bind(("", 6000))` | give it a number; an address is an `(ip, port)` tuple |
| 3 | `s.listen(1)` | ready for calls; 1 = queue size (backlog) |
| 4 | `conn, addr = s.accept()` | blocks until a client rings; returns a NEW socket |
| 5 | `data = conn.recv(1024)` / `conn.send(data)` | talk on `conn`, not `s` |
| 6 | `conn.close()` | hang up this call |

## Client - 4 steps
`socket()` -> `connect((ip, port))` -> `send(text.encode())` / `recv(1024).decode()` -> `close()`

## Things that catch people out
- Sockets carry **bytes**: `encode()` before send, `decode()` after recv.
- The client never calls `bind()`. The OS gives it a random port.
- "Connection refused" = the server isn't running, or the port is wrong.
- "Address already in use" = an old server is still holding the port. `SO_REUSEADDR` fixes quick restarts.

## Files
1. `01_tcp_server.py` + `02_tcp_client.py` - the client sends one message
2. `03_echo_server.py` + `04_echo_client.py` - the server sends it back

Try it: two terminals, server first. In a third terminal, `ss -tn` or `netstat -ant` shows LISTEN, then ESTABLISHED.

## Lab questions
1. Listening socket: `server_sock`
2. Connection socket: `conn_sock`
3. Client socket: `client_sock`
4. Client port: random, picked by the OS
5. Server port: 6000 (6060 for the echo)
6. Data is sent as bytes
