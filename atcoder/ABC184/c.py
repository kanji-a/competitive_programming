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

# 一手でいけるか
def f(r1, c1, r2, c2):
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        return True

def resolve():
    r1, c1 = LI()
    r2, c2 = LI()

    ans = -1
    if r1 == r2 and c1 == c2:
        ans = 0
    elif f(r1, c1, r2, c2):
        ans = 1
    else:
        # ◇移動の後にX移動するパターン
        is_dia_diag = False
        for i in range(-3, 4):
            for j in range(-3 + abs(i), 4 - abs(i)):
                if f(r1 + i, c1 + j, r2, c2):
                    is_dia_diag = True
        # X移動2回(パリティ同じマスへ行く)も含める
        if is_dia_diag or (r1 + c1) % 2 == (r2 + c2) % 2:
            ans = 2
        else:
            ans = 3
    
    print(ans)

if __name__ == '__main__':
    resolve()
