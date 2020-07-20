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
    T = [LI() for _ in range(N)]

    is_found = [False]

    def dfs(depth, xor):
        if depth == N:
            if xor == 0: 
                is_found[0] = True
        else:
            for i in range(K):
                dfs(depth + 1, xor ^ T[depth][i])

    dfs(0, 0)

    if is_found[0]:
        print('Found')
    else:
        print('Nothing')

if __name__ == '__main__':
    resolve()
