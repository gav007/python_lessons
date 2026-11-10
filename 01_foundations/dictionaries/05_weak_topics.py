# parse dictionary data where confidence is <= 2

topic_confidence = {
    "CSV files": 2,
    "OOP classes": 3,
    "STP": 2,
    "VLANs": 4,
    "File handling": 3,
    "Dictionaries": 1
}

for topic, confidence in topic_confidence.items():
    if confidence <= 2:
        print(topic, confidence)


