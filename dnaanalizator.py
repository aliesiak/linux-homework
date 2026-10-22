lengths = []
while True:
    dna = input().strip()
    if dna == "STOP":
        break
    is_valid = True
    for char in dna:
        if char not in "ATGC":
            is_valid = False
            break
        if is_valid:
            lengths.append(len(dna))
        else:
            print("неверно")
print(len(lengths))
print(lengths)

