import sys
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
    ABCD = S()
    A = ABCD[0]
    BCD = ABCD[1:]

    ans = [A, '', BCD[0], '', BCD[1], '', BCD[2], '=', '7']
    for i in range(2 ** 3):
        tmp = int(A)
        for j in range(3):
            if i >> j & 1:
                tmp += int(BCD[j])
                ans[j*2+1] = '+'
            else:
                tmp -= int(BCD[j])
                ans[j*2+1] = '-'
        if tmp == 7:
            print(''.join(ans))
            break

if __name__ == '__main__':
    resolve()
