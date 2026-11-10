# Roadmap - where this is going

Goal: become someone who can **automate and troubleshoot networks with Python** -
the skill set of a network automation / NetDevOps engineer, with security and IoT on the side.

Rhythm: little and often. A few short sessions a week beats one long one.
Each stage ends with a **portfolio project** that goes in `04_projects/`.

---

## Stage 1 - Foundations, properly (now)
Know what every line does: types, what a function takes in and gives back, files, errors.
- Built-ins: `str`, `list`, `dict`, `set`, `open()`, `try/except`
- Standard library: `json`, `csv`, `re`, `datetime`, `pathlib`
- **Project:** log or invoice cleaner that reads a file and writes a clean report

## Stage 2 - Linux and automation tools
Make Python drive the computer.
- `subprocess` (run `ping`, `ip`, `ss`), `argparse` (real command-line tools), `logging`, `shutil`
- Linux: `ip`, `ss`, `netstat`, `grep`, `cron`, `systemctl`
- **Project:** an admin CLI tool, e.g. `netcheck --host 8.8.8.8 --report`

## Stage 3 - Network programming (college Lessons 6-7+)
How programs talk over a network.
- `socket` (TCP, then UDP), `ipaddress` (subnets done right), `threading` (many clients)
- HTTP with `requests`; small web apps with `flask`
- Concepts: client/server, ports, bytes vs text, protocols (HTTP, DNS, SIP/RTP)
- **Project:** a port checker / multi-client chat / tiny "still OK?" check-in protocol

## Stage 4 - Talking to real network devices
The bread and butter of network automation (fits CML labs).
- `paramiko` - SSH from Python
- `netmiko` - SSH to Cisco and others, send `show` commands, push config
- `textfsm` / `ttp` - turn `show` output into data
- `napalm` - one interface for many vendors (get facts, compare configs)
- `pysnmp` / `easysnmp` - SNMP polling (links to Network Management / FCAPS)
- `jinja2` - config templates
- **Project:** config backup + "what changed?" tool for a CML lab

## Stage 5 - Modern automation
How it's done at scale.
- APIs: RESTCONF / NETCONF (`requests`, `ncclient`), JSON / YAML (`pyyaml`)
- `nornir` (Python automation framework), Ansible (YAML playbooks, good to know alongside)
- `pytest` (tests), Git branches, GitHub Actions (tests run on every push)
- `pydantic` (check data is valid), `rich` / `typer` (nice CLIs)
- **Project:** a small "network as code" repo: inventory in YAML, templates, tests, push to a lab

## Stage 6 - Security, IoT and AI (side branches)
- Security: `scapy` (build and sniff packets), `python-nmap`, reading pcaps with `pyshark`
- IoT: `paho-mqtt`, `pyserial` (Arduino / ESP32), sensor data to a dashboard
- Speed: `asyncio` (many devices at once)
- AI: calling a local or cloud model from a tool (like Pip)
- Packaging: virtual environments, `requirements.txt`, Docker basics
- **Project:** pick one that makes a good demo, e.g. ESP32 sensor -> MQTT -> Pi dashboard

---

## Parked
- Classes / OOP (syllabus Module 11) - come back when a project needs it (Stage 4 libraries use them a lot)

## Certs it lines up with
CCNA (automation section) -> Cisco DevNet Associate / CCNA Automation -> Python Institute PCEP/PCAP
