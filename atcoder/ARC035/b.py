import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10 ** 9 + 7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    T = [I() for _ in range(N)]
    
    T.sort()
    time = 0
    T_cum = [0] * (N + 1)
    for i in range(N):
        T_cum[i+1] = T_cum[i] + T[i]
    time = sum(T_cum)
    print(time)

    cnt = collections.Counter(T)
    num = 1
    for i in cnt.values():
        tmp = 1
        for j in range(i):
            tmp *= j + 1
            tmp %= MOD
        num *= tmp
        num %= MOD
    print(num)

if __name__ == '__main__':
    resolve()
