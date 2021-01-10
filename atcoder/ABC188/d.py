import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, C = LI()
    abc = [LI() for _ in range(N)]
    # print(abc)
    ab = set()
    for a, b, _ in abc:
        ab.add(a - 1)
        ab.add(b)
    ab = list(ab)
    ab.sort()
    d = {e: i for i, e in enumerate(ab)}
    # print(d)
    imos = [0] * (len(d) + 1)
    for i in abc:
        a, b, c = i
        imos[d[a-1]] += c
        imos[d[b]] -= c
    # print(imos)
    acm = list(itertools.accumulate(imos))
    # print(acm)
    d_keys = sorted(d.keys())
    d_keys.append(d_keys[-1] + 1)
    # print(d_keys)
    ans = sum([min(acm[i], C) * (d_keys[i+1] - d_keys[i]) for i in range(len(acm) - 1)])
    print(ans)

if __name__ == '__main__':
    resolve()
