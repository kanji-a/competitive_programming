import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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
    K = []
    T = []
    # 消費期限→棚番号
    d = {}
    # 棚番号→2番目の商品の消費期限
    second = [0] * N
    for i in range(N):
        KT = LI()
        K.append(KT[0])
        tmp = KT[1:]
        T.append(collections.deque(tmp))
        for j in tmp:
            d[j] = i
        if len(tmp) >= 2:
            second[i] = tmp[1]
    M = I()
    a = LI()
    # 1,2番目の商品をそれぞれheapqで管理
    hq = [[] for _ in range(2)]
    for i in range(N):
        for j in range(2):
            if T[i]:
                heapq.heappush(hq[j], -T[i].popleft())
    # 2番目の商品だったが現在は違うもの
    # 1番目が売れて2番目の商品が減るとき、heapqから直接取り除けないので集合として管理する
    removed = set()

    for i in a:
        # print(hq, second, removed)
        # 2番目の商品一覧の頭を削除されていないものにする
        while hq[1] and -hq[1][0] in removed:
            heapq.heappop(hq[1])
        if i == 1 or i == 2 and hq[0] and (hq[1] and hq[0][0] < hq[1][0] or not hq[1]):
            # 1番目の棚から買った場合
            # 1番目の商品一覧から削除
            m = -heapq.heappop(hq[0])
            print(m)
            shelf = d[m]
            next_top = second[shelf]
            if next_top == 0:
                continue
            # 2番目の商品一覧から削除
            removed.add(next_top)
            # 1番目の商品一覧に追加
            heapq.heappush(hq[0], -next_top)
            # 3番目以降→2番目の商品一覧
            if T[shelf]:
                second[shelf] = T[shelf].popleft()
                heapq.heappush(hq[1], -second[shelf])
            else:
                second[shelf] = 0
        else:
            # 2番目の棚から買った場合
            # 2番目の商品一覧から削除
            m = -heapq.heappop(hq[1])
            print(m)
            shelf = d[m]
            # 3番目以降→2番目の商品一覧
            if T[shelf]:
                second[shelf] = T[shelf].popleft()
                heapq.heappush(hq[1], -second[shelf])
            else:
                second[shelf] = 0

if __name__ == '__main__':
    resolve()
