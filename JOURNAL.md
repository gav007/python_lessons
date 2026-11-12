# Gav's Python journal

Short dated notes: what I did, what clicked, what confused me. Newest at the top.

---

## 11-12 Nov 2026 - Lesson 7, keeping the call open
- **Did:** `second_server.py` / `second_client.py` - a chat: type lines, each one echoes back, `bye` hangs up.
  Server prints who called and what they said.
- **Clicked:** two loops. Outer = wait for the next caller. Inner = this one conversation.
  `recv()` giving empty bytes (`b""`) = the client hung up -> `break` out of the inner loop only.
- **Tripped me up:** pasted server code into the client file (two servers fighting over port 6000 =
  "only one usage of each socket address"). Tip: `bind`/`listen` = server, `connect` = client.
  And Ctrl+C can't stop a waiting server on Windows - close the window instead.
- **Next:** the Ctrl+C trick in `reference/05_ctrl_c_server.py` (settimeout + try/except), then write it myself.

---

## 10 Nov 2026 - Lesson 7, TCP sockets
- **Did:** went over the server/client shape on paper. Added commented reference code in
  `03_networking/lesson07_tcp_sockets/`.
- **Clicked:** the phone-call picture. The server has two sockets: the listening one, and a new one per caller from `accept()`.
- **Confusing at first:** which socket to talk on (`conn`, not the listening one), and bytes vs str (`encode` / `decode`).
- **Curious about for later:** SIP/RTP (VoIP = SIP sets up the call, RTP carries the voice, both just sockets underneath),
  making my own protocol (e.g. a "still OK?" check-in for an elderly-care device), UDP, threads.
- **Next:** practise writing the server and client from memory on the VM. Add Lesson 6 (addressing) code.
