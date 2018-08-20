t = int(input())
aList = []
for i in range(t):
    aList.append(int(input()))

bList = [0] * (max(aList) + 1)
bList[0] = 0
bList[1] = 1
for i in range(2, len(bList)):
    bList[i] = bList[i - 1] + bList[i - 2]

for j in aList:
    print(bList[j])
print(bList)
