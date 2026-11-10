# Gav's Python journal

Short dated notes: what I did, what clicked, what confused me. Newest at the top.

---

## 10 Nov 2026 - Lesson 7, TCP sockets
- **Did:** went over the server/client shape on paper. Added commented reference code in
  `03_networking/lesson07_tcp_sockets/`.
- **Clicked:** the phone-call picture. The server has two sockets: the listening one, and a new one per caller from `accept()`.
- **Confusing at first:** which socket to talk on (`conn`, not the listening one), and bytes vs str (`encode` / `decode`).
- **Curious about for later:** SIP/RTP (VoIP = SIP sets up the call, RTP carries the voice, both just sockets underneath),
  making my own protocol (e.g. a "still OK?" check-in for an elderly-care device), UDP, threads.
- **Next:** practise writing the server and client from memory on the VM. Add Lesson 6 (addressing) code.
