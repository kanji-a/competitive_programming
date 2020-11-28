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
    a, b, x, y = LI()

    # 最低xかかる
    # bのが下であれば、階移動を1階節約できる
    # 階移動にx2階かy一回か短い方を選ぶ
    if a == b:
        print(x)
    elif a < b:
        print(x + (b - a) * min(2 * x, y))
    else:
        print(x + (a - b - 1) * min(2 * x, y))

if __name__ == '__main__':
    resolve()
