t = int(input())
for _ in range(t):
    n = int(input())
    aList = input().split()
    createNum = ''
    if len(aList) == 1:
        print(aList[0])
    else:
        firstNum = int(aList[0] + aList[1])
        secondNum = int(aList[1] + aList[0])
        if firstNum > secondNum:
            createNum += str(firstNum)
        else:
            createNum += str(secondNum)
        for i in range(2, len(aList)):
            firstNum = int(createNum + aList[i])
            secondNum = int(aList[i] + createNum)
            if firstNum > secondNum:
                createNum = str(firstNum)
            else:
                createNum = str(secondNum)
    print(int(createNum))


