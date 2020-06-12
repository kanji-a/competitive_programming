import sys
input = lambda: sys.stdin.readline().rstrip() 
import bisect

def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort()
    C.sort()

    ans = 0
    for b in B:
        a_r = bisect.bisect_left(A, b)
        c_l = bisect.bisect_right(C, b)
        ans += a_r * (N - c_l)

    print(ans)

if __name__ == '__main__':
    resolve()
