import sys
input = lambda: sys.stdin.readline().rstrip() 
import bisect as bs

def resolve():
    N, M = map(int, input().split())
    P = [int(input()) for _ in range(N)]

    PP = set()
    for j in P+[0]:
        for k in P+[0]:
            if j+k<M:
                PP.add(j+k)

    PP = list(PP)
    PP.sort()

    ans = 0
    for i in PP:
        if i<=M:
            j = bs.bisect_left(PP, M-i)
            if j<len(PP):
                ans = max(i+PP[j-1], ans)

    print(ans)

if __name__ == '__main__':
    resolve()
