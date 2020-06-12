import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    R, C = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(R)]

    ans = 0
    for i in range(2**R):
        sum = 0
        for c in range(C):
            front = 0
            for r in range(R):
                if a[r][c] != (i>>r)&1:
                    front += 1
            sum += max(front, R-front)
        ans = max(sum, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
