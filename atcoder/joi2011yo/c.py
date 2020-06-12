import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    K = int(input())
    q = [list(map(int, input().split())) for _ in range(K)]

    for a, b in q:
        d = min(a-1, N-a, b-1, N-b)
        print(d%3+1)

if __name__ == '__main__':
    resolve()
