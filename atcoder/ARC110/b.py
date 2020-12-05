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
    N = I()
    T = SS()

    ans = 0
    idx_zero = []
    for i in range(N):
        if T[i] == '0':
            idx_zero.append(i)
    len_idx_zero = len(idx_zero)
    # print(idx_zero)

    # 0がある場合
    if idx_zero:
        # 0の間隔が全て2であり、最初の0までと最後の0からの1が2個以下であれば1個以上ある
        first_ones = idx_zero[0]
        last_ones = N - idx_zero[-1] - 1
        # print(first_ones, last_ones)
        if [idx_zero[j+1] - idx_zero[j] for j in range(len_idx_zero - 1)].count(3) == len_idx_zero - 1 and first_ones <= 2 and last_ones <= 2:
            ans = 10 ** 10 - len_idx_zero + 1
            if last_ones >= 1:
                ans -= 1
    else:
        if T == '1':
            ans = 10 ** 10 * 2
        elif T == '11':
            ans = 10 ** 10

    print(ans)

if __name__ == '__main__':
    resolve()
