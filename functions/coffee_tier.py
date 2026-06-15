# One function takes in a number of coffees bought and returns a loyalty tier

def coffee_tier(coffee):
    
    if coffee < 5:
        return "Bronze"
    elif coffee <= 9:
        return "Silver"
    else:
        return "Gold"


def main():
    
    print("Enter number of coffee's bought")
    print("-"*20)

    while True:
    
        try:
            num_of_coffee = int(input("How many coffee's ? "))
            
            if num_of_coffee <= 0:
                print("You must purchase a coffee before a reward")
            else:
                reward = coffee_tier(num_of_coffee)
                print(f"You are entitled to a {reward} coupon")
                break

        except ValueError:
            print("Not a valid entry")


if __name__ == "__main__":
    main()
