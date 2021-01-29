import sys, collections, heapq
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N, Q = LI()
    # 幼児のレート
    A = []
    # 幼児の所属
    B = []

    # 幼稚園ごとにheapqで管理 レートは-1倍して格納
    kg = collections.defaultdict(list)
    for i in range(N):
        AB = LI()
        A.append(AB[0])
        B.append(AB[1])
        heapq.heappush(kg[AB[1]], (-AB[0], i))
    # 転園した幼児一覧
    del_kg = collections.defaultdict(set)
    # 園内最強から外れた幼児一覧
    del_strongest = set()

    # 幼稚園の最強幼児をheapqで管理 レートはそのままの値で格納
    strongest = []
    for i in kg.values():
        heapq.heappush(strongest, (-i[0][0], i[0][1]))

    for _ in range(Q):
        C, D = LI()
        C -= 1
        # 所属情報変更
        source = B[C]
        B[C] = D
        # 転園元
        del_kg[source].add(C)
        # 最強幼児が抜ける場合
        if kg[source] and C == kg[source][0][1]:
            # 抜けた最強幼児を各園最強一覧から削除
            del_strongest.add(C)
            # heapqのトップは削除されていないものになるようにしておく
            while kg[source] and kg[source][0][1] in del_kg[source]:
                heapq.heappop(kg[source])
            # 園の二番手がいる場合
            if kg[source]:
                tmp = kg[source][0]
                # 各園最強一覧に追加
                heapq.heappush(strongest, (-tmp[0], tmp[1]))
                del_strongest.discard(tmp[1])

        # 転園先
        # 最強幼児が更新される場合
        if kg[D] and A[C] > -kg[D][0][0]:
            # 元最強幼児を各園最強一覧から削除
            del_strongest.add(kg[D][0][1])
        # 最強幼児が更新されるか転園先に幼児がいない場合
        if kg[D] and A[C] > -kg[D][0][0] or not kg[D]:
            # 新しい最強幼児を各園最強一覧に追加
            heapq.heappush(strongest, (A[C], C))
            del_strongest.discard(C)

        # 転園先に追加
        heapq.heappush(kg[D], (-A[C], C))
        del_kg[D].discard(C)
        # heapqのトップは削除されていないものになるようにしておく
        while strongest and strongest[0][1] in del_strongest:
            heapq.heappop(strongest)

        # print(kg)
        # print(del_kg)
        # print(strongest)
        # print(del_strongest)
        print(strongest[0][0])

if __name__ == '__main__':
    resolve()
