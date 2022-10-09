result = []

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a + (b / c) == 10:
                entry = [a, b, c]
                result.append(entry)

print(result)
