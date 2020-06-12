import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    ans = [0]*N
    for i in A:
        ans[i-1] += 1

    for i in ans:
        print(i)

if __name__ == '__main__':
    resolve()
