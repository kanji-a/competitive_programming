import bisect, collections, copy, heapq, itertools, math, string, sys
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
    A, B, C, D, E, F = LI()

    # 水と砂糖の用意できるパターンを列挙
    w = set()
    for i in range(F // (100 * A) + 1):
        for j in range((F - i * 100 * A) // (100 * B) + 1):
            if i != 0 and i != 0:
                w.add(i * A + j * B)
    # print(w)

    s = set()
    for i in range(F // C + 1):
        for j in range((F - i * C) // D + 1):
            s.add(i * C + j * D)
    # print(s)

    # 全探索で間にあう(2分探索不要)
    # 初期値として水100Aの0%砂糖水を設定
    ans = [A, 0]
    for i, j in itertools.product(w, s):
        if 100 * i + j <= F and j <= i * E:
            # 100j/(100i+j) > 100ans[1]/(100ans[0]+ans[1])
            if j * (100 * ans[0] + ans[1]) > ans[1] * (100 * i + j):
                ans[0] = i
                ans[1] = j

    print(ans[0] * 100 + ans[1], ans[1])

if __name__ == '__main__':
    resolve()
