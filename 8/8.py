import sys
with sys.stdin as i:
    n = int(i.readline())
    for _ in range(n):
        tx, ty = [int(a) for a in i.readline().split()]
        grid = [['10%' for __ in range(20)] for ___ in range(20)]

        for y in range(max(ty - 2, 0), min(19, ty + 3)):
            print(y)
            ydiff = abs(y - ty)
            for x in range(max(tx - 2, 0), min(19, tx + 3)):
                xdiff = abs(x - tx)

                if xdiff == 0 and ydiff == 0:
                    grid[y][x] = '100%'
                elif (xdiff == 1 and ydiff <= 1) or (ydiff == 1 and xdiff <= 1):
                    grid[y][x] = '50%'
                else:
                    grid[y][x] = '25%'

        print('\n'.join([' '.join(elements) for elements in grid]))