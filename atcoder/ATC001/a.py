H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]

s = [0, 0]
g = [0, 0]

for i in range(H):
    for j in range(W):
        if c[i][j] == 's':
            s = [i, j]
        if c[i][j] == 'g':
            g = [i, j]

d = [[1, 0], [-1, 0], [0, -1], [0, 1]]
stack = [s]
can = 'No'

while len(stack) > 0:
    current = stack.pop()
    cy = current[0]
    cx = current[1]
    if c[cy][cx] == 'g':
        can = 'Yes'
    else:
        c[cy][cx] = '#'
        for i in d:
            next = [cy+i[0], cx+i[1]]
            # はみ出さないかつ通ってない
            if (0<=next[0]<H and 0<=next[1]<W) and c[next[0]][next[1]]!='#':
                stack.append(next)

print(can)