t = int(input())
for _ in range(t):
    aList = [int(x) for x in input().split()]
    n = aList[0]
    s = aList[1]
    bList = [int(x) for x in input().split()]
    prefixSums = []
    found = False
    for c, val in enumerate(bList, 0):
        prefixSums = list(map(lambda x: x + val, prefixSums))
        prefixSums.append(val)
        if s in prefixSums:
            loc = prefixSums.index(s)
            print(loc + 1, c + 1)
            found = True
            break

    if not found:
        print(-1)

