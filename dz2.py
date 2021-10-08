def thesaurus(*names):
    word1 = set()
    word2 = {}
    for i in range(0,len(names)):
        word1.add (names[i][0])
    print(word1)
    for word in word1:
        a = []
        for name in names:
            if word == name[0]:
                a.append(name)
            word2[word] = a
    return word2

name = ["Иван", "Мария", "Петр", "Илья", ]
print(thesaurus(*name))

