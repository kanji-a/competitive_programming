import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    S = input()

    cnt = [0]*2019
    cnt[0] = 1

    # Sの右側から1ずつ左に伸ばして、cntの対応するところに加算
    rmd = 0
    num_rate = 1
    L = len(S)
    for i in range(L):
        rmd = (int(S[L-i-1])*num_rate + rmd) % 2019
        num_rate = num_rate*10%2019
        cnt[rmd] += 1

    ans = sum([i*(i-1)//2 for i in cnt])
    print(ans)

if __name__ == '__main__':
    resolve()
