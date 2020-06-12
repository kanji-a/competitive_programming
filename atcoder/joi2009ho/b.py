import sys
input = lambda: sys.stdin.readline().rstrip() 
import bisect as bs

def resolve():
    d = int(input())
    n = int(input())
    m = int(input())
    ds = [0]
    for _ in range(n-1):
        ds.append(int(input()))
    k = [int(input()) for _ in range(m)]

    ds.sort()
    ans = 0
    for i in k:
        idx = bs.bisect_left(ds, i)
        left = ds[(idx-1)%n]
        right = ds[idx%n]
        ans += min((i-left)%d, (right-i)%d)

    print(ans)

if __name__ == '__main__':
    resolve()
