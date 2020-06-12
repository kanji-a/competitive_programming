import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    A_neg = sorted([a for a in A if a < 0])
    A_zero = [a for a in A if a==0]
    A_pos = sorted([a for a in A if a > 0])
    A_neg_pair_num = len(A_neg)*len(A_pos)
    A_zero_pair_num = len(A_zero)*(len(A_zero)-1)
    A_pos_pair_num = len(A_pos)*(len(A_pos)-1)+len(A_neg)*(len(A_neg)-1)
    ans = 0

    if K <= A_neg_pair_num:
        i1 = 0
        i2 = 0
        cnt = 1
        for i in range(N):
            for j in range(i+1, N):
                # print(A[i]*A[j], cnt)
                cnt+=1
                if cnt==K:
                    i1 = i
                    i2 = j
        print(A_neg[i1], A_pos[-i2+1])
        ans = A_neg[i1]*A_pos[-i2+1]
    elif A_neg_pair_num < K <= A_neg_pair_num+A_zero_pair_num:
        ans = 0
    else:
        pass
    print(ans)


if __name__ == '__main__':
    resolve()
