import sys
input = lambda: sys.stdin.readline().rstrip() 
import bisect as bs

def resolve():
    N = int(input())
    S = input()

    R = []
    G = []
    B = []
    for i in range(N):
        if S[i]=='R':
            R.append(i)
        if S[i]=='G':
            G.append(i)
        if S[i]=='B':
            B.append(i)

    ans = 0
    for i in R:
        index_G = bs.bisect_left(G, i)
        index_B = bs.bisect_left(B, i)
        # print(i, index_G, index_B)
        ans += index_G*(len(B)-index_B)
        # print('ansGRB', i, ans)
        for j in range(index_G):
            if 2*i-G[j]<N and S[2*i-G[j]]=='B':
                ans -= 1
        ans += index_B*(len(G)-index_G)
        for j in range(index_B):
            if 2*i-B[j]<N and S[2*i-B[j]]=='G':
                ans -= 1
    # print('ansR', ans)
    for i in G:
        index_R = bs.bisect_left(R, i)
        index_B = bs.bisect_left(B, i)
        # print(i, index_R, index_B)
        ans += index_R*(len(B)-index_B)
        for j in range(index_R):
            if 2*i-R[j]<N and S[2*i-R[j]]=='B':
                ans -= 1
        # print('ansRGB', ans)
        ans += index_B*(len(R)-index_R)
        for j in range(index_B):
            if 2*i-B[j]<N and S[2*i-B[j]]=='R':
                ans -= 1
        # print('ansBGR', ans)
    # print('ansG', ans)
    for i in B:
        index_G = bs.bisect_left(G, i)
        index_R = bs.bisect_left(R, i)
        # print(i, index_G, index_B)
        ans += index_G*(len(R)-index_R)
        for j in range(index_G):
            if 2*i-G[j]<N and S[2*i-G[j]]=='R':
                ans -= 1
        ans += index_R*(len(G)-index_G)
        for j in range(index_R):
            if 2*i-R[j]<N and S[2*i-R[j]]=='G':
                ans -= 1
    # print('ansB', ans)

    print(ans)


if __name__ == '__main__':
    resolve()
