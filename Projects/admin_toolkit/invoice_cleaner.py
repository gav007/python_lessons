# Designed for learning
# Build in nvim
# Reads in messy invoice lines and cleans them

def clean_invoice(file_name):
   
    valid_invoices = []

    with open("data/" + file_name, "r") as file:

        for line in file:
            
            chunks = line.strip().split(",")
            
            if len(chunks) != 4:
                
                print("BAD LINE:", chunks)
            
            else:
                
                invoice_id_string = chunks[0]
                company_string = chunks[1]
                amount_string = chunks[2]
                status_string = chunks[3]

                try:
                    invoice_dict = {}
                    
                    amount_float = float(amount_string)
                    
                    invoice_dict["id"] = invoice_id_string
                    invoice_dict["company"] = company_string
                    invoice_dict["amount"] = amount_float
                    invoice_dict["status"] = status_string
                    
                    valid_invoices.append(invoice_dict)

                except ValueError:

                    print("BAD AMOUNT:", chunks)
    
    return valid_invoices                


def total_amounts_by_status(valid_invoices):
    
    """
    Takes in a list of invoice dictionaries.
    Adds up the total amount of money for each invoice status.
    Returns a dictionary with PAID, UNPAID, and QUERY totals.
    """
    
    amount_totals = {
        "PAID": 0,
        "UNPAID": 0,
        "QUERY": 0
    }
    
    for invoice in valid_invoices:
        
        if invoice["status"] == "PAID":
            amount_totals["PAID"] += invoice["amount"]
            
        elif invoice["status"] == "UNPAID":
            amount_totals["UNPAID"] += invoice["amount"]
            
        elif invoice["status"] == "QUERY":
            amount_totals["QUERY"] += invoice["amount"]
            
    return amount_totals


def count_invoices_by_status(valid_invoices):
    
    """
    Takes in a list of invoice dictionaries.
    Counts how many invoices have each status.
    Returns a dictionary with PAID, UNPAID, and QUERY counts.
    """
    
    status_counts = {
        "PAID": 0,
        "UNPAID": 0,
        "QUERY": 0
    }
    
    for invoice in valid_invoices:
        
        if invoice["status"] == "PAID":
            status_counts["PAID"] += 1
            
        elif invoice["status"] == "UNPAID":
            status_counts["UNPAID"] += 1
            
        elif invoice["status"] == "QUERY":
            status_counts["QUERY"] += 1
            
    return status_counts

def write_summary(status_dict, paid_dict):
    
    with open("reports/summary.txt", "w") as file:
        
        file.write("--- SUMMARY ---\n")
        for status in status_dict:
            #status_dict[status] = str(status_dict[status])
            file.write(status + " " + str(status_dict[status]) + '\n')
        
        file.write("-" * 20 + "\n")
                    
        for amount in paid_dict:
            #paid_dict[amount] = str(paid_dict[amount])
            file.write(amount + " " + str(paid_dict[amount]) + '\n')

def main():

    file_name = input("Enter your file name >> ")
    invoices = clean_invoice(file_name)
    amount_totals = total_amounts_by_status(invoices)
    status_counts = count_invoices_by_status(invoices)
    write_summary(status_counts, amount_totals)
    
    #print(status)
    #print(amount)

if __name__ == "__main__":
    main() 


