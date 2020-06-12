import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    time = [list(map(int, input().split())) for _ in range(3)]

    for i in time:
        bh = i[0]
        bm = i[1]
        bs = i[2]
        eh = i[3]
        em = i[4]
        es = i[5]
        ts = (eh*3600+em*60+es) - (bh*3600+bm*60+bs)
        print(ts//3600, ts%3600//60, ts%60)

if __name__ == '__main__':
    resolve()