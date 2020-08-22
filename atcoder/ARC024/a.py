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
    L, R = LI()
    l = LI()
    r = LI()
    cnt_l = collections.Counter(l)
    cnt_r = collections.Counter(r)

    ans = 0
    for k, v in cnt_l.items():
        ans += min(v, cnt_r[k])

    print(ans)

if __name__ == '__main__':
    resolve()
