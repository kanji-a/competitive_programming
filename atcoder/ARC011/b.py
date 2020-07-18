import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    w = LSS()

    ans = []
    for i in range(N):
        tmp = ''
        for j in w[i]:
            if j in ('b', 'c', 'B', 'C'):
                tmp += '1'
            elif j in ('d', 'w', 'D', 'W'):
                tmp += '2'
            elif j in ('t', 'j', 'T', 'J'):
                tmp += '3'
            elif j in ('f', 'q', 'F', 'Q'):
                tmp += '4'
            elif j in ('l', 'v', 'L', 'V'):
                tmp += '5'
            elif j in ('s', 'x', 'S', 'X'):
                tmp += '6'
            elif j in ('p', 'm', 'P', 'M'):
                tmp += '7'
            elif j in ('h', 'k', 'H', 'K'):
                tmp += '8'
            elif j in ('n', 'g', 'N', 'G'):
                tmp += '9'
            elif j in ('z', 'r', 'Z', 'R'):
                tmp += '0'
            elif j == ' ':
                tmp += ' '
        if tmp.count(' ') != len(tmp):
            ans.append(tmp)

    print(*ans)

if __name__ == '__main__':
    resolve()
