print("cow")
print("cat")
print("dog")
print("cow")
print("cat")
print("cow")
data = sorted(set(["cow", "cat", "dog", "cow", "cat", "cow"]))
with open("uniq.txt", "w",
          encoding="utf-8") as f:
    f.write("\n".join(data) +  f"\nВсего уникальных: {len(data)}")


