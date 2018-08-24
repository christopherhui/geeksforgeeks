t = int(input())
for _ in range(t):
    n = int(input())
    aList = input().split()
    num = len(aList(max))
    aDict = {}
    for i in aList:
        count = 1
        while len(i) < num:
            i = int(i) * 10
            i = str(i)
            count *= 10
        i = int(i)
        aDict[i] = count
    biggestNum = ''
    while len(aDict) > 0:
        maxNum = max(aDict)
        thisNum = str(maxNum / aDict[maxNum])
        biggestNum += thisNum

    if biggestNum == '':
        print(0)
    else:
        print(int(biggestNum))



