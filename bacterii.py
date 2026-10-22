growth = [
        [0, 2, 4, 8],
        [0, 1, 1, 2],
        [0, 3, 6, 9]
]
threshold = 5
for culture in growth:
    found = False
    for index, value in enumerate(culture):
        if value >= threshold:
            print(index)
            found = True
            break
        if not found:
            print("отсутствует")

