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
    H, W, M = LI()
    hw = {tuple(LI()) for _ in range(M)}

    cnt_h = collections.Counter([h for h, w in hw])
    cnt_w = collections.Counter([w for h, w in hw])

    max_h = max(cnt_h.values())
    max_w = max(cnt_w.values())
    max_h_k = [k for k, v in cnt_h.items() if v == max_h]
    max_w_k = [k for k, v in cnt_w.items() if v == max_w]

    # 縦横のターゲット数最大の座標に置く
    # そのような座標がターゲット上ならば、縦横ターゲット数から1を引く
    is_on_target = True
    for i, j in itertools.product(max_h_k, max_w_k):
        if (i, j) not in hw:
            is_on_target = False
            break

    if is_on_target:
        ans = max_h + max_w - 1
    else:
        ans = max_h + max_w
    print(ans)

if __name__ == '__main__':
    resolve()
