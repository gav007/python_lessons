# Task:
# Ask the user for an invoice amount. Convert it to a float. 
# Print one of these messages:

# under 0: Invalid amount
# 0 to 99.99: Small invoice
# 100 to 499.99: Medium invoice
# 500 or more: Large invoice

SUPPLIER_NAME = "GAV'S WIDGETS"
RUNNING_TOTAL = 0
INVOICES = 3

while INVOICES > 0:
    while True:
        try:
            amount_text = input("Enter Value >> ")
            amount_text = float(amount_text)
            RUNNING_TOTAL += amount_text
            break
        except ValueError:
            print("Invalid Entry")

    if amount_text < 0:
        print("Invalid amount")
    elif amount_text == 0:
        print("Amount is Zero? Come-on")
    elif amount_text < 100:
        print(f"Small invoice from {SUPPLIER_NAME}")
    elif amount_text < 500:
        print(f"Medium invoice from {SUPPLIER_NAME}")
    else:
        print(f"Large invoice from {SUPPLIER_NAME}")
    
    INVOICES -= 1

print(f"The total was {RUNNING_TOTAL}")
        
