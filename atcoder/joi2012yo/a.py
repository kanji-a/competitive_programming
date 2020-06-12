import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    P = [int(input()) for _ in range(3)]
    J = [int(input()) for _ in range(2)]

    print(min(P)+min(J)-50)

if __name__ == '__main__':
    resolve()