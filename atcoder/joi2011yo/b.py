import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    S = input()
    N = int(input())
    R = [input() for _ in range(N)]

    ans = 0
    for i in R:
        if S in i*2:
            ans+=1

    print(ans)

if __name__ == '__main__':
    resolve()
