N = int(input())
A = [int(input()) for i in range(N)]
 
counter = [0 for _ in range(N)]
for i in A:
    counter[i-1] += 1

if (not 0 in counter):
    print('Correct')
else:
    print(counter.index(2)+1, counter.index(0)+1)