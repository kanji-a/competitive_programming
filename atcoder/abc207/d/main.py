#!/usr/bin/env python3
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
INF = float('inf')
MOD = 10 ** 9 + 7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    # 全部の座標を足した点の位置が合うように平行移動
    N = I()
    ab = [LI() for _ in range(N)]
    cd = [LI() for _ in range(N)]
    for i in range(N):
        a, b = ab[i]
        ab[i] = [a * N, b * N]
        c, d = cd[i]
        cd[i] = [c * N, d * N]

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
        cd_set.add((c - gc, d - gd))
    # print(ab)
    # print(cd_set)

    # for i in range(N):
    #     print(ab[i])
    # for i in range(N):
    #     print(cd[i])

    ans = 'No'

    # 全てのSの点に対して
    for i in range(N):
        a, b = ab[i]
        # あるTの点を選んで
        for j in range(N):
            # print('ij', i, j)
            c, d = cd[j]
            # 原点からの距離が同じであれば
            if a ** 2 + b ** 2 == c ** 2 + d ** 2:
                ll = a ** 2 + b ** 2
                if ll == 0:
                    ans = 'Yes'
                    break
                # 回転行列を作成し
                # 全てのSを回転させた点が全てTに入っていればOK
                # is_ok = True
                aabb_set = set()
                cos_ll = a * c + b * d
                # sin_ll = int((ll ** 2 - cos_ll ** 2) ** 0.5)
                sin_ll = math.isqrt(ll ** 2 - cos_ll ** 2)
                for k in range(N):
                    aa = (cos_ll * ab[k][0] - sin_ll * ab[k][1]) // ll
                    bb = (sin_ll * ab[k][0] + cos_ll * ab[k][1]) // ll
                    aabb_set.add((aa, bb))
                    # if (aa, bb) not in cd_set:
                    #     is_ok = False
                    #     break
                # if is_ok:
                # print('aabb', aabb_set)
                if aabb_set == cd_set:
                    ans = 'Yes'

    print(ans)

if __name__ == '__main__':
    resolve()
