term1 = {"math": 3, "literature": 5, "biology": 2}
term2 = {"math": 7, "literature": 9, "chemistry": 8, "english": 6}


def getListKeywords(d:dict):
    return d.keys()

def resolve(term1:dict, term2:dict):
    result = {}
    listKeywords = []
    term1Keywords = getListKeywords(term1)
    term2Keywords = getListKeywords(term2)

    for kw in term1Keywords:
        listKeywords.append(kw)

    for kw in term2Keywords:
        if kw not in term1.keys():
            listKeywords.append(kw)

    for kw in listKeywords:
        if kw not in term2Keywords:
            result.update({kw:term1[kw]})
        elif kw not in term1Keywords:
            result.update({kw:term2[kw]})
        else:
            avgResult = (int(term1[kw]) + int(term2[kw])) / 2
            result.update({kw:avgResult})

    return result

print(resolve(term1,term2))