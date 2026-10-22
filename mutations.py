reference = input().strip()
sample = input().strip()
if len(reference) != len(sample):
    print("Ошибка")
else: 
    print("\nНайденные мутации:")
    for i, ref_nuc in enumerate(reference):
        samp_nuc = sample[i]
        if ref_nuc != samp_nuc:
            print(f"{i + 1}: {ref_nuc} > {samp_nuc}")

