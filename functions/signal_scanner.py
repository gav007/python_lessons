# Open the file
# Loop through each line
# Count how many lines contain the search word
# Return the count



def count_signal_lines(filename, search_word):
    
    total = 0
    cleaned_search_word = search_word.strip().lower()

    with open(filename, "r") as file:
        for line in file:
            cleaned_line = line.strip().lower()
            if cleaned_search_word in cleaned_line:
                total += 1
                
    return total


def main():
    while True:
        try:
            
            search_word = input("Enter your word >> ")
            result = count_signal_lines("signal_log.txt", search_word)
            print("Number of times the word occurs:", result)
            break
        
        except FileNotFoundError:

            print("Not a valid file")


if __name__ == "__main__":
    main()
