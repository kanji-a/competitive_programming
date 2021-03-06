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
    N = I()

    # maxの逆演算のため、hが0なものとそうでないものに分類
    xyh_0 = []
    xyh_not0 = []
    for _ in range(N):
        xyh = LI()
        if xyh[2] == 0:
            xyh_0.append(xyh)
        else:
            xyh_not0.append(xyh)

    for cx, cy in itertools.product(range(101), range(101)):
        H = []
        for x, y, h in xyh_not0:
            H.append(h + abs(x - cx) + abs(y - cy))
        # hが0でないものでOKだったら、hが0のもので辻褄が会うかどうか見る
        if len(set(H)) == 1:
            is_ok = True
            for x, y, h in xyh_0:
                if max(H[0] - abs(x - cx) - abs(y - cy), 0) != 0:
                    is_ok = False
            if is_ok:
                ans = (cx, cy, H[0])

    print(*ans)

if __name__ == '__main__':
    resolve()
