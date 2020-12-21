import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def _inv_gcd(a: int, b: int) -> typing.Tuple[int, int]:
    a %= b
    if a == 0:
        return (b, 0)

    # Contracts:
    # [1] s - m0 * a = 0 (mod b)
    # [2] t - m1 * a = 0 (mod b)
    # [3] s * |m1| + t * |m0| <= b
    s = b
    t = a
    m0 = 0
    m1 = 1

    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u  # |m1 * u| <= |m1| * s <= b

        # [3]:
        # (s - t * u) * |m1| + t * |m0 - m1 * u|
        # <= s * |m1| - t * u * |m1| + t * (|m0| + |m1| * u)
        # = s * |m1| + t * |m0| <= b

        s, t = t, s
        m0, m1 = m1, m0

    # by [3]: |m0| <= b/g
    # by g != b: |m0| < b/g
    if m0 < 0:
        m0 += b // s

    return (s, m0)

def crt(r: typing.List[int], m: typing.List[int]) -> typing.Tuple[int, int]:
    assert len(r) == len(m)

    n = len(r)

    # Contracts: 0 <= r0 < m0
    r0 = 0
    m0 = 1
    for i in range(n):
        assert 1 <= m[i]
        r1 = r[i] % m[i]
        m1 = m[i]
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0 % m1 != r1:
                return (0, 0)
            continue

        # assume: m0 > m1, lcm(m0, m1) >= 2 * max(m0, m1)

        '''
        (r0, m0), (r1, m1) -> (r2, m2 = lcm(m0, m1));
        r2 % m0 = r0
        r2 % m1 = r1
        -> (r0 + x*m0) % m1 = r1
        -> x*u0*g % (u1*g) = (r1 - r0) (u0*g = m0, u1*g = m1)
        -> x = (r1 - r0) / g * inv(u0) (mod u1)
        '''

        # im = inv(u0) (mod u1) (0 <= im < u1)
        g, im = _inv_gcd(m0, m1)

        u1 = m1 // g
        # |r1 - r0| < (m0 + m1) <= lcm(m0, m1)
        if (r1 - r0) % g:
            return (0, 0)

        # u1 * u1 <= m1 * m1 / g / g <= m0 * m1 / g = lcm(m0, m1)
        x = (r1 - r0) // g % u1 * im % u1

        '''
        |r0| + |m0 * x|
        < m0 + m0 * (u1 - 1)
        = m0 + m0 * m1 / g - m0
        = lcm(m0, m1)
        '''

        r0 += x * m0
        m0 *= u1  # -> lcm(m0, m1)
        if r0 < 0:
            r0 += m0

    return (r0, m0)

def resolve():
    T = I()
    for _ in range(T):
        N, S, K = LI()
        # S+K*a≡0(mod N)を解く
        # x=K*aと置いて、以下の連立合同式にする
        # x≡-S(mod N)
        # x≡0(mod K)
        p = crt([-S, 0], [N, K])
        if p == (0, 0):
            print(-1)
        else:
            print(p[0] // K)
            
if __name__ == '__main__':
    resolve()
