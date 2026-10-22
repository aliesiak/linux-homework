reads = ["ATGCC", "GCCAA", "CAAAT", "TTTGG"]
k = 3
for i in range(len(reads)):
    for j in range(len(reads)):
        if i != j:
            prefix = reads[j][:k]
            if reads[i].endswith(prefix):
                print(f"{i + 1} - {j + 1}")

