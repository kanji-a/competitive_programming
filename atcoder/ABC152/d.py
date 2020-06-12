N = int(input())

ans = 0
ctable = [[0 for _ in range(10)] for _ in range(10)]

for n in range(1, N+1):
    first = int(str(n)[0])
    last = int(str(n)[-1])
    ctable[first][last] += 1

for i in range(10):
    for j in range(10):
        ans += ctable[i][j] * ctable[j][i]

print(ans)