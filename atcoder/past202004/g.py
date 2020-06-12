import sys
input = lambda: sys.stdin.readline().rstrip() 
from collections import Counter
import bisect as bs

def resolve():
    Q = int(input())
    Query = [input().split() for _ in range(Q)]

    S = ''
    l = 0
    idx = 0
    # 文字毎に、(累積個数が変わりはじめるindex, 累積個数)を持つ
    # acm = [[0] for _ in range(26)]
    acm = [[(0, 0)] for _ in range(26)]
    for i in Query:
        if i[0]=='1':
            C = i[1]
            X = int(i[2])
            # S += C*X
            l += X
            acm[ord(C)-ord('a')].append((l, acm[ord(C)-ord('a')][-1][1]+X))
        else:
            D = int(i[1])
            idx_new = min(idx+D, l)
            ans = 0
            for j in acm:
                j0 = [k[0] for k in j]
                begin = bs.bisect_left(j0, idx)
                end = bs.bisect_left(j0, idx_new)
                print(j, begin, end)
                # if end<len(j):

                c = j[end][1]-idx_new - j[begin][1] 
                ans += c**2
                # print(ans)

            idx = idx_new

    print(acm)
    print(ans)

if __name__ == '__main__':
    resolve()