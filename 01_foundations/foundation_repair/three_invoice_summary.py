# TASK

# The program should:

# Ask for three invoice amounts.
# Convert each to float.
# Keep a running total.
# Count how many are large invoices.
# Print the total and count.

# RULES:
# under 0: Invalid amount
# 0 to 99.99: Small invoice
# 100 to 499.99: Medium invoice
# 500 or more: Large invoice

RUNNING_TOTAL = 0
large_invoices = 0
runner = 3

while runner > 0:
    
    while True:
        try:
            invoice_text = input("Enter Invoice Amount >> ")
            invoice_float = float(invoice_text)
            RUNNING_TOTAL += invoice_float
            break
        except ValueError:
            print("Invalid Input")

    if invoice_float < 0:
        print("Invalid amount")
    elif invoice_float == 0:
        print("Amount is Zero? Come-on")
    elif invoice_float < 100:
        print(f"Small invoice")
    elif invoice_float < 500:
        print(f"Medium invoice")
    else:
        print(f"Large invoice")
        large_invoices += 1
        
    runner -= 1

print()   
print("SUMMARY")
print("-------------")
print("Total Amount:", RUNNING_TOTAL)
print("Large Invoices count:", large_invoices)
    