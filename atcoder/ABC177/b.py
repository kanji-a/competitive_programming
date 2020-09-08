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
    S = SS()
    T = SS()
    len_S = len(S)
    len_T = len(T)

    ans = len(T)
    for i in range(len_S - len_T + 1):
        diff = len([(j, k) for j, k in zip(S[i:i+len_T], T) if j != k])
        ans = min(diff, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
