import bisect, collections, copy, heapq, itertools, math, string, sys
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
    N, M, T = LI()
    AB = [LI() for _ in range(M)]

    ans = 'Yes'
    b = N

    for i in range(M):
        A, B = AB[i]
        if i == 0:
            B_p = 0
        else:
            B_p = AB[i-1][1]

        b -= A - B_p
        # print(b)
        if b <= 0:
            ans = 'No'
            break
        else:
            b = min(b + B - A, N)
        # print(b)

    b -= T - AB[-1][1]
    # print(b)
    if b <= 0:
        ans = 'No'

    print(ans)

if __name__ == '__main__':
    resolve()
