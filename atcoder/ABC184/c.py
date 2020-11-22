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
    r1, c1 = LI()
    r2, c2 = LI()

    ans = -1
    if r1 == r2 and c1 == c2:
        ans = 0
    elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        ans = 1
    # 斜め移動2回か、斜め移動後に四角に入るか
    elif (r1 + c1) % 2 == (r2 + c2) % 2 or abs((c1 - r1) - abs(c2 - r2)) <= 3 or abs((c1 + r1) - (c2 + r2)) <= 3:
        ans = 2
    else:
        ans = 3
    
    print(ans)

if __name__ == '__main__':
    resolve()
