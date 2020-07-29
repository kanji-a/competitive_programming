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
    x = I()

    # 5を上にして、6と5を交互に出す
    ans = 0
    ans += x // 11 * 2
    x %= 11
    if x == 0:
        print(ans)
    elif 0 < x <= 6:
        print(ans + 1)
    else:
        print(ans + 2)

if __name__ == '__main__':
    resolve()
