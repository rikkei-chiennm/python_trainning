import random

def createRandomList(n) :
    list = []
    for i in range(0, n):
        list.append(random.randrange(1, 9))

    return list

while(True):
    value = input()
    try:
        n = int(input())
    except ValueError:
        continue
    break

newList = createRandomList(n)

print(newList)