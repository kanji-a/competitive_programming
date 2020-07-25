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
    N = I()
    s = [SS() for _ in range(N)]

    ans = sum([i.count('AB') for i in s])

    # .*AとB.*をいくつくっつけられるか
    # .*AにB.*をくっつけた後、間にB.*Aを挟む方針 挟み方はどうでもいい
    tA = 0
    fB = 0
    fBtA = 0
    for i in s:
        if i[-1] == 'A' and i[0] == 'B':
            fBtA += 1
        elif i[-1] == 'A':
            tA += 1
        elif i[0] == 'B':
            fB += 1

    if tA == fB == 0:
        ans += max(fBtA - 1, 0)
    else:
        ans += min(tA, fB) + fBtA

    print(ans)

if __name__ == '__main__':
    resolve()
