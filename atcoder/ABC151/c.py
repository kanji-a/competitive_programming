N, M = map(int, input().split())
pS = [input().split() for _ in range(M)]

p = [int(i[0]) for i in pS]
S = [i[1] for i in pS]

aced = [False for _ in range(N)]
penalty = [0 for _ in range(N)]
# pena = 0

for i in range(M):
    if not aced[int(pS[i][0])-1]:
        if pS[i][1] == 'WA':
            penalty[int(pS[i][0])-1] += 1
            # pena += 1
        if pS[i][1] == 'AC':
            aced[int(pS[i][0])-1] = True

# print(aced.count(True), pena)
penaltyCount = 0
for i in range(N):
    if aced[i]:
        penaltyCount += penalty[i]

print(aced.count(True), penaltyCount)
