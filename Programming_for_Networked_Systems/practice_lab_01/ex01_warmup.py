
user_entry = input("Device and status: ")

cleaned_entry = user_entry.strip().split()

device = cleaned_entry[0].upper()
status = cleaned_entry[1].upper()

print("Device:", device)
print("Status:", status)

if status == "UP":
    print(f"{device} is online")
else:
    print(f"{device} is offline")
