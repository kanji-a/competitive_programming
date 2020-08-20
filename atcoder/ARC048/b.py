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
    RH = [LI() for _ in range(N)]

    # レート毎のグーチョキパー人数と累計人数を持っておく
    cnt = [[0] * 3 for _ in range(max([r for r, h in RH]) + 1)]
    for r, h in RH:
        cnt[r][h-1] += 1
    cum = list(itertools.accumulate([sum(i) for i in cnt], initial=0))
    # print(cnt)
    # print(cum)

    for r, h in RH:
        w = cum[r] + cnt[r][h%3]
        l = cum[-1] - cum[r+1] + cnt[r][(h+1)%3]
        d = cnt[r][h-1] - 1
        print(w, l, d)

if __name__ == '__main__':
    resolve()
