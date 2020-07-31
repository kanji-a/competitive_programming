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
    N, R = LI()
    S = list(SS())

    # 逆から考える 射程の一番遠くに塗られてないマスが来るように塗っていく
    # 移動
    ans = 0
    for i in range(N):
        if S[N-1-i] == '.':
            ans = max(N - R - i, 0)
            break

    # 塗り
    for i in range(N):
        j = N - 1 - i
        if S[j] == '.':
            for r in range(R):
                if j - r >= 0:
                    S[j-r] = 'o'
            ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
