def read_invoices():
    paid_invoice = []
    unpaid_invoice = []
    query_items = []

    with open("invoices.txt", "r") as file:

        for line in file:
            
            line = line.strip().split(",")

            if len(line) != 4:
                query_items.append(line)
                continue

            invoice_number = line[0].strip()
            supplier = line[1].strip()
            amount = line[2].strip()
            status = line[3].strip()

            try:
                amount = float(amount)
            except ValueError:
                query_items.append([invoice_number, supplier, amount, status, "Invalid amount"])
                continue

            clean_invoice = [invoice_number, supplier, amount, status] 
        

            if status == "UNPAID":
                unpaid_invoice.append(clean_invoice)
            elif status == "PAID":
                paid_invoice.append(clean_invoice)
            else:
                query_items.append(clean_invoice)

            #print(line)

    return paid_invoice, unpaid_invoice, query_items

def main():
    paid, unpaid, query = read_invoices()

    print("PAID:", paid)
    print("UNPAID:", unpaid)
    print("QUERY:", query)


if __name__ == "__main__":
    main()


