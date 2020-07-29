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
    N, K = LI()
    A = [I() for _ in range(N)]
    up = []
    cnt = 0
    for i in range(N - 1):
        if A[i] < A[i+1]:
            cnt += 1
        else:
            up.append(cnt)
            cnt = 0
    up.append(cnt)

    ans = 0
    for i in up:
        if i + 1 >= K:
            ans += i + 2 - K

    print(ans)

if __name__ == '__main__':
    resolve()
