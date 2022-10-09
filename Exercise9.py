import socket

def getHostName():
    return socket.gethostname()

def getLocalIP(hostname):
    return socket.gethostbyname(hostname)

def toBinary(number):
    return "{0:b}".format(number)

def resolve():
    hostname = getHostName()
    localIP = getLocalIP(hostname)
    localIPEntries = localIP.split(".")
    localIPEntriesInBinary = []
    result = "{}.{}.{}.{}"

    for entry in localIPEntries:
        localIPEntriesInBinary.append(toBinary(int(entry)))

    return result.format(
        localIPEntriesInBinary[0],
        localIPEntriesInBinary[1],
        localIPEntriesInBinary[2],
        localIPEntriesInBinary[3]
    )

print(resolve())

