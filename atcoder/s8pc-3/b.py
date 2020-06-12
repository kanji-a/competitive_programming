import sys, itertools, copy
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    H, W, K = LI()
    c = [[int(i) for i in S()] for _ in range(H)]

    ans = 0
    for i, j in itertools.product(range(H), range(W)):
        c_tmp = copy.deepcopy(c)
        c_tmp[i][j] = 0
        score = 0
        chain_cnt = 0
        while True:
            # 落下処理
            # その石がどれだけ落下するかの算出
            drop = [[0]*W for _ in range(H)]
            for k in range(W):
                for l in range(H-1):
                    drop[H-l-2][k] = drop[H-l-1][k] + (1 if c_tmp[H-l-1][k]==0 else 0)
            # print('drop')
            # for i in drop:
            #     print(i)
            
            # 落下先にコピー
            for k in range(W):
                for l in range(H):
                    if drop[H-l-1][k]!=0:
                        c_tmp[H-l-1+drop[H-l-1][k]][k] = c_tmp[H-l-1][k]
                        c_tmp[H-l-1][k] = 0
            # print('dropped s')
            # for i in c_tmp:
            #     print(i)

            # 消滅判定
            num_sum = 0
            for k in range(H):
                prev = 0
                cnt = 1
                for l in range(W):
                    if c_tmp[k][l]==prev:
                        cnt += 1
                    else:
                        if cnt>=K:
                            num_sum += prev*cnt
                            for m in range(cnt):
                                c_tmp[k][l-cnt+m] = 0
                        prev = c_tmp[k][l]
                        cnt = 1
                if cnt>=K:
                    num_sum += prev*cnt
                    for m in range(cnt):
                        c_tmp[k][l+1-cnt+m] = 0
            # print('s')
            # for i in s:
            #     print(i)
            if num_sum==0:
                break
            score += (2**chain_cnt) * num_sum
            chain_cnt += 1
        ans = max(score, ans)

    print(ans)

if __name__ == '__main__':
    resolve()