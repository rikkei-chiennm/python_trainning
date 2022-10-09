n = int(input("N = "))

def resolve(n):
    binary = "{0:b}".format(n)
    i = 1
    result = []
    while(i <= len(binary)):
        if binary[-i] == '1':
            result.append(binary[-i:])
            break
        i+=1

    return ''.join(result)

print(resolve(n))