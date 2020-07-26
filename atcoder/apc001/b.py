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
    a = LI()
    b = LI()

    # 全てのiに対してa[i]<=b[i]にしていく
    tmp = 0
    for i in range(N):
        if a[i] > b[i]:
            tmp += a[i] - b[i]
        else:
            tmp -= (b[i] - a[i]) // 2

    if tmp <= 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    resolve()
