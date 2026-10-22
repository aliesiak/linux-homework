rna = input()
stop_codons = ["UAA", "UAG", "UGA"]
coding_count = 0
found_stop_codon = ""
for i in range(0, len(rna), 3):
    codon = rna[i:i+3]
    if len(codon) < 3:
        break
    if codon in stop_codons:
        found_stop_codon = codon
        break
    else:
        coding_count += 1
print (f"Количество кодирующих кодонов:{coding_count}")
print(f"Стоп-кодон: {found_stop_codon}")

