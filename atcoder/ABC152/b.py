a, b = input().split()

aa = ''.join([a for _ in range(int(b))])
bb = ''.join([b for _ in range(int(a))])

print(sorted([aa, bb])[0])