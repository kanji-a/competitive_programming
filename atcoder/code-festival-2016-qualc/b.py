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
    K, T = LI()
    a = LI()

    # aを2グループに分けて交互に食べれば良い
    # 最も差の少ない2グループの分け方を知りたい

    a.sort(reverse=True)
    a_cum = [0] * (T + 1)
    for i in range(T):
        a_cum[i+1] = a_cum[i] + a[i]

    ans = INF
    for i in a_cum:
        ans = min(max(abs(2 * i - K) - 1, 0), ans)

    print(ans)

if __name__ == '__main__':
    resolve()
