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

    def f(x):
        return sum([int(i) for i in str(x)])

    ans = []
    l = 9 * len(str(N))
    for i in range(l + 1):
        x = N - l + i
        if x > 0 and x + f(x) == N:
            ans.append(x)

    print(len(ans))
    for i in ans:
        print(i)

if __name__ == '__main__':
    resolve()
