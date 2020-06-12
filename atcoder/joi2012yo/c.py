import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    A, B = map(int, input().split())
    C = int(input())
    D = [int(input()) for _ in range(N)]

    D.sort(reverse=True)
    val = [0]*(N+1)
    for i in range(N+1):
        cal = C+sum(D[:i])
        price = A + B * i
        val.append(cal//price)
    print(max(val))

if __name__ == '__main__':
    resolve()
