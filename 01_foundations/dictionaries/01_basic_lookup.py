# dictionary practice 01
# goal: practice looking up values by key

student_confidence = {
        "Python": 3,
        "CCNA": 4,
        "Linux": 2
        
        }

print(student_confidence["Python"])
print(student_confidence["Linux"])

if "Java" in student_confidence:
    print("Java Exists")

else:
    print("Java does not exist")


