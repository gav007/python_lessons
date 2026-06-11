#count how many times each item appears

subjects = ["Python", "CCNA", "Python", "Linux", "CCNA", "Python"]

subject_counts = {}

for subject in subjects:
    if subject in subject_counts:
        subject_counts[subject] += 1
    else:
        subject_counts[subject] = 1

for subject, count in subject_counts.items():
    print(subject, count)


