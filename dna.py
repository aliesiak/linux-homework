#!/usr/bin/env python3
import sys
dna = sys.argv[1].upper()
rev_comp = dna.translate(str.maketrans("ATCG", "TAGC"))[::-1]
rna = dna.replace("T", "U")
start = dna.find("ATG")
print(rev_comp, rna, start,sep=", ")

