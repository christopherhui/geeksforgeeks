aList = [0] * 10001
aList[0] = aList[1] = aList[2] = 1
aList[3] = 2
for i in range(4, 10001):
   aList[i] = aList[i - 1] + aList[i - 3] + aList[i - 4]

for _ in range(t):
    print(aList[int(input())] % (10 ** 9 + 7))