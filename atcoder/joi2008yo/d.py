import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    m = int(input())
    constellation_xy = [list(map(int, input().split())) for _ in range(m)]
    n = int(input())
    photo_xy = [list(map(int, input().split())) for _ in range(n)]
    constellation_xy_n = [[i[0]-constellation_xy[0][0], i[1]-constellation_xy[0][1]] for i in constellation_xy]

    for i in photo_xy:
        ok = True
        for j in constellation_xy_n:
            if [i[0]+j[0], i[1]+j[1]] not in photo_xy:
                ok = False
                break
        if ok:
            print(i[0]-constellation_xy[0][0], i[1]-constellation_xy[0][1])
            break

if __name__ == '__main__':
    resolve()
