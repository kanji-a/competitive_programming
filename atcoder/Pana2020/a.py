import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    K = int(input())
    A = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]
    print(A[K-1])

if __name__ == '__main__':
    resolve()