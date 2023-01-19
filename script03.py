import names

nameList = []
for i in range(5):
    nameList.append(names.get_full_name())


def nameLen(nameList):
    for i in range(len(nameList)):
        print(nameList[i], int(len(nameList[i]))-nameList[i].count(' '))

nameLen(nameList)
