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
    A = []
    B = []
    for i in range(N):
        AB = LI()
        A.append(AB[0])
        B.append(AB[1] - 1)

    def get_strongest_infant(gid):
        hq = g[gid]
        while hq:
            rate, id = hq[0]
            if B[id] != gid:
                heapq.heappop(g[gid])
            else:
                return -rate
        return 0

    def get_equality():
        while strongest:
            rate, gid = strongest[0]
            # 園の最高レートが最新情報と合致していれば出力
            if get_strongest_infant(gid) == rate:
                return rate
            else:
                heapq.heappop(strongest)

    # 幼稚園iの園児 (-rate, id) を入れたheapq
    g = [[] for _ in range(2 * 10 ** 5)]
    for i in range(N):
        heapq.heappush(g[B[i]], (-A[i], i))

    # 園ごとの最高レートを持つheapq
    strongest = []
    for i in range(N):
        rate = get_strongest_infant(i)
        if rate:
            heapq.heappush(strongest, (A[i], i))

    for i in range(Q):
        C, D = LI_()

        gid_before = B[C]
        B[C] = D
        # 転園先に園児追加 転園元からは削除しない
        heapq.heappush(g[D], (-A[C], C))
        for i in (gid_before, D):
            rate = get_strongest_infant(i)
            if rate:
                heapq.heappush(strongest, (rate, i))
        print(get_equality())


if __name__ == '__main__':
    resolve()
