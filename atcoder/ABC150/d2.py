import sys, fractions, functools
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

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return functools.reduce(lcm_base, numbers, 1)

def resolve():
    N, M = LI()
    a = LI()

    a_half = [i//2 for i in a]
    a_half_lcm = lcm_list(a_half)
    has_scm = not 0 in [a_half_lcm//i%2 for i in a_half]

    if has_scm:
        print((M-a_half_lcm)//(2*a_half_lcm)+1)
    else:
        print(0)

if __name__ == '__main__':
    resolve()