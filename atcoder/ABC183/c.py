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
    N, K = LI()
    T = [LI() for _ in range(N)]

    ans = 0
    for i in itertools.permutations(range(1, N)):
        tmp = sum([T[i[j]][i[j+1]] for j in range(N - 2)])
        if tmp + T[0][i[0]] + T[i[-1]][0] == K:
            ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
