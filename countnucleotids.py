def count_nucleotide(dna, nucleotide):
    return dna.count(nucleotide)
dna_sequence = input()
nucleotide = input()
print(count_nucleotide(dna_sequence, nucleotide))

