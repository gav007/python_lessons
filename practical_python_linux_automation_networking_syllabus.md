# Practical Python, Linux, Automation and Networking Syllabus

**Track:** Beginner-to-capstone practical programming for a TU Dublin Networking Technologies student  
**Mode:** Slow, lab-driven, one concept at a time  
**Final goal:** Build independent Python tools for Linux, automation, admin data handling, logging, web basics, and networking support

---

## 0. Course Identity

This syllabus is not a generic Python course. It is designed for a student who already has some Python exposure but wants stronger foundations, deeper understanding, and practical projects that connect to networking, Linux, automation, and real administrative data handling.

The main identity of this course is:

> **Practical Python for Linux, automation, networking, and admin tools.**

The aim is not to memorise syntax for its own sake. The aim is to understand what Python code is doing, what each function or method takes in, what it gives back, what type each value is, and how small ideas combine into useful tools.

This course deliberately avoids throwaway beginner projects such as guessing games, pizza apps, fake banking apps, and random animal classes. Those can be useful for absolute beginners, but they are not the centre of this track. The project style here is closer to:

- file inspectors
- CSV and invoice cleaners
- expense/report generators
- Linux folder audit tools
- log parsers
- backup helpers
- subprocess-based admin tools
- network checkers
- simple web and socket tools
- final hybrid system/network/admin toolkit

---

## 1. How This Course Should Be Used

Each topic should be studied in this order:

1. Read the concept explainer.
2. Study the syntax and parameter breakdown.
3. Type the tiny example manually.
4. Run it.
5. Break it on purpose.
6. Fix it.
7. Complete the guided lab.
8. Complete one or two variations.
9. Submit your code for review.
10. Only then move on.

The important rule is:

> **Do not move quickly just because the example makes sense when reading it. You only know it when you can write a small version yourself.**

Reading code and writing code are different skills. Reading gives recognition. Writing gives ownership.

---

## 2. Standard Lesson Format

Every topic block in this syllabus follows the same rhythm.

### Concept Explainer

A plain-English explanation of what the concept is, why it matters, and where it appears in real work.

### Syntax and Parameter Breakdown

A detailed breakdown of the functions, methods, commands, arguments, parameters, return values, and common mistakes.

This section must always answer:

- What is being called?
- Is it a function, method, class, command, or module?
- What does it take in?
- What type is each input?
- What does it return?
- What type is the return value?
- Does it change something in place?
- Does it print only, return only, or both?
- What errors are common?

### Tiny Example

A small typed example. No cleverness. No shortcuts. One idea only.

### Guided Practice / Lab Sheet

A hands-on task with steps. This is where the concept becomes real.

### Variation Drills

Small changes to prove the concept is understood, not just copied.

### Build-Up Exercise

After three or four connected ideas, combine them into a slightly bigger guided exercise.

### Capstone

An independent project for that cluster. It should require planning, coding, testing, and a short README.

### Review Checklist

A short checklist to confirm what stuck.

---

## 3. AI Assistance Rules

AI is allowed, but it should not replace the learning.

Use this rule:

1. You write first.
2. AI gives hints if you freeze.
3. AI reviews your attempt.
4. AI explains errors.
5. AI may show a corrected version after your version exists.
6. AI may generate variations after your version works.

Avoid this pattern:

> “Write the whole project for me and explain it after.”

That creates a nice-looking repository and a weak brain. Very modern, very useless.

For every AI-reviewed task, record:

- what you attempted
- what broke
- what the fix was
- what you learned
- one variation to try next

---

## 4. Assumed Working Environment

The course assumes this setup:

- Windows laptop
- WSL Ubuntu for Linux work
- Python 3
- terminal-based workflow
- Git and GitHub
- VS Code or Neovim
- folders organised by module
- small README files for projects

Recommended repository name:

```text
python-practical-toolkit
```

Suggested structure:

```text
python-practical-toolkit/
├── 00_setup_and_notes/
├── 01_foundation_repair/
├── 02_functions_and_modules/
├── 03_data_structures/
├── 04_file_io_exceptions/
├── 05_csv_json_reports/
├── 06_linux_fundamentals/
├── 07_filesystem_automation/
├── 08_logging_and_log_parsing/
├── 09_subprocess_tools/
├── 10_cli_tools/
├── 11_oop_project_structure/
├── 12_testing_git_readmes/
├── 13_web_basics/
├── 14_sockets_networking/
├── 15_network_support_tools/
└── 16_final_capstone/
```

Each project folder should contain:

```text
project_name/
├── README.md
├── data/
├── output/
├── src/
└── tests/          # added later when testing begins
```

---

## 5. Course Timeline

This is designed as a **16-week core syllabus** with optional deeper work after each module.

The pace is deliberately steady. The goal is not to “cover” material. The goal is to become capable.

| Week | Module | Main Theme | Cluster Project |
|---|---|---|---|
| 1 | Module 1 | Foundation repair | Input validator mini-tools |
| 2 | Module 2 | Functions and modules | Expense calculator functions |
| 3 | Module 3 | Strings, lists, dictionaries, sets | Invoice record organiser |
| 4 | Module 4 | File I/O and exceptions | Expense and invoice cleaner |
| 5 | Module 5 | CSV, JSON, reports | Monthly admin report generator |
| 6 | Module 6 | Linux fundamentals | Linux command workbook |
| 7 | Module 7 | Filesystem automation | Linux File Doctor |
| 8 | Module 8 | Logging and log parsing | Log Watcher |
| 9 | Module 9 | Subprocess and OS interaction | Command runner report tool |
| 10 | Module 10 | CLI tools | Admin Automation CLI |
| 11 | Module 11 | OOP and project structure | Service desk record system |
| 12 | Module 12 | Testing, debugging, Git, README | Polished repo checkpoint |
| 13 | Module 13 | Web basics and HTTP | Mini HTML status dashboard |
| 14 | Module 14 | Sockets | TCP echo and diagnostic tools |
| 15 | Module 15 | Network support tooling | Network Check Reporter |
| 16 | Module 16 | Final capstone | Hybrid System, Network & Admin Toolkit |

---

# Module 1: Python Foundation Repair

## Purpose

This module reviews the basics, but not like an absolute beginner course. The goal is to repair weak spots: types, input conversion, conditions, loops, tracing, and simple validation.

The focus is not “what is a variable?” The focus is:

- What type is this value?
- Where did it come from?
- What happens if the input is wrong?
- What does the loop do each time?
- What value changes inside the loop?
- What condition stops it?

---

## Concept Explainer

A Python program is a sequence of instructions. Most beginner confusion comes from not tracking values clearly. A variable is a name pointing to a value. That value has a type: string, integer, float, Boolean, list, dictionary, and so on.

In real automation scripts, type confusion is everywhere. User input arrives as text. File content arrives as text. CSV fields arrive as text. Command output arrives as text. If you need calculations, comparisons, totals, filtering, or validation, you must convert and check values carefully.

This is why foundation repair matters. Every later project depends on being able to say:

> “This value is a string right now. I need a float. This conversion can fail. I should handle that.”

---

## Syntax and Parameter Breakdown

### `input(prompt)`

`input()` is a built-in function.

It takes in:

| Part | Type | Example | Meaning |
|---|---|---|---|
| `prompt` | `str` | `"Enter amount: "` | Message shown to the user |

It returns:

| Return Type | Example | Important Note |
|---|---|---|
| `str` | `"123.45"` | Always returns a string, even if the user types a number |

Example:

```python
amount_text = input("Enter amount: ")
print(type(amount_text))
```

If the user enters `50`, the type is still `str`.

### `int(value)` and `float(value)`

These are built-in conversion functions.

They take in:

| Function | Input Type | Example | Returns |
|---|---|---|---|
| `int()` | string or number | `int("42")` | `int` |
| `float()` | string or number | `float("19.99")` | `float` |

Common errors:

```python
int("hello")      # ValueError
float("12 euro") # ValueError
```

### `if`, `elif`, `else`

These control which block of code runs.

Syntax:

```python
if condition:
    # runs if condition is True
elif another_condition:
    # runs if first condition is False and this one is True
else:
    # runs if no previous condition is True
```

A condition must evaluate to `True` or `False`.

### `for` loop

Used when you have a known collection or range.

```python
for item in collection:
    print(item)
```

### `while` loop

Used when repetition depends on a condition.

```python
while condition:
    # repeat while condition is True
```

Common danger: forgetting to update the condition inside the loop, creating an infinite loop.

---

## Tiny Example

```python
amount_text = input("Enter invoice amount: ")
amount = float(amount_text)

if amount > 100:
    print("Large invoice")
else:
    print("Normal invoice")
```

Trace it:

1. User enters text.
2. `input()` returns a string.
3. `float()` converts it to a number.
4. `if amount > 100` checks a Boolean condition.
5. One branch runs.

---

## Guided Practice / Lab Sheet

Create `invoice_amount_checker.py`.

Task:

Ask the user for an invoice amount. Convert it to a float. Print one of these messages:

- under 0: `Invalid amount`
- 0 to 99.99: `Small invoice`
- 100 to 499.99: `Medium invoice`
- 500 or more: `Large invoice`

Steps:

1. Create a variable called `amount_text`.
2. Use `input()` to get the value.
3. Convert it to float and store it in `amount`.
4. Use `if / elif / else`.
5. Test with `-5`, `20`, `150`, `800`.

---

## Variation Drills

1. Add a message if the user enters exactly `0`.
2. Add a variable called `supplier_name` and include it in the output.
3. Add a running total for three invoice amounts using a loop.
4. Print the type of each value before and after conversion.

---

## Build-Up Exercise

Create `three_invoice_summary.py`.

The program should:

1. Ask for three invoice amounts.
2. Convert each to float.
3. Keep a running total.
4. Count how many are large invoices.
5. Print the total and count.

---

## Module Capstone: Input Validator Mini-Tools

Build a small folder of validation scripts:

```text
01_foundation_repair/
├── invoice_amount_checker.py
├── three_invoice_summary.py
├── login_attempt_counter.py
└── menu_loop.py
```

The capstone script should be `menu_loop.py`.

It should:

- show a simple menu
- ask the user to choose an option
- validate the choice
- keep looping until the user chooses quit
- use at least one `while` loop
- use at least one `if / elif / else` chain

---

## Review Checklist

You are ready to move on when you can explain:

- why `input()` returns a string
- when to use `int()` versus `float()`
- what a Boolean condition is
- the difference between `for` and `while`
- what variable changes inside a loop
- why bad input can crash a script

---

# Module 2: Functions, Parameters, Returns, and Modules

## Purpose

This module focuses on the part that often causes freezing: functions. You need to understand what goes in, what comes back, and why `print()` is not the same as `return`.

---

## Concept Explainer

A function is a named block of code that performs a task. It helps you avoid repeating yourself and lets you test one piece of logic at a time.

A parameter is a variable listed in the function definition. An argument is the actual value you pass when calling the function.

A return value is the result the function sends back to the caller.

This matters because real projects become impossible if everything is written in one long script. File reading, validation, parsing, reporting, and saving should each become separate functions.

---

## Syntax and Parameter Breakdown

### Basic function

```python
def function_name(parameter1, parameter2):
    result = parameter1 + parameter2
    return result
```

| Part | Meaning |
|---|---|
| `def` | Starts a function definition |
| `function_name` | Name used to call the function |
| `parameter1` | Input variable inside the function |
| `return` | Sends a value back |

### Example

```python
def add_numbers(a, b):
    total = a + b
    return total

answer = add_numbers(5, 7)
print(answer)
```

Function call breakdown:

| Item | Type | Meaning |
|---|---|---|
| `5` | `int` | First argument, goes into `a` |
| `7` | `int` | Second argument, goes into `b` |
| `answer` | `int` | Receives returned value |

### `print()` versus `return`

`print()` displays something on the screen.  
`return` gives a value back to the code that called the function.

Bad pattern:

```python
def calculate_total(a, b):
    print(a + b)
```

This prints a value but returns `None`.

Better pattern:

```python
def calculate_total(a, b):
    return a + b
```

Now the result can be reused, tested, written to a file, or included in a report.

### Default parameters

```python
def format_currency(amount, symbol="€"):
    return f"{symbol}{amount:.2f}"
```

| Parameter | Default | Meaning |
|---|---|---|
| `amount` | none | Must be supplied |
| `symbol` | `"€"` | Optional; uses euro symbol unless another is given |

---

## Tiny Example

```python
def calculate_vat(amount, rate=0.23):
    vat = amount * rate
    return vat

invoice_amount = 100.00
vat_amount = calculate_vat(invoice_amount)
print(vat_amount)
```

Trace it:

1. `invoice_amount` is a float.
2. Function is called with one argument.
3. `rate` uses default value `0.23`.
4. Function returns a float.
5. Returned value is stored in `vat_amount`.

---

## Guided Practice / Lab Sheet

Create `expense_functions.py`.

Write these functions:

```python
def calculate_total(amounts):
    pass

def calculate_average(amounts):
    pass

def format_euro(amount):
    pass
```

Requirements:

- `calculate_total()` takes a list of floats and returns a float.
- `calculate_average()` takes a list of floats and returns a float.
- `format_euro()` takes a float and returns a string like `€12.50`.

Test data:

```python
expenses = [12.50, 30.00, 7.25]
```

---

## Variation Drills

1. Add a function called `count_large_expenses(amounts, limit)`.
2. Add a default limit of `100.00`.
3. Add a function called `find_highest_expense(amounts)`.
4. Make one function return two values: total and average.

---

## Build-Up Exercise

Create `expense_report.py`.

It should:

1. Store expenses in a list.
2. Use functions to calculate total, average, highest, and large-count.
3. Print a neat report.
4. Avoid doing calculations directly in the main part of the program.

---

## Module Capstone: Expense Calculator Functions

Build a small function-based expense tool.

Required files:

```text
02_functions_and_modules/
├── expense_math.py
└── main.py
```

`expense_math.py` should contain reusable functions.

`main.py` should import and use them.

Required functions:

- `calculate_total(amounts)`
- `calculate_average(amounts)`
- `count_over_limit(amounts, limit=100.0)`
- `format_currency(amount, symbol="€")`
- `summarise_expenses(amounts)` returning a dictionary

---

## Review Checklist

You are ready to move on when you can explain:

- parameter versus argument
- `print()` versus `return`
- what `None` means
- how default parameters work
- why functions make testing easier
- how to import your own module

---

# Module 3: Strings, Lists, Dictionaries, Sets, and Real Records

## Purpose

This module turns basic data structures into real-world record handling. Instead of abstract examples, you will work with invoice lines, usernames, IP addresses, supplier names, and status values.

---

## Concept Explainer

A string is text. A list is an ordered collection. A dictionary stores key-value pairs. A set stores unique values.

These structures matter because real scripts need to organise data. A CSV row might become a dictionary. A list might store all invoices. A set might remove duplicate IP addresses. A string method might clean messy input.

The key learning point is choosing the correct structure:

- Use a string for one piece of text.
- Use a list when order matters or you need many items.
- Use a dictionary when you want to look something up by name or ID.
- Use a set when uniqueness matters.

---

## Syntax and Parameter Breakdown

### String methods

```python
clean_name = supplier_name.strip().title()
```

| Method | Belongs To | Takes In | Returns | Meaning |
|---|---|---|---|---|
| `.strip()` | string | optional chars | string | removes whitespace at ends |
| `.lower()` | string | nothing | string | lowercases text |
| `.upper()` | string | nothing | string | uppercases text |
| `.split(sep)` | string | separator string | list | splits text into parts |
| `.replace(old, new)` | string | two strings | string | replaces text |

### List methods

```python
invoices.append("INV001")
```

| Method | Belongs To | Takes In | Returns | Changes List? |
|---|---|---|---|---|
| `.append(item)` | list | any item | `None` | yes |
| `.remove(item)` | list | existing item | `None` | yes |
| `.sort()` | list | optional args | `None` | yes |
| `.pop(index)` | list | optional int | removed item | yes |

Important: many list methods return `None` because they change the list in place.

### Dictionary access

```python
invoice = {
    "id": "INV001",
    "supplier": "Acme Supplies",
    "amount": 145.50,
    "status": "PAID"
}

print(invoice["supplier"])
```

| Operation | Meaning |
|---|---|
| `invoice["supplier"]` | get value by key; crashes if missing |
| `invoice.get("supplier")` | get value safely; returns `None` if missing |
| `invoice["status"] = "PAID"` | add or update key |
| `"status" in invoice` | check if key exists |

### Set basics

```python
unique_ips = set(ip_list)
```

| Operation | Meaning |
|---|---|
| `set(list_value)` | converts list to set, removing duplicates |
| `.add(item)` | adds one item |
| `.update(items)` | adds many items |
| `item in my_set` | membership test |

---

## Tiny Example

```python
raw_line = " INV001, acme supplies , 145.50 , paid "
parts = raw_line.split(",")

invoice = {
    "id": parts[0].strip(),
    "supplier": parts[1].strip().title(),
    "amount": float(parts[2].strip()),
    "status": parts[3].strip().upper()
}

print(invoice)
```

This takes one messy line of text and turns it into a structured dictionary.

---

## Guided Practice / Lab Sheet

Create `invoice_record_parser.py`.

Given:

```python
raw_lines = [
    "INV001,Acme Supplies,145.50,PAID",
    "INV002,OfficeMart,82.10,UNPAID",
    "INV003,TechFix Ltd,75.25,PAID"
]
```

Build a list of dictionaries:

```python
[
    {"id": "INV001", "supplier": "Acme Supplies", "amount": 145.50, "status": "PAID"},
    ...
]
```

Steps:

1. Create an empty list called `invoices`.
2. Loop through each raw line.
3. Split the line by comma.
4. Clean each part.
5. Convert amount to float.
6. Create a dictionary.
7. Append it to the list.
8. Print each dictionary.

---

## Variation Drills

1. Count how many invoices are `PAID`.
2. Create a set of unique supplier names.
3. Create a dictionary where invoice ID is the key.
4. Print only invoices over `100.00`.
5. Detect duplicate invoice IDs using a set.

---

## Build-Up Exercise

Create `invoice_organiser.py`.

It should:

- read hard-coded raw invoice lines
- convert them into dictionaries
- store them in a list
- create separate lists for `PAID`, `UNPAID`, and `QUERY`
- print totals for each status

---

## Module Capstone: Invoice Record Organiser

Build a script that takes messy invoice records and organises them.

Required features:

- clean whitespace
- normalise status to uppercase
- convert amounts to floats
- store invoices as dictionaries
- group by status
- collect unique suppliers
- detect duplicate invoice IDs
- print a clean summary

Suggested output:

```text
Invoice Summary
---------------
Total invoices: 12
Paid: 7
Unpaid: 3
Query: 2
Unique suppliers: 8
Duplicate invoice IDs: INV004
Total paid amount: €920.50
```

---

## Review Checklist

You are ready to move on when you can explain:

- why strings need cleaning
- why `.split()` returns a list
- why `.append()` returns `None`
- when to use a list of dictionaries
- how a set removes duplicates
- when dictionary access can raise `KeyError`

---

# Module 4: File I/O and Exceptions

## Purpose

This module moves from hard-coded data to real files. This is a major step. Most useful automation scripts read files, process them, and write new output files.

---

## Concept Explainer

File I/O means file input/output. Input means reading data from a file. Output means writing data to a file.

The basic pattern is:

1. Open the file.
2. Process the file.
3. Close the file.

In modern Python, you usually use `with open(...) as file:` so Python closes the file automatically when the block ends.

Exceptions are errors that happen while a program runs. File scripts need exception handling because files may be missing, locked, badly formatted, or full of invalid data.

---

## Syntax and Parameter Breakdown

### `open(filename, mode, encoding="utf-8")`

`open()` is a built-in function.

| Parameter | Type | Example | Meaning |
|---|---|---|---|
| `filename` | `str` or path object | `"data/invoices.txt"` | file path |
| `mode` | `str` | `"r"`, `"w"`, `"a"` | read, write, append |
| `encoding` | `str` | `"utf-8"` | text encoding |

Returns:

| Return Type | Meaning |
|---|---|
| file object | object with methods like `.read()`, `.readline()`, `.write()` |

Common modes:

| Mode | Meaning | Danger |
|---|---|---|
| `"r"` | read | file must exist |
| `"w"` | write | overwrites existing file |
| `"a"` | append | adds to end |
| `"x"` | create new | fails if file exists |

### File object methods

| Method | Takes In | Returns | Meaning |
|---|---|---|---|
| `.read()` | nothing | string | whole file content |
| `.readline()` | nothing | string | next line |
| `.write(text)` | string | int | writes text, returns characters written |

### `try / except`

```python
try:
    amount = float(amount_text)
except ValueError:
    print("Invalid amount")
```

| Part | Meaning |
|---|---|
| `try` | code that might fail |
| `except ValueError` | runs if that specific error occurs |
| `else` | optional; runs if no error occurred |
| `finally` | optional; always runs |

---

## Tiny Example

```python
try:
    with open("data/invoices.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found")
```

Trace it:

1. Python tries to open the file.
2. If it exists, each line is read.
3. `.strip()` removes the newline.
4. If the file is missing, the exception block runs.

---

## Guided Practice / Lab Sheet

Create this file:

```text
data/invoices.txt
```

Content:

```text
INV001,Acme Supplies,145.50,PAID
INV002,OfficeMart,82.10,UNPAID
INV003,TechFix Ltd,not_a_number,PAID
INV004,PaperCo,44.20,QUERY
```

Create `read_invoices.py`.

Steps:

1. Open the file with `with open()`.
2. Loop through each line.
3. Strip the newline.
4. Split by comma.
5. Try to convert amount to float.
6. If conversion fails, put the line into a `bad_lines` list.
7. Print good invoices and bad lines.

---

## Variation Drills

1. Add line numbers to bad-line reports.
2. Write bad lines to `output/bad_lines.txt`.
3. Write clean invoices to `output/clean_invoices.txt`.
4. Count paid, unpaid, and query invoices.
5. Add exception handling for missing input file.

---

## Build-Up Exercise

Create `invoice_file_cleaner.py`.

It should:

- read `data/invoices.txt`
- parse each line
- skip empty lines
- validate number of fields
- validate amount
- group records by status
- write clean records to output files
- write rejected records to `bad_lines.txt`

---

## Module Capstone: Expense and Invoice Cleaner

Build a proper file-based cleaner.

Required files:

```text
04_file_io_exceptions/
├── data/
│   ├── invoices.txt
│   └── expenses.txt
├── output/
│   ├── clean_invoices.txt
│   ├── bad_lines.txt
│   └── summary.txt
└── src/
    └── cleaner.py
```

Required features:

- use `with open()`
- use `try / except`
- catch `FileNotFoundError`
- catch `ValueError`
- validate field counts
- write clean output
- write bad output
- print a final summary

---

## Review Checklist

You are ready to move on when you can explain:

- what a file object is
- why `with` is safer than manually closing
- what mode `"w"` does
- why file data arrives as strings
- why conversion can fail
- how to catch `FileNotFoundError`
- how to catch `ValueError`

---

# Module 5: CSV, JSON, Config Files, and Reports

## Purpose

This module upgrades plain text file handling into structured data handling. CSV and JSON are everywhere in business, networking, web APIs, exports, logs, and reports.

---

## Concept Explainer

CSV stands for comma-separated values. It is a simple table format. Each row is a record. Each column is a field.

JSON stands for JavaScript Object Notation. It is a structured text format used heavily in web APIs, configuration files, and data exchange.

In practical automation, you often read CSV, clean it, store records as dictionaries, and write a report as CSV, JSON, or plain text.

---

## Syntax and Parameter Breakdown

### `csv.DictReader(file_object)`

`DictReader` reads rows into dictionaries using the first row as headers.

```python
import csv

with open("data/invoices.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["invoice_id"])
```

| Part | Type | Meaning |
|---|---|---|
| `file` | file object | opened CSV file |
| `reader` | iterator | gives one row at a time |
| `row` | dictionary | keys come from CSV headers |

### `csv.DictWriter(file_object, fieldnames=...)`

Writes dictionaries to CSV.

```python
fieldnames = ["invoice_id", "supplier", "amount", "status"]
writer = csv.DictWriter(file, fieldnames=fieldnames)
writer.writeheader()
writer.writerow(invoice)
```

| Parameter | Type | Meaning |
|---|---|---|
| `file_object` | file object | output CSV file |
| `fieldnames` | list of strings | column names |

### `json.load(file_object)`

Reads JSON from a file and converts it to Python data.

| JSON | Python |
|---|---|
| object | dictionary |
| array | list |
| string | string |
| number | int or float |
| true/false | True/False |
| null | None |

### `json.dump(data, file_object, indent=4)`

Writes Python data as JSON.

---

## Tiny Example

```python
import csv

with open("data/invoices.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        amount = float(row["amount"])
        print(row["supplier"], amount)
```

---

## Guided Practice / Lab Sheet

Create `data/invoices.csv`:

```csv
invoice_id,supplier,amount,status
INV001,Acme Supplies,145.50,PAID
INV002,OfficeMart,82.10,UNPAID
INV003,TechFix Ltd,75.25,PAID
```

Create `csv_invoice_reader.py`.

Steps:

1. Import `csv`.
2. Open the CSV file.
3. Use `csv.DictReader`.
4. Loop through rows.
5. Convert amount to float.
6. Count paid invoices.
7. Print summary.

---

## Variation Drills

1. Write only unpaid invoices to a new CSV.
2. Write a JSON summary file.
3. Add a config file containing the unpaid limit.
4. Add error handling for missing columns.
5. Add a report timestamp using `datetime`.

---

## Build-Up Exercise

Create `monthly_report_generator.py`.

It should:

- read invoice CSV
- read expense CSV
- calculate totals
- group by status/category
- write `summary.txt`
- write `summary.json`
- write `unpaid_invoices.csv`

---

## Module Capstone: Monthly Admin Report Generator

Build a small reporting tool.

Input:

```text
data/invoices.csv
data/expenses.csv
data/config.json
```

Output:

```text
output/monthly_summary.txt
output/monthly_summary.json
output/unpaid_invoices.csv
output/bad_rows.csv
```

Required features:

- CSV input
- JSON config
- dictionary-based records
- validation
- exception handling
- clean reports
- README explaining inputs and outputs

---

## Review Checklist

You are ready to move on when you can explain:

- the difference between CSV and JSON
- why `DictReader` is useful
- why CSV values still arrive as strings
- what `fieldnames` means
- how JSON maps to Python types
- why config files are useful

---

# Module 6: Linux Fundamentals for Python Automation

## Purpose

This module builds the Linux mental model needed for automation. You do not need to become a Linux wizard overnight. You need enough command-line fluency to understand files, permissions, processes, pipes, logs, and scheduled tasks.

---

## Concept Explainer

Linux is built around files, processes, users, permissions, and text streams. A lot of admin work is about inspecting those things.

Python automation becomes much stronger when you understand what Linux already gives you:

- `ls` shows files
- `find` searches files
- `grep` searches text
- `cat`, `head`, `tail` inspect text
- `ps` shows processes
- `chmod` changes permissions
- `cron` schedules tasks
- `/var/log` stores many logs

The goal is not to replace Linux commands with Python. The goal is to understand both and know when to use each.

---

## Syntax and Parameter Breakdown

### `pwd`

Shows current directory.

```bash
pwd
```

No parameters required.

Returns text output in the terminal.

### `ls -lah`

Lists files.

```bash
ls -lah
```

| Part | Meaning |
|---|---|
| `ls` | list directory contents |
| `-l` | long format |
| `-a` | include hidden files |
| `-h` | human-readable sizes |

### `grep "ERROR" app.log`

Searches text.

| Part | Meaning |
|---|---|
| `grep` | search command |
| `"ERROR"` | pattern to search for |
| `app.log` | file to search |

### Pipes

```bash
cat app.log | grep "ERROR"
```

A pipe sends output from one command into another command.

---

## Tiny Example

```bash
mkdir linux_lab
cd linux_lab
echo "ERROR failed login" > app.log
echo "INFO service started" >> app.log
grep "ERROR" app.log
```

---

## Guided Practice / Lab Sheet

Create a folder called `linux_lab`.

Tasks:

1. Print current directory with `pwd`.
2. Create folders `data`, `logs`, and `output`.
3. Create a file called `logs/app.log`.
4. Add five lines to it using `echo`.
5. Use `cat` to display it.
6. Use `grep` to find `ERROR`.
7. Use `wc -l` to count lines.
8. Use `ls -lah` to inspect sizes and permissions.

---

## Variation Drills

1. Use `find` to locate all `.log` files.
2. Use `tail` to view the last two lines.
3. Use `chmod` to remove write permission from a file.
4. Try writing to the file again and observe the error.
5. Use `man grep` or `grep --help` to inspect options.

---

## Build-Up Exercise

Create a Linux command cheat sheet in `00_setup_and_notes/linux_commands.md`.

For each command, record:

- command name
- what it does
- common options
- example
- what type of output it gives
- how Python might use or replace it later

---

## Module Capstone: Linux Command Workbook

Build a workbook folder containing:

```text
06_linux_fundamentals/
├── linux_commands.md
├── sample_logs/
├── command_outputs/
└── notes.md
```

You should save output from commands into files using redirection:

```bash
ls -lah > command_outputs/listing.txt
ps aux > command_outputs/processes.txt
```

---

## Review Checklist

You are ready to move on when you can explain:

- current directory versus absolute path
- what `ls -lah` shows
- what permissions roughly mean
- what a pipe does
- what redirection does
- why logs are usually text files
- how Linux commands relate to automation

---

# Module 7: Filesystem Automation with `pathlib`, `os`, and `shutil`

## Purpose

This module connects Linux file knowledge to Python file automation. You will inspect folders, filter files, check sizes, move files, copy files, and produce reports.

---

## Concept Explainer

The filesystem is where real automation starts. Most admin scripts do some version of this:

- scan a folder
- find files matching rules
- check file size or date
- copy/move/archive files
- write a report
- avoid damaging anything accidentally

Python gives several tools for this. `pathlib` is the modern path-handling module. `os` gives lower-level operating system functions. `shutil` handles copying, moving, and deleting file trees.

---

## Syntax and Parameter Breakdown

### `Path("some/path")`

```python
from pathlib import Path

folder = Path("data")
```

| Part | Type | Meaning |
|---|---|---|
| `Path` | class | creates a path object |
| `"data"` | string | path text |
| `folder` | Path object | object representing the path |

### `Path.iterdir()`

```python
for item in folder.iterdir():
    print(item)
```

| Method | Belongs To | Takes In | Returns |
|---|---|---|---|
| `.iterdir()` | Path object | nothing | iterator of Path objects |

### Common `Path` methods

| Method/Attribute | Returns | Meaning |
|---|---|---|
| `.exists()` | bool | path exists |
| `.is_file()` | bool | path is a file |
| `.is_dir()` | bool | path is a directory |
| `.suffix` | string | file extension |
| `.name` | string | final filename |
| `.stat()` | stat object | size, times, permissions |

### `shutil.copy2(source, destination)`

Copies file and keeps metadata.

| Parameter | Type | Meaning |
|---|---|---|
| `source` | string or Path | file to copy |
| `destination` | string or Path | target location |

---

## Tiny Example

```python
from pathlib import Path

folder = Path("data")

for item in folder.iterdir():
    if item.is_file():
        print(item.name, item.suffix, item.stat().st_size)
```

---

## Guided Practice / Lab Sheet

Create folder:

```text
data/sample_files/
```

Add a mix of `.txt`, `.csv`, `.log`, and `.md` files.

Create `file_scanner.py`.

Steps:

1. Import `Path`.
2. Create a Path object for the folder.
3. Check whether the folder exists.
4. Loop through the folder.
5. Print only files.
6. Print filename, extension, and size.
7. Count each file extension.

---

## Variation Drills

1. List only `.log` files.
2. Find files over a size limit.
3. Find empty files.
4. Copy `.csv` files into an archive folder.
5. Write a report to `output/file_report.txt`.

---

## Build-Up Exercise

Create `folder_audit.py`.

It should:

- scan a chosen folder
- count files by extension
- identify empty files
- identify large files
- identify old files if you want the date challenge
- write a text report

---

## Module Capstone: Linux File Doctor

Build a safe filesystem inspection tool.

Required features:

- use `pathlib`
- accept a folder path in a variable
- check if folder exists
- scan files recursively using `.rglob("*")`
- count file types
- report empty files
- report large files
- write report to output folder
- never delete files in version 1

Optional version 2:

- archive files by extension
- dry-run mode
- command-line argument for folder path

---

## Review Checklist

You are ready to move on when you can explain:

- string path versus Path object
- what `.iterdir()` returns
- what `.rglob()` does
- how `.stat().st_size` works
- why file-moving scripts need dry-run mode
- when to use `shutil`

---

# Module 8: Logging and Log Parsing

## Purpose

This module teaches two different meanings of “logging”:

1. Your Python program writing its own log messages.
2. Your Python program reading existing log files to find useful information.

Both matter.

---

## Concept Explainer

A log is a record of events. Systems, applications, web servers, scripts, and network tools all produce logs.

In real work, logs help answer questions such as:

- What happened?
- When did it happen?
- Was it an error, warning, or normal event?
- Which user, IP, file, or service was involved?
- Is the same problem repeating?

Python’s `logging` module lets your scripts record what they are doing. Log parsing lets your scripts read existing logs and summarise patterns.

---

## Syntax and Parameter Breakdown

### `logging.basicConfig(...)`

```python
import logging

logging.basicConfig(
    filename="output/script.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
```

| Parameter | Type | Example | Meaning |
|---|---|---|---|
| `filename` | string | `"output/script.log"` | where logs are written |
| `level` | logging constant | `logging.INFO` | minimum severity to record |
| `format` | string | `"%(levelname)s %(message)s"` | layout of each log line |

### Logging functions

| Function | Meaning |
|---|---|
| `logging.debug()` | detailed troubleshooting info |
| `logging.info()` | normal event |
| `logging.warning()` | something odd but not fatal |
| `logging.error()` | something failed |
| `logging.critical()` | serious failure |

### Basic log parsing

```python
if "ERROR" in line:
    error_count += 1
```

This is simple string matching.

### Regex parsing

```python
import re

ip_pattern = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")
match = ip_pattern.search(line)
```

| Part | Meaning |
|---|---|
| `re.compile()` | prepares a reusable pattern |
| `.search(line)` | finds first match in text |
| `.findall(line)` | finds all matches |
| raw string `r"..."` | avoids escaping backslashes twice |

---

## Tiny Example

```python
import logging

logging.basicConfig(
    filename="output/run.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Script started")
logging.warning("This is a warning")
logging.error("This is an error")
```

---

## Guided Practice / Lab Sheet

Create `data/app.log`:

```text
2026-07-01 09:00:01 INFO service started
2026-07-01 09:01:10 WARNING disk almost full
2026-07-01 09:02:44 ERROR failed login from 192.168.1.20
2026-07-01 09:03:55 ERROR failed login from 192.168.1.20
2026-07-01 09:04:12 INFO backup complete
```

Create `log_parser.py`.

Steps:

1. Open the log file.
2. Count `INFO`, `WARNING`, and `ERROR` lines.
3. Extract lines containing `failed login`.
4. Extract IP addresses using simple splitting first.
5. Write a summary file.

---

## Variation Drills

1. Use regex to extract IP addresses.
2. Count failed logins per IP.
3. Print the top offending IP.
4. Add Python logging to record your parser’s progress.
5. Handle missing log file gracefully.

---

## Build-Up Exercise

Create `log_summary_reporter.py`.

It should:

- read one or more `.log` files
- count severity levels
- extract IPs
- count repeated errors
- write summary report
- write parser activity to its own log file

---

## Module Capstone: Log Watcher

Build a log analysis tool.

Required features:

- read log files from `data/logs`
- count `INFO`, `WARNING`, `ERROR`, `CRITICAL`
- extract IP addresses
- count failed login events
- detect repeated IP addresses
- write `output/log_summary.txt`
- write `output/parser_run.log`

Optional version 2:

- accept a severity threshold
- output JSON summary
- watch a file using repeated reads later

---

## Review Checklist

You are ready to move on when you can explain:

- the difference between program logging and log parsing
- what `logging.basicConfig()` configures
- what `level` controls
- why logs are usually plain text
- when simple string matching is enough
- when regex becomes useful
- what `.search()` returns

---

# Module 9: `subprocess` and Operating-System Interaction

## Purpose

This module teaches Python how to run external commands safely and capture their output. This is a major bridge between Python and Linux/system administration.

---

## Concept Explainer

`subprocess` lets Python start another program or command. For example, Python can run `ls`, `ping`, `whoami`, `ip addr`, or `df -h`, then capture the output.

This is powerful because many useful tools already exist at the OS level. Python can act as the organiser: run command, capture output, parse output, write report.

But it must be used carefully. Running shell commands with unchecked user input can be dangerous.

---

## Syntax and Parameter Breakdown

### `subprocess.run(...)`

```python
import subprocess

result = subprocess.run(
    ["ls", "-lah"],
    capture_output=True,
    text=True,
    check=False
)
```

| Parameter | Type | Example | Meaning |
|---|---|---|---|
| first argument | list of strings | `["ls", "-lah"]` | command and arguments |
| `capture_output` | bool | `True` | capture stdout/stderr |
| `text` | bool | `True` | return strings instead of bytes |
| `check` | bool | `False` | if True, raise error on non-zero exit |

Returns:

| Return Type | Important Attributes |
|---|---|
| `CompletedProcess` object | `.args`, `.returncode`, `.stdout`, `.stderr` |

Example inspection:

```python
print(result.returncode)
print(result.stdout)
print(result.stderr)
```

### Avoid this early on

```python
subprocess.run("ls -lah", shell=True)
```

`shell=True` can be useful but dangerous. Start with list-style commands.

---

## Tiny Example

```python
import subprocess

result = subprocess.run(
    ["whoami"],
    capture_output=True,
    text=True
)

print("Return code:", result.returncode)
print("Output:", result.stdout.strip())
```

---

## Guided Practice / Lab Sheet

Create `command_runner.py`.

Run these commands using `subprocess.run()`:

- `whoami`
- `pwd`
- `ls -lah`
- `df -h`

For each command:

1. Store result in a variable.
2. Print return code.
3. Print stdout.
4. Print stderr if present.
5. Write selected output to a report file.

---

## Variation Drills

1. Run a command that fails and inspect return code.
2. Use `check=True` and catch `subprocess.CalledProcessError`.
3. Create a helper function called `run_command(command_parts)`.
4. Return a dictionary with command, return code, stdout, stderr.
5. Write command results to JSON.

---

## Build-Up Exercise

Create `system_snapshot.py`.

It should run:

- `whoami`
- `hostname`
- `pwd`
- `df -h`
- `ip addr` or equivalent available command

Then write a report.

---

## Module Capstone: Command Runner Report Tool

Build a safe subprocess-based reporting tool.

Required features:

- run approved commands only
- capture stdout and stderr
- store return codes
- write a text report
- write a JSON report
- log errors
- avoid `shell=True`

Optional version 2:

- allow command selection from a menu
- add timeout handling
- parse useful values from output

---

## Review Checklist

You are ready to move on when you can explain:

- what a subprocess is
- why the command is usually a list of strings
- what stdout and stderr are
- what return code means
- what `CompletedProcess` contains
- why `shell=True` needs caution
- how subprocess connects Python to Linux tools

---

# Module 10: Command-Line Interfaces and `argparse`

## Purpose

This module turns scripts into tools. A script that needs editing every time is not a proper tool. A command-line interface lets you pass inputs when running the program.

---

## Concept Explainer

A command-line interface, or CLI, lets users control a program through terminal arguments.

Instead of editing this inside the code:

```python
folder = "data"
```

You run:

```bash
python file_doctor.py data --large-limit 1000000
```

This matters because real admin tools need reusable inputs: folder path, output file, severity level, hostname, port, dry-run mode, and so on.

---

## Syntax and Parameter Breakdown

### `argparse.ArgumentParser()`

```python
import argparse

parser = argparse.ArgumentParser(description="Scan files and write a report")
```

Creates a parser object.

### `.add_argument(...)`

```python
parser.add_argument("folder", help="Folder to scan")
parser.add_argument("--limit", type=int, default=1000000)
parser.add_argument("--dry-run", action="store_true")
```

| Parameter | Type | Meaning |
|---|---|---|
| first argument | string | argument name |
| `help` | string | help text |
| `type` | callable | converts input, e.g. `int` |
| `default` | any | value if not supplied |
| `action="store_true"` | string | Boolean flag |

### `.parse_args()`

```python
args = parser.parse_args()
print(args.folder)
print(args.limit)
print(args.dry_run)
```

Returns a namespace object. Its attributes match argument names.

---

## Tiny Example

```python
import argparse

parser = argparse.ArgumentParser(description="Say hello")
parser.add_argument("name", help="Name to greet")
parser.add_argument("--shout", action="store_true")

args = parser.parse_args()

message = f"Hello {args.name}"

if args.shout:
    message = message.upper()

print(message)
```

Run:

```bash
python hello_cli.py Gav
python hello_cli.py Gav --shout
```

---

## Guided Practice / Lab Sheet

Create `invoice_cli.py`.

It should accept:

```bash
python invoice_cli.py data/invoices.csv --status PAID --output output/paid.csv
```

Arguments:

- input CSV path
- optional `--status`
- optional `--output`

Steps:

1. Create parser.
2. Add positional input file.
3. Add optional status filter.
4. Add optional output file.
5. Print parsed arguments first.
6. Then connect to CSV reading.

---

## Variation Drills

1. Add `--summary-only` as a Boolean flag.
2. Add `--min-amount` as a float.
3. Add `--dry-run`.
4. Add helpful error messages.
5. Add `--format text/json` using `choices=["text", "json"]`.

---

## Build-Up Exercise

Convert an earlier project into a CLI tool.

Suggested choice:

- Linux File Doctor
- Log Watcher
- Monthly Report Generator

Add arguments for input folder, output folder, and dry-run mode.

---

## Module Capstone: Admin Automation CLI

Build one reusable CLI tool that can run at least two commands:

```bash
python admin_tool.py scan-files data/sample_files --output output/files.txt
python admin_tool.py clean-invoices data/invoices.csv --output output/invoices.csv
```

This may use subcommands with `argparse`, or a simpler menu-based version first.

Required features:

- accepts command-line arguments
- validates input paths
- writes output files
- has `--help`
- has a README with example commands

---

## Review Checklist

You are ready to move on when you can explain:

- positional argument versus optional argument
- what `type=int` does
- what `default` means
- what `store_true` means
- what `args` contains
- why CLI tools are better than editing variables manually

---

# Module 11: OOP for Practical Tools

## Purpose

This module teaches object-oriented programming without drifting into abstract nonsense. Classes are used when they help organise real data and behaviour.

---

## Concept Explainer

A class is a blueprint. An object is a thing created from that blueprint.

A class can hold:

- data attributes: what the object knows
- methods: what the object can do

For practical tools, OOP becomes useful when you have repeated structured records or tool components:

- Invoice
- Expense
- LogEntry
- HostCheckResult
- ReportWriter
- FileScanResult
- ServiceTicket

OOP should not be used just to look fancy. Use it when it makes the program clearer.

---

## Syntax and Parameter Breakdown

### Class definition

```python
class Invoice:
    def __init__(self, invoice_id, supplier, amount, status):
        self.invoice_id = invoice_id
        self.supplier = supplier
        self.amount = amount
        self.status = status
```

| Part | Meaning |
|---|---|
| `class Invoice:` | defines a new class |
| `__init__` | initializer method, runs when object is created |
| `self` | the specific object being worked on |
| `invoice_id` etc. | parameters passed when creating object |
| `self.invoice_id` | attribute stored on object |

### Creating an object

```python
invoice = Invoice("INV001", "Acme Supplies", 145.50, "PAID")
```

| Argument | Type | Goes Into |
|---|---|---|
| `"INV001"` | string | `invoice_id` |
| `"Acme Supplies"` | string | `supplier` |
| `145.50` | float | `amount` |
| `"PAID"` | string | `status` |

### Method

```python
class Invoice:
    def __init__(self, invoice_id, supplier, amount, status):
        self.invoice_id = invoice_id
        self.supplier = supplier
        self.amount = amount
        self.status = status

    def is_paid(self):
        return self.status == "PAID"
```

`is_paid()` takes no external parameter, but it still has `self` because it needs the object’s own data.

### `__str__`

```python
    def __str__(self):
        return f"{self.invoice_id} - {self.supplier} - €{self.amount:.2f} - {self.status}"
```

Returns a human-readable string when printing the object.

---

## Tiny Example

```python
class Invoice:
    def __init__(self, invoice_id, supplier, amount, status):
        self.invoice_id = invoice_id
        self.supplier = supplier
        self.amount = amount
        self.status = status

    def is_paid(self):
        return self.status == "PAID"

invoice = Invoice("INV001", "Acme Supplies", 145.50, "PAID")
print(invoice.supplier)
print(invoice.is_paid())
```

---

## Guided Practice / Lab Sheet

Create `invoice.py`.

Define an `Invoice` class with:

- `invoice_id`
- `supplier`
- `amount`
- `status`

Methods:

- `is_paid()` returns Boolean
- `is_large(limit=500.0)` returns Boolean
- `to_dict()` returns dictionary
- `__str__()` returns readable string

Create `main.py` to test it.

---

## Variation Drills

1. Add validation so amount cannot be negative.
2. Add `mark_paid()` method.
3. Add `from_csv_row(row)` as a helper function or class method later.
4. Create an `Expense` class.
5. Create a list of Invoice objects and filter paid invoices.

---

## Build-Up Exercise

Create a small service desk model.

Classes:

- `Ticket`
- `Customer`
- `Device`

Keep it simple. Each class should have attributes, `__str__`, and one or two useful methods.

---

## Module Capstone: Service Desk Record System

Build a command-line record manager using classes.

Required classes:

- `Ticket`
- `Customer`
- `Device`
- `ReportWriter` or similar

Required features:

- create records
- store records in lists
- search by ID or name
- update ticket status
- write a report
- separate class files from `main.py`

Optional version 2:

- save/load JSON
- use inheritance for different ticket types
- add validation methods

---

## Review Checklist

You are ready to move on when you can explain:

- class versus object
- why `self` exists
- what `__init__` does
- attribute versus method
- why methods can use object data
- when OOP helps
- when OOP is overkill

---

# Module 12: Debugging, Testing, Git, and README Writing

## Purpose

This module makes your projects more serious. A project is not just code that worked once. It needs debugging habits, tests, version control, and documentation.

---

## Concept Explainer

Debugging is the process of finding and fixing problems. Testing is the habit of checking code with known inputs and expected outputs. Git records project history. A README explains what the project does and how to run it.

These are not extras. They are what make a project believable.

---

## Syntax and Parameter Breakdown

### `assert`

```python
assert calculate_total([1, 2, 3]) == 6
```

If the condition is false, Python raises an `AssertionError`.

### Basic `pytest` style later

```python
def test_calculate_total():
    assert calculate_total([1, 2, 3]) == 6
```

### Git commands

| Command | Meaning |
|---|---|
| `git status` | show changed files |
| `git add .` | stage changes |
| `git commit -m "message"` | save checkpoint |
| `git log --oneline` | show commit history |
| `git push` | upload to remote repo |

---

## Tiny Example

```python
def calculate_total(amounts):
    return sum(amounts)

assert calculate_total([1, 2, 3]) == 6
assert calculate_total([]) == 0
```

---

## Guided Practice / Lab Sheet

Pick one earlier project.

Tasks:

1. Add three `assert` checks for simple functions.
2. Add clear error messages.
3. Run the file.
4. Break one test on purpose.
5. Fix it.
6. Commit changes with Git.
7. Write a README.

README should include:

- project name
- what it does
- how to run it
- sample input
- sample output
- what you learned
- next improvements

---

## Variation Drills

1. Add tests for bad input.
2. Add a known CSV test file.
3. Add a Git commit for each meaningful change.
4. Add a troubleshooting section to README.
5. Add a “limitations” section.

---

## Build-Up Exercise

Polish one previous capstone as if showing it to someone else.

Required:

- clean folder structure
- README
- sample data
- output example
- at least five commits
- at least three tests/assertions

---

## Module Capstone: Polished Repo Checkpoint

Choose one project from Modules 4 to 11 and polish it.

Deliverables:

- GitHub-ready folder
- README
- sample data
- clean output
- comments where useful
- no dead files
- no random `test_final_REAL.py` disaster files

---

## Review Checklist

You are ready to move on when you can explain:

- what a test checks
- why known input/output matters
- how Git commits act as checkpoints
- what a README must explain
- how to make a project understandable after a month away

---

# Module 13: Web Basics, HTML, HTTP, and Requests

## Purpose

This module introduces web basics from a networking-adjacent angle. You will learn enough HTML and HTTP to understand how simple web pages, requests, responses, and status dashboards work.

---

## Concept Explainer

HTML is the structure of a web page. HTTP is the protocol used for web requests and responses.

A browser sends an HTTP request. A server sends back an HTTP response. That response might contain HTML, JSON, an image, or an error.

For practical Python, web basics matter because tools often:

- request data from APIs
- generate HTML reports
- check whether a website is up
- parse response codes
- build local dashboards

---

## Syntax and Parameter Breakdown

### Basic HTML

```html
<!DOCTYPE html>
<html>
<head>
    <title>Status Report</title>
</head>
<body>
    <h1>System Status</h1>
    <p>All checks complete.</p>
</body>
</html>
```

| Tag | Meaning |
|---|---|
| `<html>` | page root |
| `<head>` | metadata |
| `<title>` | browser tab title |
| `<body>` | visible content |
| `<h1>` | heading |
| `<p>` | paragraph |
| `<table>` | table |

### `requests.get(url)`

Requires third-party package `requests`.

```python
import requests

response = requests.get("https://example.com", timeout=5)
print(response.status_code)
print(response.text[:100])
```

| Parameter | Type | Meaning |
|---|---|---|
| `url` | string | target web address |
| `timeout` | int/float | seconds before giving up |

Returns:

| Type | Important Attributes |
|---|---|
| Response object | `.status_code`, `.text`, `.json()` |

---

## Tiny Example

Generate an HTML report from Python:

```python
html = """
<!DOCTYPE html>
<html>
<body>
<h1>Invoice Summary</h1>
<p>Total invoices: 10</p>
</body>
</html>
"""

with open("output/report.html", "w", encoding="utf-8") as file:
    file.write(html)
```

---

## Guided Practice / Lab Sheet

Create `html_report_generator.py`.

It should:

1. Store report data in a dictionary.
2. Build an HTML string.
3. Write it to `output/report.html`.
4. Open the file in a browser.
5. Add a table of invoices.

---

## Variation Drills

1. Add CSS inside `<style>`.
2. Create a table from a list of dictionaries.
3. Add warning rows for unpaid invoices.
4. Use `requests.get()` to check a website status.
5. Write website check results into HTML.

---

## Build-Up Exercise

Create a local status dashboard.

It should show:

- file scan summary
- invoice summary
- log summary
- network check summary later

---

## Module Capstone: Mini HTML Status Dashboard

Build a generated HTML dashboard.

Required features:

- reads summary JSON files from previous tools
- builds one HTML page
- includes tables
- includes headings
- includes generated timestamp
- writes to `output/dashboard.html`

Optional version 2:

- add basic CSS
- auto-open in browser
- include network status checks

---

## Review Checklist

You are ready to move on when you can explain:

- what HTML is for
- what HTTP does
- what a status code means
- what `requests.get()` returns
- why APIs often return JSON
- how Python can generate HTML reports

---

# Module 14: Sockets and Network Programming Basics

## Purpose

This module introduces sockets slowly. Sockets can feel strange at first because you are no longer just reading files or printing reports. You are sending data between programs over a network connection.

---

## Concept Explainer

A socket is an endpoint for network communication. One program can listen for connections. Another program can connect to it. Once connected, they can send and receive bytes.

Sockets are the foundation underneath many networked systems. You do not need to build the internet from scratch, thankfully. But understanding sockets helps networking concepts become real.

Start with TCP:

- server creates socket
- server binds to IP and port
- server listens
- client connects
- client sends data
- server receives data
- server replies

---

## Syntax and Parameter Breakdown

### Create a TCP socket

```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

| Argument | Meaning |
|---|---|
| `socket.AF_INET` | IPv4 addressing |
| `socket.SOCK_STREAM` | TCP socket |

### Bind and listen

```python
server_socket.bind(("127.0.0.1", 5000))
server_socket.listen()
```

| Method | Takes In | Meaning |
|---|---|---|
| `.bind((host, port))` | tuple: string, int | choose local address and port |
| `.listen()` | optional backlog | start listening |

### Accept connection

```python
client_socket, client_address = server_socket.accept()
```

Returns:

| Value | Meaning |
|---|---|
| `client_socket` | socket for that client |
| `client_address` | tuple containing IP and port |

### Send and receive

```python
data = client_socket.recv(1024)
client_socket.sendall(b"Hello")
```

| Method | Takes In | Returns |
|---|---|---|
| `.recv(1024)` | max bytes to read | bytes |
| `.sendall(data)` | bytes | None |

Important: sockets send bytes, not normal strings. Use `.encode()` and `.decode()`.

---

## Tiny Example

Client sends message:

```python
message = "hello server"
data = message.encode("utf-8")
```

Server receives bytes:

```python
received = data.decode("utf-8")
```

---

## Guided Practice / Lab Sheet

Build two files:

```text
server.py
client.py
```

Version 1:

- server listens on `127.0.0.1:5000`
- client connects
- client sends `hello`
- server prints it
- server sends `message received`
- client prints response

Do not add threading yet.

---

## Variation Drills

1. Change the port.
2. Send username and message.
3. Add a loop so the client can send multiple messages.
4. Add `quit` to close connection.
5. Log messages to a file.

---

## Build-Up Exercise

Build a simple diagnostic server.

Client sends commands:

- `TIME`
- `STATUS`
- `HELP`
- `QUIT`

Server replies with text.

---

## Module Capstone: TCP Echo and Diagnostic Tool

Build a small TCP client/server pair.

Required features:

- TCP server
- TCP client
- message encoding/decoding
- command handling
- clean quit behaviour
- logging to file
- README explaining host, port, and usage

Optional version 2:

- handle multiple clients later
- add threading later
- send JSON messages later

---

## Review Checklist

You are ready to move on when you can explain:

- what a socket is
- client versus server
- IP address versus port
- why TCP uses connections
- why socket data is bytes
- what `.encode()` and `.decode()` do
- what `.bind()`, `.listen()`, `.accept()`, `.connect()`, `.sendall()`, and `.recv()` do

---

# Module 15: Network Support Tools

## Purpose

This module combines Python, Linux, subprocess, sockets, and basic networking into support-style tools.

---

## Concept Explainer

A network support tool helps answer questions such as:

- Is this host reachable?
- Does DNS resolve?
- Is this port open?
- Which checks passed or failed?
- Can I write a status report?

This module should stay ethical and defensive. Only test systems you own, have permission to test, or are using in a lab.

---

## Syntax and Parameter Breakdown

### Ping through subprocess

```python
result = subprocess.run(
    ["ping", "-c", "1", "127.0.0.1"],
    capture_output=True,
    text=True
)
```

| Part | Meaning |
|---|---|
| `ping` | command |
| `-c 1` | send one packet on Linux |
| `127.0.0.1` | target host |

### DNS lookup with socket

```python
import socket

ip_address = socket.gethostbyname("example.com")
```

| Function | Takes In | Returns |
|---|---|---|
| `socket.gethostbyname()` | hostname string | IPv4 address string |

### Port check with socket

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)
result = sock.connect_ex(("127.0.0.1", 80))
sock.close()
```

| Method | Meaning |
|---|---|
| `.settimeout(3)` | give up after 3 seconds |
| `.connect_ex((host, port))` | returns 0 if connection succeeds |

---

## Tiny Example

```python
import socket

host = "example.com"

try:
    ip = socket.gethostbyname(host)
    print(host, "resolves to", ip)
except socket.gaierror:
    print("DNS lookup failed")
```

---

## Guided Practice / Lab Sheet

Create `hosts.csv`:

```csv
name,host,port
Localhost,127.0.0.1,80
Example,example.com,80
GoogleDNS,8.8.8.8,53
```

Create `network_checker.py`.

Steps:

1. Read hosts from CSV.
2. For each host, try DNS lookup if needed.
3. Ping host using subprocess.
4. Check port using socket.
5. Store results in dictionaries.
6. Write a CSV report.

---

## Variation Drills

1. Add timeout setting.
2. Add JSON output.
3. Add HTML dashboard output.
4. Add `--host-file` CLI argument.
5. Add logging.

---

## Build-Up Exercise

Create `network_reporter.py`.

It should combine:

- CSV input
- subprocess ping
- socket port check
- dictionary result records
- report generation
- logging
- error handling

---

## Module Capstone: Network Check Reporter

Build a network support report tool.

Required features:

- reads `data/hosts.csv`
- checks DNS where applicable
- pings host
- checks configured port
- writes `output/network_report.csv`
- writes `output/network_report.json`
- writes `output/network_summary.txt`
- logs tool activity
- includes README and safe-use note

Optional version 2:

- HTML dashboard
- CLI arguments
- retries
- latency parsing
- simple socket server integration from Module 14

---

## Review Checklist

You are ready to move on when you can explain:

- DNS resolution versus ping
- host versus port
- what `connect_ex()` returns
- why timeouts matter
- why network tools need permission boundaries
- how subprocess and sockets solve different problems

---

# Module 16: Final Capstone

## Final Project: Hybrid System, Network & Admin Toolkit

## Purpose

The final capstone combines the full course into one coherent toolkit. It should look like something a junior IT support/admin automation student could show as evidence of skill.

This is not one giant messy script. It should be a structured project.

---

## Project Identity

Name suggestion:

```text
practical_admin_network_toolkit
```

Short description:

> A Python toolkit for scanning folders, cleaning admin data, parsing logs, running safe system checks, checking network hosts, and generating text/JSON/HTML reports.

---

## Required Features

The final toolkit must include at least five tool modes.

### 1. File Audit

Scans a folder and reports:

- total files
- file types
- empty files
- large files
- largest files
- output report

Uses:

- `pathlib`
- dictionaries
- file writing
- error handling

### 2. Invoice / Expense Cleaner

Reads CSV files and reports:

- valid records
- bad rows
- totals
- paid/unpaid/query statuses
- unique suppliers

Uses:

- `csv`
- dictionaries
- lists
- sets
- exceptions
- report writing

### 3. Log Watcher

Reads logs and reports:

- severity counts
- repeated errors
- failed login events
- IP address counts

Uses:

- file reading
- string methods
- regex
- dictionaries
- logging

### 4. System Snapshot

Runs safe Linux commands and reports:

- current user
- hostname
- disk usage
- current directory
- selected network info if available

Uses:

- `subprocess.run()`
- stdout/stderr handling
- return codes
- JSON output

### 5. Network Check Reporter

Reads a host list and reports:

- DNS lookup result
- ping result
- port check result
- summary status

Uses:

- `socket`
- `subprocess`
- CSV input
- structured output

---

## Project Structure

```text
practical_admin_network_toolkit/
├── README.md
├── data/
│   ├── invoices.csv
│   ├── expenses.csv
│   ├── hosts.csv
│   └── logs/
│       └── app.log
├── output/
│   ├── reports/
│   └── logs/
├── src/
│   ├── main.py
│   ├── file_audit.py
│   ├── invoice_cleaner.py
│   ├── log_watcher.py
│   ├── system_snapshot.py
│   ├── network_checker.py
│   ├── report_writer.py
│   └── models.py
└── tests/
    ├── test_invoice_cleaner.py
    └── test_file_audit.py
```

---

## CLI Design

Example commands:

```bash
python src/main.py file-audit data/sample_files --output output/reports/file_audit.txt
python src/main.py clean-invoices data/invoices.csv --output output/reports/invoices.csv
python src/main.py parse-logs data/logs --output output/reports/log_summary.txt
python src/main.py system-snapshot --output output/reports/system_snapshot.json
python src/main.py check-network data/hosts.csv --output output/reports/network_report.csv
python src/main.py dashboard --output output/reports/dashboard.html
```

---

## Minimum Technical Requirements

The final project must use:

- functions
- modules
- dictionaries
- lists
- sets
- file I/O
- CSV reading/writing
- JSON reading/writing
- exception handling
- logging
- `pathlib`
- `subprocess`
- `argparse`
- at least one class
- Git commits
- README
- sample input data
- sample output files

Optional:

- HTML dashboard
- socket client/server mode
- tests with `pytest`
- config file
- richer terminal output

---

## Capstone Build Plan

### Phase 1: Skeleton

- create folder structure
- create README draft
- create empty module files
- create sample data
- create `main.py`
- commit

### Phase 2: File Audit Tool

- scan folder
- collect results
- write report
- commit

### Phase 3: Invoice Cleaner

- read CSV
- validate rows
- write clean and bad rows
- commit

### Phase 4: Log Watcher

- read logs
- count severities
- extract IPs
- write report
- commit

### Phase 5: System Snapshot

- run safe commands
- capture outputs
- write JSON
- commit

### Phase 6: Network Checker

- read host CSV
- DNS lookup
- ping
- port check
- write report
- commit

### Phase 7: CLI Integration

- add argparse
- connect subcommands
- add help text
- commit

### Phase 8: Final Polish

- README
- screenshots or sample output
- tests
- cleanup
- final commit

---

## Final README Requirements

The README must include:

- project name
- what problem it solves
- features
- setup instructions
- example commands
- sample input
- sample output
- technologies used
- what you learned
- limitations
- future improvements
- ethical/safe-use note for network checks

---

## Final Review Questions

At the end of the course, you should be able to answer:

1. What does each module in your final project do?
2. What types move through the program?
3. Where are strings converted to numbers?
4. Where are exceptions handled?
5. Where does logging happen?
6. Which functions return data and which write files?
7. Which parts use Linux commands?
8. Which parts use sockets?
9. Which parts could break on another machine?
10. What would you improve next?

---

# Ongoing Drill Template

Use this format for individual practice sessions.

```text
DRILL [number] — [Topic]
Difficulty: ⭐ / ⭐⭐ / ⭐⭐⭐

TASK:
Plain English description of what the code should do.

INPUT:
What the function/method/script takes in.
Name, type, example value.

OUTPUT / RETURN:
What it should return or write.
Type and example.

RULES:
Any constraints.

YOUR TURN:
Write it from scratch.
```

After each submitted attempt, review should follow:

1. What is correct.
2. What is broken.
3. Why it is broken.
4. Corrected version if needed.
5. One variation.
6. One short thing to remember.

---

# Project Difficulty Ladder

## Level 1: Single Concept

Example:

- write a function that validates an amount
- read one file
- split one string
- check one host

## Level 2: Combined Concepts

Example:

- read CSV and calculate totals
- scan folder and group extensions
- parse log and count errors

## Level 3: Tool

Example:

- invoice cleaner
- file doctor
- log watcher
- network reporter

## Level 4: Toolkit

Example:

- one CLI with multiple subcommands
- structured modules
- shared report writer
- logging
- README

## Level 5: Independent Capstone

Example:

- hybrid system/network/admin toolkit
- proper documentation
- sample data
- tests
- Git history

---

# What To Avoid

Avoid learning patterns that look productive but do not build skill.

Do not:

- copy full solutions before trying
- watch long tutorials without coding
- build giant scripts with no functions
- move on while still confused about inputs and returns
- ignore error messages
- leave projects undocumented
- keep twenty files called `final_final2.py`
- treat AI output as understanding

Do:

- type code manually
- print types often
- inspect return values
- use small functions
- test with bad input
- write reports
- commit often
- explain your code back in plain English

---

# Completion Standard

This syllabus is complete when you have:

- finished each module capstone
- reviewed mistakes
- created variations
- pushed work to GitHub
- written READMEs
- built the final toolkit
- explained the final project without reading the code line by line

The real test is not whether the code runs once.

The real test is whether you can return to it later, understand it, modify it, and build the next thing from it.
