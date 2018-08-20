t = int(input())
aDict = {}
for i in range(t):
    aDict[int(input())] = 0

currSum = 1
for n in range(2, max(aDict) + 1):
    divisible = False
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        divisible = True

    if not divisible:
        currSum += 1

    if n in aDict:
        aDict[n] = currSum

for a in aDict:
    print(aDict[a])
