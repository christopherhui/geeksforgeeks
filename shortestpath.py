t = int(input())
for i in range(t):
    n = int(input())
    bSF = [0] * (n + 1)
    bSF[1] = 1
    bSF[2] = 2
    for j in range(3, n + 1):
        if j % 3 == 0:
            bSF[j] = bSF[int(j / 3)] + 1
        else:
            bSF[j] = bSF[j - 1] + 1
    print(bSF[n] - 1)
