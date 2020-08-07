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
    A = LI()

    cnt = collections.Counter(A)
    edge = [k for k, v in cnt.items() if v >= 2]
    edge.sort(reverse=True)


    if len(edge) >= 1 and cnt[edge[0]] >= 4:
        ans = edge[0] ** 2
    elif len(edge) >= 2:
        ans = edge[0] * edge[1]
    else:
        ans = 0

    print(ans)

if __name__ == '__main__':
    resolve()
