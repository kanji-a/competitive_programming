import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    A, B, C, X, Y = map(int, input().split())

    ans = 0
    if A+B > 2*C:
        ans = 2*C*min(X, Y)+min((A if X>Y else B)*abs(X-Y), 2*C*abs(X-Y))
    else:
        ans = A*X+B*Y
    
    print(ans)

if __name__ == '__main__':
    resolve()
