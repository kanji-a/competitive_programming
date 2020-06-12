import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort(reverse=True)
    print(A)
    print([A[i] for i in range(0, len(A)-1, 2)])
    print(sum([A[i] for i in range(0, len(A)-1, 2)]))

if __name__ == '__main__':
    resolve()
