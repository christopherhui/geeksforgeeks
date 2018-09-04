t = int(input())
for _ in range(t):
    aList = [int(x) for x in input().split()]
    bList = input().split()
    visited = {}
    count = 0
    for x, i in enumerate(bList, 0):

        for y, let in enumerate(i, 0):
            if let == 'X' and (x, y) not in visited:
                queue = [(x, y)]
                visited[(x, y)] = 1

                while queue:
                    cord = queue.pop()
                    cList = []
                    x, y = cord[0], cord[1]
                    if x + 1 <= aList[1]:
                        cList.append(x + 1, y)
                    if y + 1 <= aList[0]:
                        cList.append(x, y + 1)
                    for newCord in cList:
                        if bList[newCord[0]][newCord[1]] == 'X':
                            queue.append(newCord)
                            visited[newCord] = 1

                count += 1

    print(count)

