def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))
sequences = [
        "AACG",
        "AATG",
        "TATG",
        "TTTG"
    ]
for s1 in sequences:
    row = [str(hamming_distance(s1, s2)) for s2 in sequences]
    print(" ".join(row))

