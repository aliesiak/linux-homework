def is_valid_dna(dna):
    if not dna:
        return False
    valid_nucleotids = {"A", "T", "G", "C"}
    return all(nucleotide in valid_nucleotids for nucleotide in dna)
def hamming_distance(s1, s2):
    if not is_valid_dna(s1) or not is_valid_dna(s2):
        return None
    if len(s1) != len(s2):
        return None
    distance = 0
    for n1, n2 in zip(s1, s2):
        if n1 !=n2:
            distance += 1
    return distance
sequence_1 = input().upper()
sequence_2 = input().upper()
result = hamming_distance(sequence_1, sequence_2)
print(f"Расстояние Хэмминга: {result}")

