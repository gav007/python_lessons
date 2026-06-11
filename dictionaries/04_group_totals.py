
# List of lists
study_sessions = [
    ["Python", 30],
    ["CCNA", 40],
    ["Python", 25],
    ["CCNA", 35],
    ["Linux", 20]
]

minutes_by_subject = {}

for subject_time in study_sessions:
    subject = subject_time[0]
    time = subject_time[1]

    if subject in minutes_by_subject:
        minutes_by_subject[subject] += time

    else:
        minutes_by_subject[subject] = time

for subject, time in minutes_by_subject.items():
    print(subject, time)


