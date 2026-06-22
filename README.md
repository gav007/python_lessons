# python_lessons

General purpose repo for recording Python sessions.

## Summary of repository contents

This README has been updated to reflect the files and folders currently in this repository (as of 2026-06-22).

Root files
- .gitignore — ignored files/dirs for the project
- README.md — (this file)

Top-level directories
- AI/ — small AI-related examples and prompt playground
  - AI/fake_ai.py — toy example for an AI-like interface
  - AI/ollama_ai.py — placeholder (empty)
  - AI/01_prompt_playground/ — prompt-playground folder

- dictionaries/ — short example scripts demonstrating Python dictionaries
  - 01_basic_lookup.py
  - 02_update_values.py
  - 03_count_items.py
  - 04_group_totals.py
  - 05_weak_topics.py
  - 06_nested_dictionaries.py
  - 07_inventory_tracker.py
  - 08_inventory_with_functions.py

- files/ — example data files and utility scripts
  - expenses.py — script for processing expenses (example)
  - expenses.txt — example input data for expenses.py
  - expenses_output.txt — sample output from expenses.py
  - invoice_cleaner.py — data-cleaning helper for invoices
  - invoices.txt — example invoice lines
  - service_log.txt — (empty log placeholder)
  - suspicious_logins.txt — (empty log placeholder)
  - NOTE: there is a malformed filename in this folder whose name appears to include invoice lines; consider removing or renaming that file (it looks like content was used as the filename by mistake).

- functions/ — small example functions and helper scripts
  - .gitkeep
  - coffee_tier.py — example function(s) related to coffee pricing/tiers
  - signal_log.txt — sample log of signals
  - signal_scanner.py — example script to scan signal logs
  - study_minutes.py — small helper to track study time / minutes


## How to use the scripts

General notes
- These examples are plain Python scripts; they should run with Python 3.8+.
- No requirements.txt is present; if you add third-party dependencies later, add a requirements.txt at project root.

Run a script
- From the repository root run:

    python files/expenses.py

- Or run any other script similarly, for example:

    python files/invoice_cleaner.py
    python functions/coffee_tier.py

Check file contents before running if unsure. Some files (service_log.txt, suspicious_logins.txt, AI/ollama_ai.py) are currently empty placeholders.

## Recommended next steps

- Clean up filenames in files/ (rename or remove the file whose name contains invoice lines). Having proper filenames makes the repo easier to use.
- Add a brief README in each subdirectory (e.g., dictionaries/README.md) describing the purpose and how to run the examples in that folder.
- If you want runnable examples, add a small README or top-level examples/ folder with clear input → output examples.
- Consider adding a requirements.txt if any examples depend on external packages.
- Add a LICENSE file to make the project license explicit.


## Contact

Repository owner: @gav007

