#!/usr/bin/env python3
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
INF = float('inf')
MOD = 10 ** 9 + 7
EPS = 1e-6
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    ab = [LI() for _ in range(N)]
    cd = [LI() for _ in range(N)]

    # 重心の座標が整数になるようにする
    for i in range(N):
        a, b = ab[i]
        ab[i] = [a * N, b * N]
        c, d = cd[i]
        cd[i] = [c * N, d * N]

    # 重心が原点になるように平行移動
    ga = sum(i for i, _ in ab) // N
    gb = sum(i for _, i in ab) // N
    gc = sum(i for i, _ in cd) // N
    gd = sum(i for _, i in cd) // N
    cd_set = set()
    for i in range(N):
        a, b = ab[i]
        ab[i] = [a - ga, b - gb]
        c, d = cd[i]
        cd[i] = [c - gc, d - gd]
    # print(ab)
    # print(cd)

    ans = 'No'
    # Sの最初の点に対して
    a, b = ab[0]
    ll = a ** 2 + b ** 2
    # あるTの点を選んで
    for c, d in cd:
        # print(c, d, ll)
        # 原点からの距離が同じであれば
        if c ** 2 + d ** 2 == ll:
            if ll == 0:
                print('Yes')
                return
            # 回転行列を作成し
            # 全てのSを回転させた点が全てTに入っていればOK
            angle = math.atan2(d, c) - math.atan2(b, a)
            is_ok = True
            for k in range(N):
                aa = math.cos(angle) * ab[k][0] - math.sin(angle) * ab[k][1]
                bb = math.sin(angle) * ab[k][0] + math.cos(angle) * ab[k][1]
                is_aabb_in_cd = False
                for c, d in cd:
                    if abs(c - aa) <= EPS and abs(d - bb) <= EPS:
                        is_aabb_in_cd = True
                if not is_aabb_in_cd:
                    is_ok = False
                    break
            if is_ok:
                ans = 'Yes'
                break

    print(ans)

if __name__ == '__main__':
    resolve()
