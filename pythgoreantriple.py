t = int(input())
for _ in range(t):
    n = int(input())
    aList = list(map(lambda x: x**2, [int(x) for x in input().split()]))
    aList.sort()
    found = False
    for i in range(n - 1):
        if found:
            break
        for j in range(n - 1, 0, -1):
            if aList[i] + aList[j] in aList:
                found = True
                break
    if found:
        print("Yes")
    else:
        print("No")