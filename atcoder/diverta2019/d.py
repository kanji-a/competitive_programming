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

    ans = 0
    # N//m=N%m=i => N=m*i, i<m => i<N**0.5
    for i in range(1, int(N ** 0.5) + 1):
        # N//m = N%m = i <=> (N-i)//i = m
        if (N - i) % i == 0:
            m = (N - i) // i
            ## 誤差のため、i==mはループで除外しきれない
            if i < m:
                ans += m

    print(ans)

if __name__ == '__main__':
    resolve()
