# Admin Automation Toolkit

A small Python learning project built in WSL/Neovim.

This project reads messy invoice data from a text file, cleans valid records, skips bad records, calculates invoice summaries, and writes the results to a report file.

## Current Version

Version 1: Invoice Cleaner Summary Report

## What the Program Does

The program reads invoice records from:

Each valid invoice line should have four comma-separated fields:

invoice_id,company,amount,status

Example:

INV001,Acme Supplies,145.50,PAID

The program checks each line and builds a clean invoice dictionary for valid records.

Example cleaned invoice:

{
    "id": "INV001",
    "company": "Acme Supplies",
    "amount": 145.50,
    "status": "PAID"
}

Valid invoice dictionaries are stored together in a list.

Current Features
Reads invoice data from a local text file
Splits each line into invoice fields
Checks for badly formatted lines
Converts invoice amounts from text into numbers
Handles invalid amount values using try / except
Stores clean invoices as dictionaries
Counts invoices by status
Totals invoice amounts by status
Writes a summary report to a text file
Supported Invoice Statuses

The current supported statuses are:

PAID
UNPAID
QUERY
Output File

The summary report is written to:

reports/summary.txt

The report currently includes:

Invoice count by status
Total invoice amount by status
Example Output
--- SUMMARY ---
PAID 10
UNPAID 6
QUERY 4
--------------------
PAID 922.57
UNPAID 1211.49
QUERY 407.99
Known Limitations

This is still a learning version.

Current limitations:

Only supports comma-separated text files
Company names cannot contain commas
Status values must exactly match PAID, UNPAID, or QUERY
Amount values must be valid numbers
The report file is overwritten each time the program runs
Bad records are printed to the terminal but not yet saved to a separate error report
The report formatting is basic
Skills Practised

This project practises:

File input
File output
Loops
String methods
Lists
Dictionaries
Conditional logic
Functions
Return values
Exception handling
Basic data cleaning
Simple report generation
Next Possible Improvements

Possible future improvements:

Save bad records to a separate file
Improve report formatting
Strip extra whitespace from fields
Support lowercase status values
Add totals for all invoices combined
Add command-line arguments
Add CSV support
Add tests
Split the project into multiple files later
Project Status

Working Version 1 complete.

The project can currently read messy invoice data, clean valid records, calculate summaries, and write a basic report file.


One note before you run it: if your output has amounts first and counts second, that just means the order inside `write_summary()` is reversed or your parameter names are still confusing you. Not fatal. Just another little naming goblin.
