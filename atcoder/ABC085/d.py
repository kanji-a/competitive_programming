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
    N, H = LI()
    a = []
    b = []
    for _ in range(N):
        ab = LI()
        a.append(ab[0])
        b.append(ab[1])
    b.sort(reverse=True)
    a_max = max(a)

    # amax以上のbを強い順に投げていく
    # その後amaxを連打 amaxを持つ刀を先に投げていても、後に投げたことにすればよい
    ans = 0
    i = 0
    while i < N and H > 0 and b[i] > a_max:
        H -= b[i]
        i += 1
        ans += 1

    if 0 < H:
        ans += (H - 1) // a_max + 1

    print(ans)

if __name__ == '__main__':
    resolve()
