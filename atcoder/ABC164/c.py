import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    S = tuple(input() for _ in range(N))

    print(len(set(S)))

if __name__ == '__main__':
    resolve()
