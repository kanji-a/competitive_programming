import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    n = I()

    def rec(depth, p0_x, p0_y, p1_x, p1_y):
        if depth!=n:
            p2_x = p0_x*2/3 + p1_x*1/3
            p2_y = p0_y*2/3 + p1_y*1/3
            p4_x = p0_x*1/3 + p1_x*2/3
            p4_y = p0_y*1/3 + p1_y*2/3
            p3_x = (1/2)*(p4_x-p2_x)-(3**0.5/2)*(p4_y-p2_y)+p2_x
            p3_y = (3**0.5/2)*(p4_x-p2_x)+(1/2)*(p4_y-p2_y)+p2_y

            rec(depth+1, p0_x, p0_y, p2_x, p2_y)
            print(p2_x, p2_y)
            rec(depth+1, p2_x, p2_y, p3_x, p3_y)
            print(p3_x, p3_y)
            rec(depth+1, p3_x, p3_y, p4_x, p4_y)
            print(p4_x, p4_y)
            rec(depth+1, p4_x, p4_y, p1_x, p1_y)
    
    print(0, 0)
    rec(0, 0, 0, 100, 0)
    print(100, 0)

if __name__ == '__main__':
    resolve()