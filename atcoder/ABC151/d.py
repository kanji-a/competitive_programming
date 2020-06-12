from collections import deque
import itertools
import copy

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

def solve(s):
    d = ((1, 0), (-1, 0), (0, -1), (0, 1))
    queue = deque([s])
    steps = [[-1 for _ in range(W)] for _ in range(H)]
    steps[s[0]][s[1]] = 0

    while len(queue) > 0:
        current = queue.popleft()
        cy = current[0]
        cx = current[1]
        for i in d:
            ny = cy+i[0]
            nx = cx+i[1]
            # はみ出さないかつ通路であるかつ通ってない
            if (0<=ny<H and 0<=nx<W) and S[ny][nx]=='.' and steps[ny][nx] < 0:
                queue.append([ny, nx])
                steps[ny][nx] = steps[cy][cx] + 1
        
    return max([max(i) for i in steps])

maxStep = 0
for s in itertools.product(range(H), range(W)):
    if S[s[0]][s[1]] == '.':
        maxStep = max(solve([s[0], s[1]]), maxStep)

print(maxStep)