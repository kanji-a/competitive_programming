import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, M = map(int, input().split())
    ks = [list(map(int, input().split())) for _ in range(M)]
    p = list(map(int, input().split()))

    ans = 0
    # スイッチのパターン
    for i in range(2**N):
        # 電球
        flg = True
        for j in range(M):
            # 電球に繋がれたスイッチ
            c = 0
            for k in range(ks[j][0]):
                if (i>>(ks[j][k+1]-1))&1:
                    c += 1
            if c%2!=p[j]:
                flg = False
        if flg:
            ans += 1
    print(ans)

if __name__ == '__main__':
    resolve()
