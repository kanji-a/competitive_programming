import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    K = int(input())

    def dfs(depth, max_depth, num):
        if depth==max_depth:
            lunlun_temp.append(''.join([str(i) for i in num]))
        elif depth==0:
            for i in range(1, 10):
                dfs(depth+1, max_depth, num+[i])
        else:
            for i in range(3):
                if 0<=num[-1]-1+i<=9:
                    dfs(depth+1, max_depth, num+[num[-1]-1+i])

    lunlun = []

    i = 1
    while len(lunlun)<K:
        lunlun_temp = []
        dfs(0, i, [])
        lunlun += lunlun_temp
        i += 1

    print(lunlun[K-1])

if __name__ == '__main__':
    resolve()
