t = int(input())
for _ in range(t):
    n = int(input())
    aList = input().split()
    if len(aList) == 1:
        print(aList[0])
    else:
        for z in range(0, len(aList)):
            for i in range(0, len(aList) - 1):
                firstNum = int(aList[i] + aList[i + 1])
                secondNum = int(aList[i + 1] + aList[i])
                if firstNum > secondNum:
                    temp = aList[i]
                    aList[i] = aList[i + 1]
                    aList[i + 1] = temp

    str = ''
    for j in range(len(aList) - 1, -1, -1):
        str += aList[j]
    print(int(str))
