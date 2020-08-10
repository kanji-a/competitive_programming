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
    A, B = LI()

    # 実験した結果
    def f(x):
        rem = x % 4
        if rem == 0:
            return x
        elif rem == 1:
            return 1
        elif rem == 2:
            return x + 1
        elif rem == 3:
            return 0

    ans = f(B) ^ f(A - 1)
    print(ans)

if __name__ == '__main__':
    resolve()
