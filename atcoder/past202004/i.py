import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    ans = [0]*2**N
    round = 1
    rest = range(2**N)
    for i in range(N):
        new_rest = []
        if i==N-1:
            ans[rest[0]] = ans[rest[1]] = round
        else:
            for j in range(0, 2**(N-i), 2):
                if A[rest[j]] < A[rest[j+1]]:
                    ans[rest[j]] = round
                    new_rest.append(rest[j+1])
                else:
                    ans[rest[j+1]] = round
                    new_rest.append(rest[j])
            rest = new_rest
        round += 1

    for i in ans:
        print(i)

if __name__ == '__main__':
    resolve()
