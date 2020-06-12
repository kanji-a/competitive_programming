N = int(input())
C = list(map(int, input().split()))
Q = int(input())
S = [input() for i in range(Q)]

total = 0
min_all = min(C)
min_odd = min([C[i] for i in range(N) if i%2==0])
sold_all = 0
sold_odd = 0

for s in S:
    type = s.split()[0]
    if type == '1':
        cid = int(s.split()[1])
        num = int(s.split()[2])
        if cid % 2 == 1:
            if num <= C[cid-1] - sold_all - sold_odd:
                after = C[cid-1] - sold_all - sold_odd - num
                min_all = min(after, min_all)
                min_odd = min(after, min_odd)
                C[cid-1] -= num
                total += num
        else:
            if num <= C[cid-1] - sold_all:
                after = C[cid-1] - sold_all - num
                min_all = min(after, min_all)
                C[cid-1] -= num
                total += num

    if type == '2':
        num = int(s.split()[1])
        if num <= min_odd:
            after = min_odd - num
            min_odd = after
            min_all = min(after, min_all)
            total += num*((N+1)//2)
            sold_odd += num

    if type == '3':
        num = int(s.split()[1])
        if num <= min_all:
            after = min_all - num
            min_all = after
            min_odd -= num
            total += num*N
            sold_all += num

print(total)