from intertools import product
alphabet = input()
n = int(input())
for s in product(alphabet, repeat=n):
    print("".join(s))


