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
    n = I()

    # n+1の丸太を買って、それからなるべく多くの丸太を作成する
    # 長さn+1の丸太から1からkまで作れるkを求める
    # 余りは1以上k未満なので使いみちはない
    # n+1 = k(k+1)//2
    k_pre = int((2 * (n + 1)) ** 0.5)
    k = 0
    for i in range(k_pre - 1, k_pre + 2):
        if i * (i + 1) <= 2 * (n + 1):
            k = i
    # print(k_pre, k)
    # r = k * (k + 1) // 2
    ans = n + 1 - k
    print(ans)

if __name__ == '__main__':
    resolve()
