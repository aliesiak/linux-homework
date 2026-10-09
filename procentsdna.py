dna = input()
gc_percent = (dna.count("G") + dna.count("C")) / len(dna)* 100
print(f"{gc_percent:.2f}%")

