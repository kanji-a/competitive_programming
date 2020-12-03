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
    s = SS()
    t = SS()
    len_s = len(s)

    d = collections.defaultdict(list)
    for i in range(len_s):
        d[s[i]].append(i)
    d_keys = d.keys()
    # print(d)

    if [i in d_keys for i in t].count(False) > 0:
        print(-1)
    else:
        offset = -1
        track = 0
        for i in t:
            l = d[i]
            # offsetより大きい最小のiのインデックスを求める
            idx = bisect.bisect_right(l, offset)
            # その週のsに文字が無ければ次の週に行く
            if idx == len(l):
                track += 1
                offset = l[0]
            else:
                offset = l[idx]
            # print(l, offset, track, idx)

        ans = track * len_s + offset + 1
        print(ans)

if __name__ == '__main__':
    resolve()
