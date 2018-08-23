def permutation(swapped, stringbuilder):
    if swapped == len(string):
        print(stringbuilder, end=' ')
    else:
        for i in string:
            if i not in stringbuilder:
                permutation(swapped + 1, stringbuilder + i)


t = int(input())
for _ in range(t):
    swapped = 0
    string = input()
    stringbuilder = ''
    permutation(swapped, stringbuilder)
    print()
