# python_lessons

My learning codebase for **practical Python for networking, Linux and automation**.
I'm a Networking Technologies student at TU Dublin (Year 3). This repo is my reference,
my practice log, and my portfolio: every folder is something I've written and understood.

> How I work: write it myself first, then compare with a commented `reference/` version,
> then build a small real tool with it. Notes go in [JOURNAL.md](JOURNAL.md).

## The path

| Level | Folder | What's in it | Status |
|---|---|---|---|
| 1 | [01_foundations](01_foundations/) | data types, dictionaries, functions, files, maths | mostly done |
| 2 | [02_linux_automation](02_linux_automation/) | regex, logs, `pathlib`, `subprocess`, `argparse` | next |
| 3 | [03_networking](03_networking/) | college labs, addressing, TCP sockets, HTTP | in progress |
| 4 | [04_projects](04_projects/) | real tools: subnet tool, recon tool, Flask apps, AI | growing |
| - | [later](later/) | parked topics (classes / OOP) | parked |

- Long-term plan: [ROADMAP.md](ROADMAP.md)
- Full course plan, module by module: [docs/SYLLABUS.md](docs/SYLLABUS.md)
- Saving my work to GitHub: [GIT-CHEATSHEET.md](GIT-CHEATSHEET.md)

## Highlights
- **TCP client/server + echo** - [03_networking/lesson07_tcp_sockets](03_networking/lesson07_tcp_sockets/)
- **Subnet tool** - [04_projects/subnet_tool](04_projects/subnet_tool/)
- **System recon tool** - [04_projects/system_recon_tool](04_projects/system_recon_tool/)
- **Weather app (Flask + API)** - [04_projects/weather_flask](04_projects/weather_flask/)

## Folder rules
- Each lesson folder: my code at the top, `reference/` for the commented model answer, a short README.
- No secrets in the repo: API keys live in `.env` (ignored by Git).
- Numbered files (`01_`, `02_`) run in order.
