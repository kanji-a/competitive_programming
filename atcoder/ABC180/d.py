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
    X, Y, A, B = LI()

    # カコモンジムは、強さが強さ*(A-1)増えるといえる
    # カコモンジムの強さ増分がACジムを超えるまではカコモンジム
    s = X
    e = 0
    while s * (A - 1) < B:
        if s >= Y:
            break
        s *= A
        e += 1
    e += (Y - 1 - s) // B

    print(e)

if __name__ == '__main__':
    resolve()
