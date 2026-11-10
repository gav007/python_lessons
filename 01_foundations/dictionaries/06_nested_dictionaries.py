# Store more than one piece of information per subject.

# Nested Dictionary

subject_data = {
    "Python": {
        "minutes": 100,
        "confidence": 3
    },
    "CCNA": {
        "minutes": 75,
        "confidence": 2
    },
    "Linux": {
        "minutes": 40,
        "confidence": 3
    }
}

# Print Python Minutes

#print("Python minutes:", subject_data["Python"]["minutes"])

# Print CCNA Minutes

#print("CCNA minutes:", subject_data["CCNA"]["minutes"])

print("-"*60)
for subject, details in subject_data.items():
    print("SUBJECT", subject)
    print("MINUTES", details["minutes"])
    print("CONFIDENCE", details["confidence"])
    print("-"*60)
    
print("UPDATED")
# update python
subject_data["Python"]["minutes"] += 20

# update CCNA
subject_data["CCNA"]["minutes"]+= 30

for subject, data in subject_data.items():
    print("SUBJECT:", subject)
    print("MINUTES:", data["minutes"])
    print("CONFIDENCE:", data["confidence"])
    print("-"*60)
