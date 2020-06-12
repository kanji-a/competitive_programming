import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    tetrahedral_num = [i*(i+1)*(i+2)//6 for i in range(1, 201)]
    tetrahedral_num_odd = [i for i in tetrahedral_num if i%2==1]
    n = []
    while True:
        tmp = int(input())
        if tmp==0:
            break
        else:
            n.append(tmp)
    max_n = max(n)

    # dp[i]: 数iを構成する最小個数
    dp = [float('inf')]*(max_n+1)
    dp[0] = 0
    for i in range(1, max_n+1):
        tmp = []
        for j in tetrahedral_num:
            if i-j>=0:
                tmp.append(dp[i-j])
        dp[i] = min(tmp) + 1

    dp_odd = [float('inf')]*(max_n+1)
    dp_odd[0] = 0
    for i in range(1, max_n+1):
        tmp = []
        for j in tetrahedral_num_odd:
            if i-j>=0:
                tmp.append(dp_odd[i-j])
        dp_odd[i] = min(tmp) + 1

    for i in n:
        print(dp[i], dp_odd[i])

if __name__ == '__main__':
    resolve()