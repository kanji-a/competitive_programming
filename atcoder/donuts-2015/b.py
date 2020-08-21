import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, M = LI()
    A = LI()
    B = []
    C = []
    I = []
    for _ in range(M):
        BCI = LI()
        B.append(BCI[0])
        C.append(BCI[1])
        I.append(BCI[2:])

    ans = 0
    for i in itertools.combinations(range(N), 9):
        tmp = sum([A[j] for j in i])
        for k in range(M):
            if len(set(i) & {l - 1 for l in I[k]}) >= 3:
                tmp += B[k]
        ans = max(tmp, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
