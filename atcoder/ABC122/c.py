import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, Q = map(int, input().split())
    S = input()
    l = [0]*Q
    r = [0]*Q
    for i in range(Q):
        l[i], r[i] = map(int, input().split())

    cs = [0]*(N+1)
    for i in range(N-1):
        if S[i]=='A' and S[i+1]=='C':
            cs[i+2] = cs[i+1] + 1
        else:
            cs[i+2] = cs[i+1]

    for q in range(Q):
        print(cs[r[q]]-cs[l[q]])

if __name__ == '__main__':
    resolve()
