def createEvenList(n):
    list = []
    for i in range(0, n):
        if i % 2 == 0:
            list.append(i)
    return list


n = int(input("N = "))

newList = createEvenList(n)

print(newList)
