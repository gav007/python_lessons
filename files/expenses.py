def read_expenses():
    
    expense_label = []
    expense_cost = []

    with open("expenses.txt", "r") as file:
        
        contents = file.readlines()
        
        for line in contents:
            
            line = line.strip().split(",")
            
            if len(line) != 2:
                
                print("Bad line found")
                
                continue

            name = line[0]
            
            try:
                
                cost = float(line[1])
                expense_label.append(name)
                expense_cost.append(cost)
            
            except ValueError:
            
                print("Sent for review")
                
                continue

            
        return expense_label, expense_cost

def calculate_total(cost):
    total = 0
    
    for item in cost:
        total += item

    return total


def main():
    label, cost = read_expenses()
    total_cost = calculate_total(cost)

    with open("expenses_output.txt", "w") as out_file:
        
        out_file.write("-"*35+"\n")
        out_file.write("Expenses" + "\n")
        out_file.write("-"*35+"\n")

        for i in range(len(label)):
            cost_text = str(cost[i])
            out_file.write(label[i] + " " + cost_text+ "\n")

        out_file.write("Total: " + str(total_cost) + "\n")


main()
