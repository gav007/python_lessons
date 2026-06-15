# The function should loop through a list of study minutes and return the total


def calculate_total_minutes(minutes_list):
    total_minutes = 0

    for session in minutes_list:
        total_minutes += session

    return total_minutes


def main():
    study_minutes = []

    while True:

        try:
            
            minutes = int(input("How many minutes this session? "))
            study_minutes.append(minutes)
            total = input(("Calculate the total minutes (y/n)? "))
            
            if total.lower() == "y":
                total_minutes = calculate_total_minutes(study_minutes)
                print(f"In this session you have studied for {total_minutes} minutes")
                break
            else:
                print("Keep going")

        except ValueError:

            print("Not a valid entry")


if __name__ == "__main__":
    main()
