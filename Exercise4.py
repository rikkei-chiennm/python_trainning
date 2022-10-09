data = """
Come to the
River
Of my
Soulful
Sentiments
Meandering silently
Yearning for release.
Hasten
Earnestly
As my love flows by
Rushing through the flood-gates
To your heart.
"""

def convertToTitle(data):
    list = data.split("\n")
    title = []
    for i in list:
        if i != '':
            title.append(i[0])
    return ''.join(title)

print(convertToTitle(data))