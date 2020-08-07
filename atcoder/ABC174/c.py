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
    K = I()

    rem = 7 % K
    ans = 0
    is_ok = True
    seen = [False] * K
    while rem != 0:
        if seen[rem]:
            is_ok = False
            break
        seen[rem] = True
        rem = rem * 10 + 7
        rem %= K
        ans += 1

    if is_ok:
        print(ans + 1)
    else:
        print(-1)

if __name__ == '__main__':
    resolve()
