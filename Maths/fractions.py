print("Enter your first fraction")

while True:
    try:
        a_num = int(input("First Numerator "))
        a_den = int(input("First Denominator "))
        b_num = int(input("Second Numerator "))
        b_den = int(input("Second Denominator "))
        if a_den == 0 or b_den == 0:
            print("Can't divide by zero")
            continue
        break
    
    except ValueError:
        print("A incorrect value was given")

print("===================================") 
print("===================================")   
  

print(f"Fraction A: {a_num} / {a_den}")
print(f"Fraction B: {b_num} / {b_den}")

frac_a = a_num/a_den
frac_b = b_num/b_den

fraction_A_greater = frac_a > frac_b

if fraction_A_greater:
    print(f"{a_num}/{a_den} is Greater than {b_num}/{b_den}")
else:
    print(f"{a_num}/{a_den} is Less than {b_num}/{b_den}")

common = a_den * b_den
#print(common)
first_adder = (common / a_den) * a_num
second_adder = (common / b_den) * b_num
sum_adder = int(first_adder + second_adder)

#print(f"{sum_adder} / {common}")

gcd = 1

smallest = min(sum_adder, common)

for i in range(2, smallest + 1):
    if sum_adder % i == 0 and common % i == 0:
        gcd = i

numerator = sum_adder // gcd
denominator = common // gcd

print(f"FACTION REDUCED {numerator}/{denominator}")
get_whole = numerator // denominator
get_remainder = numerator % denominator

print(f"FACTION REDUCED WHOLE {get_whole} {get_remainder}/{denominator}")