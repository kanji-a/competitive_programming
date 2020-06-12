import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    P = int(input())

    print(min(P*A, B+max(0, (P-C)*D)))

if __name__ == '__main__':
    resolve()