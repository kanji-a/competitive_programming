import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, K = map(int, input().split())

    print(min(N%K, K-N%K)) 

if __name__ == '__main__':
    resolve()
